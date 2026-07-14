// Async form handler
(function () {
  function initForms() {
    document.querySelectorAll('[data-form]').forEach(form => {
      if (form.dataset.formInitialized) return;
      form.dataset.formInitialized = 'true';

      const submitBtn = form.querySelector('button[type="submit"]');
      const originalText = submitBtn ? submitBtn.textContent : '';
      const resultEl = form.querySelector('[data-form-result]') || document.createElement('div');
      resultEl.className = 'form-result';
      if (!form.querySelector('[data-form-result]')) {
        form.appendChild(resultEl);
      }

      form.addEventListener('submit', async (e) => {
        e.preventDefault();

        if (submitBtn) {
          submitBtn.disabled = true;
          submitBtn.textContent = 'Отправка...';
        }
        resultEl.textContent = '';
        resultEl.className = 'form-result';

        try {
          const formData = new FormData(form);
          const response = await fetch(form.action, {
            method: form.method || 'POST',
            body: formData,
            headers: { 'X-Requested-With': 'XMLHttpRequest' }
          });

          const data = await response.json().catch(() => ({
            success: response.ok,
            message: response.ok ? 'Заявка отправлена' : 'Ошибка отправки'
          }));

          if (data.success && data.redirect) {
            window.location.href = data.redirect;
            return;
          }

          resultEl.textContent = data.message || (data.success ? 'Заявка отправлена' : 'Ошибка отправки');
          resultEl.classList.add(data.success ? 'form-result-success' : 'form-result-error');

          if (data.success) {
            form.reset();
          }
        } catch (err) {
          resultEl.textContent = 'Не удалось отправить заявку. Проверьте подключение к интернету.';
          resultEl.classList.add('form-result-error');
        } finally {
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.textContent = originalText;
          }
        }
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initForms);
  } else {
    initForms();
  }
})();
