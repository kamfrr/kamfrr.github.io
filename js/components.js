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

function toggleMenu() {
  const menu = document.getElementById('mobileMenu');
  if (menu) menu.classList.toggle('active');
}

function closeMenu() {
  const menu = document.getElementById('mobileMenu');
  if (menu) menu.classList.remove('active');
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
    if (header && !header.contains(e.target)) closeMenu();
  });
});
