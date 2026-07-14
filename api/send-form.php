<?php
/**
 * Обработчик формы обратной связи.
 * Принимает POST-запрос, валидирует данные и отправляет email.
 */

// Загружаем конфиг
$config = require __DIR__ . '/config.php';

if (!$config['debug']) {
    ini_set('display_errors', '0');
    error_reporting(0);
}

// Только POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    respond(405, 'Метод не поддерживается');
}

// Honeypot-защита от ботов (скрытое поле должно оставаться пустым)
if (!empty($_POST['website'])) {
    respond(400, 'Подозрительная активность');
}

// Получаем и очищаем данные
$name    = sanitize($_POST['name'] ?? '');
$phone   = sanitize($_POST['phone'] ?? '');
$email   = filter_var(sanitize($_POST['email'] ?? ''), FILTER_SANITIZE_EMAIL);
$type    = sanitize($_POST['type'] ?? '');
$message = sanitize($_POST['message'] ?? '');
$page    = sanitize($_POST['page'] ?? $_SERVER['HTTP_REFERER'] ?? 'Неизвестно');

// Валидация
$errors = [];
if (empty($name)) {
    $errors[] = 'Укажите ваше имя';
}
if (empty($phone)) {
    $errors[] = 'Укажите телефон';
} elseif (!preg_match('/^[\d\s\+\-\(\)]{7,20}$/', $phone)) {
    $errors[] = 'Укажите корректный телефон';
}
if (!empty($email) && !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    $errors[] = 'Укажите корректный email';
}

if ($errors) {
    respond(422, implode('; ', $errors));
}

// Формируем тему и тело письма
$subject = $config['subject_prefix'] . ' ' . $type ?: 'Новая заявка';
$date    = date('d.m.Y H:i');
$ip      = $_SERVER['REMOTE_ADDR'] ?? 'Неизвестно';

$body = "Новая заявка с сайта Южный Ветер\n\n";
$body .= "Дата: {$date}\n";
$body .= "Страница: {$page}\n";
$body .= "IP: {$ip}\n\n";
$body .= "Имя: {$name}\n";
$body .= "Телефон: {$phone}\n";
$body .= "Email: " . ($email ?: 'не указан') . "\n";
$body .= "Тип оборудования: " . ($type ?: 'не выбран') . "\n\n";
$body .= "Сообщение:\n" . ($message ?: 'нет') . "\n";

// HTML-версия письма
$htmlBody = buildHtmlBody([
    'Дата'               => $date,
    'Страница'           => $page,
    'IP'                 => $ip,
    'Имя'                => $name,
    'Телефон'            => $phone,
    'Email'              => $email ?: 'не указан',
    'Тип оборудования'   => $type ?: 'не выбран',
    'Сообщение'          => nl2br($message ?: 'нет'),
]);

// Отправка
$sent = false;
if ($config['send_method'] === 'smtp') {
    $sent = sendViaSmtp($config, $subject, $body, $htmlBody);
} else {
    $sent = sendViaMail($config, $subject, $body, $htmlBody);
}

if ($sent) {
    respond(200, 'Заявка успешно отправлена', ['redirect' => $config['thank_you_url']]);
} else {
    respond(500, 'Не удалось отправить заявку. Попробуйте позже.');
}

// ===== Функции =====

function sanitize(string $value): string
{
    $value = trim($value);
    $value = stripslashes($value);
    $value = htmlspecialchars($value, ENT_QUOTES, 'UTF-8');
    return $value;
}

function respond(int $code, string $message, array $data = []): void
{
    $config = $GLOBALS['config'] ?? [];
    $isAjax = isset($_SERVER['HTTP_X_REQUESTED_WITH']) &&
              strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) === 'xmlhttprequest';

    if ($isAjax) {
        http_response_code($code);
        header('Content-Type: application/json; charset=utf-8');
        echo json_encode(array_merge(['success' => $code === 200, 'message' => $message], $data));
        exit;
    }

    // Обычная отправка формы — редирект
    if ($code === 200 && !empty($config['thank_you_url'])) {
        header('Location: ' . $config['thank_you_url']);
        exit;
    }

    http_response_code($code);
    echo '<p>' . htmlspecialchars($message) . '</p>';
    echo '<p><a href="/">Вернуться на главную</a></p>';
    exit;
}

function buildHtmlBody(array $fields): string
{
    $rows = '';
    foreach ($fields as $label => $value) {
        $rows .= "<tr><td style='padding:8px;border:1px solid #e2e8f0;font-weight:600;'>" . htmlspecialchars($label) . "</td><td style='padding:8px;border:1px solid #e2e8f0;'>" . $value . "</td></tr>";
    }
    return "<html><body><h2>Новая заявка с сайта Южный Ветер</h2><table style='border-collapse:collapse;width:100%;max-width:600px;'>{$rows}</table></body></html>";
}

function sendViaMail(array $config, string $subject, string $textBody, string $htmlBody): bool
{
    $to      = $config['recipient_email'];
    $headers = "From: " . $config['recipient_email'] . "\r\n";
    $headers .= "Reply-To: " . $config['recipient_email'] . "\r\n";
    $headers .= "MIME-Version: 1.0\r\n";
    $headers .= "Content-Type: multipart/alternative; boundary=\"boundary\"\r\n";

    $message = "--boundary\r\n";
    $message .= "Content-Type: text/plain; charset=UTF-8\r\n";
    $message .= "Content-Transfer-Encoding: 7bit\r\n\r\n";
    $message .= $textBody . "\r\n\r\n";
    $message .= "--boundary\r\n";
    $message .= "Content-Type: text/html; charset=UTF-8\r\n";
    $message .= "Content-Transfer-Encoding: 7bit\r\n\r\n";
    $message .= $htmlBody . "\r\n\r\n";
    $message .= "--boundary--";

    return mail($to, '=?UTF-8?B?' . base64_encode($subject) . '?=', $message, $headers);
}

function sendViaSmtp(array $config, string $subject, string $textBody, string $htmlBody): bool
{
    // Для SMTP-отправки подключите PHPMailer:
    // composer require phpmailer/phpmailer
    // и раскомментируйте код ниже.

    /*
    require __DIR__ . '/../vendor/autoload.php';
    $mail = new PHPMailer\PHPMailer\PHPMailer(true);
    $mail->isSMTP();
    $mail->Host       = $config['smtp']['host'];
    $mail->SMTPAuth   = true;
    $mail->Username   = $config['smtp']['username'];
    $mail->Password   = $config['smtp']['password'];
    $mail->SMTPSecure = $config['smtp']['secure'];
    $mail->Port       = $config['smtp']['port'];
    $mail->CharSet    = 'UTF-8';

    $mail->setFrom($config['smtp']['username'], $config['recipient_name']);
    $mail->addAddress($config['recipient_email']);
    foreach ($config['cc'] as $cc) {
        $mail->addCC($cc);
    }

    $mail->isHTML(true);
    $mail->Subject = $subject;
    $mail->Body    = $htmlBody;
    $mail->AltBody = $textBody;

    return $mail->send();
    */

    // Если PHPMailer не подключен — fallback на mail()
    return sendViaMail($config, $subject, $textBody, $htmlBody);
}
