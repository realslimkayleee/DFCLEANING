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
});
