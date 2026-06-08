document.addEventListener('DOMContentLoaded', () => {
  // --- Mobile Hamburger Menu Toggle ---
  const menuToggle = document.getElementById('mobile-menu-toggle');
  const mainNav = document.getElementById('main-navigation');

  if (menuToggle && mainNav) {
    menuToggle.addEventListener('click', (e) => {
      e.stopPropagation();
      const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true';
      
      menuToggle.setAttribute('aria-expanded', !isExpanded);
      menuToggle.classList.toggle('active');
      mainNav.classList.toggle('active');
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', (e) => {
      if (mainNav.classList.contains('active') && !mainNav.contains(e.target) && !menuToggle.contains(e.target)) {
        menuToggle.setAttribute('aria-expanded', 'false');
        menuToggle.classList.remove('active');
        mainNav.classList.remove('active');
      }
    });

    // Keyboard Accessibility (Esc key to close)
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mainNav.classList.contains('active')) {
        menuToggle.setAttribute('aria-expanded', 'false');
        menuToggle.classList.remove('active');
        mainNav.classList.remove('active');
        menuToggle.focus();
      }
    });
  }

  // --- Reviews Carousel ---
  const reviews = [
    {
      name: 'Arya Kannantha',
      initials: 'AK',
      date: '11 months ago',
      avatarClass: 'avatar-blue',
      text: 'Perfect job cleaning our house super time friendly and affordable. Their crew was super nice and made everything very easy.'
    },
    {
      name: 'Rayaan Bhagani',
      initials: 'RB',
      date: '11 months ago',
      avatarClass: 'avatar-teal',
      text: 'Had them clean my home. Flawless job!!'
    },
    {
      name: 'Aryan Satheesh',
      initials: 'AS',
      date: '11 months ago',
      avatarClass: 'avatar-light-blue',
      text: 'Darwin was great. Super smooth and pleasant interaction! Recommend his services to anyone!'
    },
    {
      name: 'Hannah Harvey',
      initials: 'HH',
      date: '11 months ago',
      avatarClass: 'avatar-blue',
      text: 'Very happy with the service!! Great attention to detail, amazing communication, very responsive after cleaning for setting up recurrent services!! Highly recommend!!'
    },
    {
      name: 'Gianmarco Cattinelli',
      initials: 'GC',
      date: '11 months ago',
      avatarClass: 'avatar-teal',
      text: 'Excelente servicio. Darwin es alguien muy amable y grato de conocer. Siempre está atento a cualquier necesidad que tenemos como cliente.'
    },
    {
      name: 'Людмила Должанська',
      initials: 'ЛД',
      date: '11 months ago',
      avatarClass: 'avatar-light-blue',
      text: 'I hired this team for a move out cleaning (exterior and interior) and what an amazing experience we had. The team was responsive and professional from the moment we first reached out to them, during the service and after. Our last tenant had pets in the home so a deep cleaning was required. Both teams got busy from the moment they got into the home and even sent me some pictures of things left behind just to make sure they were not throwing something away of value. We went to inspect the cleaning a day after and it was night and day. I am sure our listing won\'t stay long in the market because the house looks spotless!'
    },
    {
      name: 'Judit Melendez',
      initials: 'JM',
      date: '11 months ago',
      avatarClass: 'avatar-blue',
      text: 'If you\'re looking for clean and pristine, you\'re looking at the perfect company! Sparkly and squeaky clean is their specialty! There\'s not a mess they can\'t handle. Their customer service is admirable. Such a great experience overall, would recommend.'
    },
    {
      name: 'Kailey Klatt',
      initials: 'KK',
      date: '11 months ago',
      avatarClass: 'avatar-teal',
      text: 'An amazing experience! Highly recommend!'
    },
    {
      name: 'Dani C.R.',
      initials: 'DC',
      date: '11 months ago',
      avatarClass: 'avatar-light-blue',
      text: 'Awesome customer service, responds quickly! Their cleaning is top-notch.'
    },
    {
      name: 'Mike A',
      initials: 'MA',
      date: '11 months ago',
      avatarClass: 'avatar-blue',
      text: 'Great cleaning service. Fast response and great communication throughout. Will definitely use them again!'
    }
  ];

  const reviewCard = document.querySelector('.review-card');
  const avatar = document.querySelector('[data-review-avatar]');
  const name = document.querySelector('[data-review-name]');
  const date = document.querySelector('[data-review-date]');
  const text = document.querySelector('[data-review-text]');
  const prevButton = document.querySelector('[data-review-prev]');
  const nextButton = document.querySelector('[data-review-next]');
  const dotsWrapper = document.querySelector('[data-review-dots]');

  if (reviewCard && avatar && name && date && text && prevButton && nextButton && dotsWrapper) {
    let activeReviewIndex = 0;

    const dots = reviews.map((review, index) => {
      const dot = document.createElement('button');
      dot.className = 'review-dot';
      dot.type = 'button';
      dot.setAttribute('aria-label', `Show review from ${review.name}`);
      dot.addEventListener('click', () => setReview(index));
      dotsWrapper.appendChild(dot);
      return dot;
    });

    const renderReview = () => {
      const review = reviews[activeReviewIndex];
      avatar.textContent = review.initials;
      avatar.className = `review-avatar ${review.avatarClass}`;
      name.textContent = review.name;
      date.textContent = review.date;
      text.textContent = review.text;

      dots.forEach((dot, index) => {
        dot.setAttribute('aria-current', index === activeReviewIndex ? 'true' : 'false');
      });
    };

    const setReview = (index) => {
      activeReviewIndex = (index + reviews.length) % reviews.length;
      reviewCard.classList.add('is-transitioning');

      window.setTimeout(() => {
        renderReview();
        reviewCard.classList.remove('is-transitioning');
      }, 180);
    };

    prevButton.addEventListener('click', () => setReview(activeReviewIndex - 1));
    nextButton.addEventListener('click', () => setReview(activeReviewIndex + 1));

    renderReview();
  }

  // --- Homepage Estimate Address Toggle ---
  const addressToggle = document.getElementById('home-address-toggle');
  const addressField = document.getElementById('home-address-field');
  const addressInput = document.getElementById('home-address');

  if (addressToggle && addressField && addressInput) {
    const syncAddressField = () => {
      const shouldShowAddress = addressToggle.checked;
      addressField.hidden = !shouldShowAddress;
      addressInput.disabled = !shouldShowAddress;

      if (shouldShowAddress) {
        addressInput.focus();
      } else {
        addressInput.value = '';
      }
    };

    addressToggle.addEventListener('change', syncAddressField);
    syncAddressField();
  }

  // --- Services Grid Intersection Observer ---
  const serviceCards = document.querySelectorAll('.service-card');
  if (serviceCards.length > 0) {
    const observerOptions = {
      root: null,
      rootMargin: '0px 0px -100px 0px',
      threshold: 0.1
    };

    const cardObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry, index) => {
        if (entry.isIntersecting) {
          // Staggered delay based on index
          setTimeout(() => {
            entry.target.classList.add('is-visible');
          }, index * 100);
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    serviceCards.forEach((card) => {
      cardObserver.observe(card);

      // Tile Expand Logic
      card.addEventListener('click', function(e) {
        if (card.classList.contains('cta-card')) return;
        // Prevent toggling if clicking the 'More Information' button
        if (e.target.closest('.btn')) return;

        const isExpanded = this.classList.contains('is-expanded');
        
        // Optionally close others
        serviceCards.forEach(c => c.classList.remove('is-expanded'));

        if (!isExpanded) {
          this.classList.add('is-expanded');
          // Scroll into view if it expands out of viewport
          setTimeout(() => {
            const rect = this.getBoundingClientRect();
            if (rect.bottom > window.innerHeight || rect.top < 80) {
              this.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            }
          }, 50);
        }
      });

      // Keyboard accessibility for cards
      card.addEventListener('keydown', function(e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          this.click();
        }
      });
    });
  }

  // --- Mobile Accordion Toggle ---
  const accordionToggles = document.querySelectorAll('.mobile-accordion-toggle');
  accordionToggles.forEach(toggle => {
    toggle.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      
      const isExpanded = this.getAttribute('aria-expanded') === 'true';
      this.setAttribute('aria-expanded', !isExpanded);
      
      const dropdownMenu = this.nextElementSibling;
      if (dropdownMenu && dropdownMenu.classList.contains('dropdown-menu')) {
        dropdownMenu.classList.toggle('active');
      }
    });
  });
  // --- Gallery Page: Lenis Smooth Scroll ---
  const isReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let lenis;
  if (typeof Lenis !== 'undefined' && !isReducedMotion && document.getElementById('smooth-wrapper')) {
    lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      direction: 'vertical',
      gestureDirection: 'vertical',
      smooth: true,
      mouseMultiplier: 1,
      smoothTouch: false,
      touchMultiplier: 2,
      infinite: false,
    });

    function raf(time) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);

    // Parallax Hero
    const heroBg = document.querySelector('.gallery-hero-bg');
    if (heroBg) {
      lenis.on('scroll', (e) => {
        heroBg.style.transform = `translateY(${e.scroll * 0.3}px)`;
      });
    }
  }

  // --- Gallery Page: Scroll Reveals ---
  const revealElements = document.querySelectorAll('.reveal-up, .fade-in');
  if (revealElements.length > 0) {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { root: null, rootMargin: '0px 0px -100px 0px', threshold: 0.1 });
    
    revealElements.forEach(el => revealObserver.observe(el));
  }

  // --- Gallery Page: Lightbox ---
  const lightbox = document.getElementById('gallery-lightbox');
  const lightboxContent = document.getElementById('lightbox-content');
  const lightboxTitle = document.getElementById('lightbox-title');
  const lightboxCategory = document.getElementById('lightbox-category');
  const lightboxClose = document.getElementById('lightbox-close');
  const lightboxPrev = document.getElementById('lightbox-prev');
  const lightboxNext = document.getElementById('lightbox-next');
  
  if (lightbox) {
    let currentImageIndex = 0;
    const visibleItems = () => Array.from(galleryItems);

    const openLightbox = (index) => {
      const items = visibleItems();
      if (items.length === 0) return;
      currentImageIndex = index;
      
      const item = items[currentImageIndex];
      const imgContainer = item.querySelector('.gallery-img');
      
      
      if(lightboxTitle) lightboxTitle.textContent = '';
      
      
      // Clone image block
      lightboxContent.innerHTML = '';
      const clone = imgContainer.cloneNode(true);
      clone.className = 'lightbox-img';
      clone.style.width = '100%';
      clone.style.height = '100%';
      clone.style.objectFit = 'contain';
      lightboxContent.appendChild(clone);
      
      lightbox.showModal();
      document.body.style.overflow = 'hidden';
      if (typeof lenis !== 'undefined') lenis.stop();
    };

    const closeLightbox = () => {
      lightbox.close();
      document.body.style.overflow = '';
      if (typeof lenis !== 'undefined') lenis.start();
    };

    galleryItems.forEach((item, index) => {
      item.addEventListener('click', () => {
        const items = visibleItems();
        const activeIndex = items.indexOf(item);
        if (activeIndex !== -1) openLightbox(activeIndex);
      });
    });

    if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
    
    lightbox.addEventListener('click', (e) => {
      if (e.target === lightbox) closeLightbox();
    });

    const navigate = (direction) => {
      const items = visibleItems();
      currentImageIndex = (currentImageIndex + direction + items.length) % items.length;
      openLightbox(currentImageIndex);
    };

    if (lightboxPrev) lightboxPrev.addEventListener('click', () => navigate(-1));
    if (lightboxNext) lightboxNext.addEventListener('click', () => navigate(1));

    document.addEventListener('keydown', (e) => {
      if (!lightbox.open) return;
      if (e.key === 'ArrowLeft') navigate(-1);
      if (e.key === 'ArrowRight') navigate(1);
    });
  }

  
});
