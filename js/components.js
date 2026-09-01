// Load shared components
async function loadComponent(selector, path) {
  const el = document.querySelector(selector);
  if (!el) return;
  try {
    const res = await fetch(path);
    if (res.ok) {
      el.innerHTML = await res.text();
    }
  } catch (e) {
    console.warn('Failed to load component', path, e);
  }
}

function carouselMove(btn, dir) {
  const box = btn.closest('[data-carousel]');
  if (!box) return;
  const imgs = JSON.parse(box.dataset.carousel);
  const img = box.querySelector('img');
  const counter = box.querySelector('.carousel-counter');
  const i = ((parseInt(box.dataset.i || '0', 10) + dir) % imgs.length + imgs.length) % imgs.length;
  box.dataset.i = i;
  img.src = imgs[i];
  if (counter) counter.textContent = (i + 1) + ' / ' + imgs.length;
}

function toggleMenu() {
  const menu = document.getElementById('mobileMenu');
  const btn = document.querySelector('.menu-toggle');
  if (!menu) return;
  const open = menu.classList.toggle('active');
  if (btn) {
    btn.classList.toggle('active', open);
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  }
  document.body.classList.toggle('menu-open', open);
}

function closeMenu() {
  const menu = document.getElementById('mobileMenu');
  const btn = document.querySelector('.menu-toggle');
  if (menu) menu.classList.remove('active');
  if (btn) {
    btn.classList.remove('active');
    btn.setAttribute('aria-expanded', 'false');
  }
  document.body.classList.remove('menu-open');
}

function toggleCatalog() {
  const extra = document.getElementById('catalogExtra');
  const btn = document.getElementById('catalogToggle');
  if (!extra || !btn) return;
  const open = extra.classList.toggle('expanded');
  btn.textContent = open ? 'Свернуть каталог' : 'Показать весь каталог';
  btn.setAttribute('aria-expanded', open ? 'true' : 'false');
}

function initHeaderScroll() {
  const header = document.querySelector('.site-header');
  if (!header) return;
  const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 10);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });
}

function initRevealAnimations() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -60px 0px' });

  document.querySelectorAll('.reveal, .stagger-children').forEach(el => observer.observe(el));
}

// Initialize
document.addEventListener('DOMContentLoaded', async () => {
  await Promise.all([
    loadComponent('#site-header', '/components/header.html'),
    loadComponent('#site-footer', '/components/footer.html')
  ]);

  initHeaderScroll();
  initRevealAnimations();

  // Close mobile menu on resize
  window.addEventListener('resize', () => {
    if (window.innerWidth >= 1024) closeMenu();
  });

  // Close mobile menu on outside click
  document.addEventListener('click', (e) => {
    const header = document.querySelector('.site-header');
    const menu = document.getElementById('mobileMenu');
    const inside = (header && header.contains(e.target)) || (menu && menu.contains(e.target));
    if (!inside) closeMenu();
  });
});
