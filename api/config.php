<?php
/**
 * Конфигурация отправки форм.
 * Заполните реальные данные перед запуском на продакшене.
 */

// Кому отправлять заявки
return [
    'recipient_email' => 'info@swind.su',
    'recipient_name'  => 'ООО Южный Ветер',
    'subject_prefix'  => '[Заявка с сайта]',

    // Режим отправки: 'mail' — стандартная функция PHP mail()
    // Для SMTP установите 'smtp' и заполните SMTP-настройки ниже.
    'send_method' => 'mail',

    // SMTP-настройки (используются, если send_method = 'smtp')
    'smtp' => [
        'host'     => 'smtp.example.com',
        'port'     => 587,
        'username' => 'user@example.com',
        'password' => 'your_smtp_password',
        'secure'   => 'tls',  // 'tls', 'ssl' или ''
    ],

    // Дополнительные получатели (копии)
    'cc' => [],

    // Перенаправление после успешной отправки
    'thank_you_url' => '/pages/thank-you.html',

    // Включить вывод ошибок (только для отладки)
    'debug' => false,
];
