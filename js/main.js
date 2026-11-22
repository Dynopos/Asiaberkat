/* Asia Berkat — interaksi laman */
(() => {
  'use strict';
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  /* Nav: bayang semasa skrol + menu telefon */
  const nav = $('#nav'), burger = $('#burger'), menu = $('#menu');
  const onScroll = () => nav.classList.toggle('is-scrolled', scrollY > 10);
  onScroll(); addEventListener('scroll', onScroll, { passive: true });
  const closeMenu = () => { menu.classList.remove('is-open'); burger.setAttribute('aria-expanded', 'false'); };
  burger.addEventListener('click', () => {
    const open = !menu.classList.contains('is-open');
    menu.classList.toggle('is-open', open); burger.setAttribute('aria-expanded', String(open));
  });
  $$('a', menu).forEach(a => a.addEventListener('click', closeMenu));
  addEventListener('keydown', e => { if (e.key === 'Escape') closeMenu(); });

  /* Pautan menu aktif */
  const links = $$('.menu a[href^="#"]');
  const secObs = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return;
    links.forEach(a => a.classList.toggle('is-active', a.getAttribute('href') === '#' + e.target.id));
  }), { rootMargin: '-45% 0px -50% 0px' });
  links.forEach(a => { const s = $(a.getAttribute('href')); if (s) secObs.observe(s); });

  /* Muncul semasa skrol */
  const rev = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) { e.target.classList.add('is-in'); rev.unobserve(e.target); }
  }), { threshold: .12, rootMargin: '0px 0px -40px 0px' });
  $$('.reveal').forEach(el => rev.observe(el));

  /* Marquee: gandakan item supaya gelung lancar */
  const mq = $('#marquee');
  if (mq) mq.innerHTML += mq.innerHTML.replace(/<li>/g, '<li aria-hidden="true">');

  /* Peta: muat bila hampir kelihatan, tukar ikut cawangan */
  const frame = $('#mapFrame'), mapBox = frame && frame.closest('.loc__map');
  const branches = $$('.br');
  let mapReady = false, current = branches[0];
  const mapSrc = q => 'https://www.google.com/maps?q=' + encodeURIComponent(q) + '&output=embed';
  const showBranch = br => {
    current = br;
    branches.forEach(b => { b.classList.toggle('is-on', b === br); $('.br__pick', b).setAttribute('aria-pressed', String(b === br)); });
    if (mapReady) frame.src = mapSrc(br.dataset.q);
  };
  branches.forEach(b => $('.br__pick', b).addEventListener('click', () => showBranch(b)));
  if (frame) {
    frame.addEventListener('load', () => frame.src && mapBox.classList.add('is-loaded'));
    new IntersectionObserver((es, o) => {
      if (!es[0].isIntersecting) return;
      mapReady = true; frame.src = mapSrc(current.dataset.q); o.disconnect();
    }, { rootMargin: '300px' }).observe(mapBox);
  }

  /* Lightbox: galeri pelanggan + poster pelan */
  const lb = $('#lb'), lbImg = $('#lbImg'), lbCap = $('#lbCap'), prev = $('#lbPrev'), next = $('#lbNext');
  const sets = {
    unifi: [
      ['assets/img/poster-unifi-nubia-1200.webp', 'Poster Unifi Mobile — Pakej Nubia A77 RM59 sebulan'],
      ['assets/img/poster-unifi-freefon-1200.webp', 'Poster Unifi Mobile — Free Fon untuk pengguna unifi home']
    ],
    celcomdigi: [
      ['assets/img/poster-power-plus-1200.webp', 'Poster CelcomDigi — 5G Power+ 55 & Power+ 65'],
      ['assets/img/poster-celcomdigi-nov26-1200.webp', 'Poster CelcomDigi — ringkasan pelan prabayar Nov 2026']
    ],
    gal: $$('.gal button').map(b => [b.dataset.full, b.dataset.cap])
  };
  let list = [], idx = 0, lastFocus = null;
  const render = () => {
    const [src, cap] = list[idx];
    lbImg.src = src; lbImg.alt = cap; lbCap.textContent = cap;
    prev.hidden = next.hidden = list.length < 2;
  };
  const openLb = (name, i = 0) => {
    list = sets[name]; idx = i; lastFocus = document.activeElement;
    render(); lb.hidden = false; document.body.style.overflow = 'hidden'; $('#lbX').focus();
  };
  const closeLb = () => { lb.hidden = true; document.body.style.overflow = ''; lbImg.removeAttribute('src'); lastFocus && lastFocus.focus(); };
  const step = d => { idx = (idx + d + list.length) % list.length; render(); };
  $$('[data-lb]').forEach(b => b.addEventListener('click', () => openLb(b.dataset.lb)));
  $$('.gal button').forEach((b, i) => b.addEventListener('click', () => openLb('gal', i)));
  $('#lbX').addEventListener('click', closeLb);
  prev.addEventListener('click', () => step(-1));
  next.addEventListener('click', () => step(1));
  lb.addEventListener('click', e => { if (e.target === lb) closeLb(); });
  addEventListener('keydown', e => {
    if (lb.hidden) return;
    if (e.key === 'Escape') closeLb();
    if (e.key === 'ArrowLeft') step(-1);
    if (e.key === 'ArrowRight') step(1);
    if (e.key === 'Tab') { // kekalkan fokus dalam dialog
      const f = $$('button:not([hidden])', lb); const first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });
  let sx = 0;
  lb.addEventListener('touchstart', e => { sx = e.touches[0].clientX; }, { passive: true });
  lb.addEventListener('touchend', e => { const dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 50 && list.length > 1) step(dx < 0 ? 1 : -1); });

  const yr = $('#yr'); if (yr) yr.textContent = new Date().getFullYear();
})();
