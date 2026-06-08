class SiteHeader extends HTMLElement {
  connectedCallback() {
    const rootPath = this.getAttribute('root-path') || '';
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    
    // helper to set active class
    const isActive = (path) => currentPath === path ? 'aria-current="page"' : '';

    this.innerHTML = `
    <header class="site-header-fixed">
      <div class="container nav-wrapper">
        <!-- Logo -->
        <a href="${rootPath}index.html" class="logo-link" id="logo-home-link" aria-label="DF Cleaning Homepage">
          <img src="${rootPath}assets/logo2.png" alt="DF Cleaning Logo">
        </a>

        <!-- Desktop & Tablet Navigation -->
        <nav class="main-nav" id="main-navigation" aria-label="Primary Navigation">
          <ul class="nav-list">
            <li class="nav-item">
              <a href="${rootPath}index.html" class="nav-link" ${isActive('index.html')}>HOME</a>
            </li>
            <li class="nav-item has-dropdown">
              <div class="nav-link-wrapper" style="display: flex; align-items: center; width: 100%;">
                <a href="${rootPath}services.html" class="nav-link" style="flex-grow: 1;" ${isActive('services.html')}>SERVICES</a>
                <button class="mobile-accordion-toggle" aria-expanded="false" aria-label="Toggle Services Menu">
                  <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                </button>
              </div>
              <ul class="dropdown-menu">
                <li><a href="${rootPath}services/home-cleaning.html" class="dropdown-link">Home Cleaning</a></li>
                <li><a href="${rootPath}services/on-going-cleaning.html" class="dropdown-link">On-Going Cleaning</a></li>
                <li><a href="${rootPath}services/commercial-cleaning.html" class="dropdown-link">Commercial / Industrial Cleaning</a></li>
                <li><a href="${rootPath}services/move-in-move-out.html" class="dropdown-link">Move-In / Move-Out Cleaning</a></li>
                <li><a href="${rootPath}services/window-washing.html" class="dropdown-link">Window Washing</a></li>
                <li><a href="${rootPath}services/carpet-cleaning.html" class="dropdown-link">Carpet Cleaning</a></li>
                <li><a href="${rootPath}services/coaching.html" class="dropdown-link">Coaching</a></li>
              </ul>
            </li>
            <li class="nav-item">
              <a href="${rootPath}about.html" class="nav-link" ${isActive('about.html')}>ABOUT</a>
            </li>
            <li class="nav-item">
              <a href="${rootPath}gallery.html" class="nav-link" ${isActive('gallery.html')}>GALLERY</a>
            </li>
            <li class="nav-item">
              <a href="${rootPath}estimate.html" class="nav-link" ${isActive('estimate.html')}>CONTACT</a>
            </li>
          </ul>
        </nav>

        <!-- Action Buttons -->
        <div class="header-actions">
          <a href="tel:+17373679177" class="btn btn-outline" id="header-call-btn">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
            </svg>
            (737) 367-9177
          </a>
          <a href="${rootPath}estimate.html" class="btn btn-primary" id="header-estimate-btn">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
              <line x1="16" y1="2" x2="16" y2="6"></line>
              <line x1="8" y1="2" x2="8" y2="6"></line>
              <line x1="3" y1="10" x2="21" y2="10"></line>
            </svg>
            Get a Quote
          </a>
        </div>

        <!-- Mobile Hamburger Toggle Menu -->
        <button class="menu-toggle" id="mobile-menu-toggle" aria-label="Toggle navigation menu" aria-expanded="false" aria-controls="main-navigation">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </header>
    `;

    // Wait for the next tick so the DOM is ready
    setTimeout(() => {
        const headerEl = this.querySelector('.site-header-fixed');
        if(!headerEl) return;
        const updateScroll = () => {
          if (window.scrollY > 20) {
            headerEl.classList.add('is-scrolled');
          } else {
            headerEl.classList.remove('is-scrolled');
          }
        };
        window.addEventListener('scroll', updateScroll, { passive: true });
        updateScroll();
    }, 0);
  }
}
customElements.define('site-header', SiteHeader);
