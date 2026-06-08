import re

with open('gallery.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove inline <style> block
html = re.sub(r'<style>.*?</style>', '', html, flags=re.DOTALL)

# 2. Add Lenis to <head>
lenis_script = '\n  <script src="https://unpkg.com/@studio-freight/lenis@1.0.42/dist/lenis.min.js"></script>'
html = html.replace('</head>', lenis_script + '\n</head>')

# 3. Replace <main> block
main_content = """  <main id="smooth-wrapper">
    <!-- NEW HERO SECTION -->
    <section class="gallery-hero reveal-up">
      <img src="assets/gallery-hero-bg.jpg" alt="" class="gallery-hero-bg" aria-hidden="true" loading="lazy">
      <div class="gallery-hero-content">
        <h1 class="gallery-hero-title">Our Work, Up Close</h1>
        <p class="gallery-hero-subtitle">See the difference professional cleaning makes across residential and commercial spaces.</p>
      </div>
      <div class="scroll-down-cue" aria-hidden="true">
        <span style="font-size: 0.85rem; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.5rem;">Scroll</span>
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"></line><polyline points="19 12 12 19 5 12"></polyline></svg>
      </div>
    </section>

    <!-- FILTER BAR -->
    <section class="container section-padding">
      <div class="gallery-filter-bar reveal-up">
        <button class="filter-btn active" data-filter="all">All</button>
        <button class="filter-btn" data-filter="home-cleaning">Home Cleaning</button>
        <button class="filter-btn" data-filter="on-going-cleaning">On-Going Cleaning</button>
        <button class="filter-btn" data-filter="commercial-cleaning">Commercial / Industrial</button>
        <button class="filter-btn" data-filter="move-in-move-out">Move-In / Move-Out</button>
        <button class="filter-btn" data-filter="window-washing">Window Washing</button>
        <button class="filter-btn" data-filter="carpet-cleaning">Carpet Cleaning</button>
      </div>

      <!-- GALLERY GRID -->
      <div class="gallery-grid" id="gallery-grid">
        <!-- Home Cleaning -->
        <div class="gallery-item span-large reveal-up" data-category="home-cleaning" tabindex="0" role="button" aria-label="View Kitchen Deep Clean">
          <div class="gallery-img-container">
            <!-- [Image Slot: Home Cleaning Kitchen] -->
            <div class="gallery-img" style="width: 100%; height: 100%; background: #e2e8f0; display: grid; place-items: center; color: #64748b; font-weight: bold;">[Image Slot: Home Cleaning Kitchen]</div>
          </div>
          <div class="gallery-item-overlay">
            <div class="gallery-overlay-title">Kitchen Deep Clean</div>
            <div class="gallery-overlay-category">Home Cleaning</div>
          </div>
        </div>

        <!-- Commercial Cleaning -->
        <div class="gallery-item span-tall reveal-up" data-category="commercial-cleaning" tabindex="0" role="button" aria-label="View Corporate Office Lobby">
          <div class="gallery-img-container">
            <!-- [Image Slot: Commercial Lobby] -->
            <div class="gallery-img" style="width: 100%; height: 100%; background: #e2e8f0; display: grid; place-items: center; color: #64748b; font-weight: bold;">[Image Slot: Commercial Lobby]</div>
          </div>
          <div class="gallery-item-overlay">
            <div class="gallery-overlay-title">Corporate Office Lobby</div>
            <div class="gallery-overlay-category">Commercial / Industrial</div>
          </div>
        </div>

        <!-- Window Washing -->
        <div class="gallery-item reveal-up" data-category="window-washing" tabindex="0" role="button" aria-label="View Streak-Free Windows">
          <div class="gallery-img-container">
            <!-- [Image Slot: Window Washing] -->
            <div class="gallery-img" style="width: 100%; height: 100%; background: #e2e8f0; display: grid; place-items: center; color: #64748b; font-weight: bold;">[Image Slot: Window Washing]</div>
          </div>
          <div class="gallery-item-overlay">
            <div class="gallery-overlay-title">Streak-Free Windows</div>
            <div class="gallery-overlay-category">Window Washing</div>
          </div>
        </div>
        
        <!-- Carpet Cleaning -->
        <div class="gallery-item reveal-up" data-category="carpet-cleaning" tabindex="0" role="button" aria-label="View Carpet Stain Removal">
          <div class="gallery-img-container">
            <!-- [Image Slot: Carpet Cleaning] -->
            <div class="gallery-img" style="width: 100%; height: 100%; background: #e2e8f0; display: grid; place-items: center; color: #64748b; font-weight: bold;">[Image Slot: Carpet Cleaning]</div>
          </div>
          <div class="gallery-item-overlay">
            <div class="gallery-overlay-title">Carpet Stain Removal</div>
            <div class="gallery-overlay-category">Carpet Cleaning</div>
          </div>
        </div>

        <!-- Move-In / Move-Out -->
        <div class="gallery-item span-large reveal-up" data-category="move-in-move-out" tabindex="0" role="button" aria-label="View Empty Apartment Prep">
          <div class="gallery-img-container">
            <!-- [Image Slot: Move In/Out] -->
            <div class="gallery-img" style="width: 100%; height: 100%; background: #e2e8f0; display: grid; place-items: center; color: #64748b; font-weight: bold;">[Image Slot: Move-In/Move-Out]</div>
          </div>
          <div class="gallery-item-overlay">
            <div class="gallery-overlay-title">Empty Apartment Prep</div>
            <div class="gallery-overlay-category">Move-In / Move-Out</div>
          </div>
        </div>

        <!-- On-Going Cleaning -->
        <div class="gallery-item reveal-up" data-category="on-going-cleaning" tabindex="0" role="button" aria-label="View Weekly Living Room Clean">
          <div class="gallery-img-container">
            <!-- [Image Slot: On-Going Cleaning] -->
            <div class="gallery-img" style="width: 100%; height: 100%; background: #e2e8f0; display: grid; place-items: center; color: #64748b; font-weight: bold;">[Image Slot: On-Going Cleaning]</div>
          </div>
          <div class="gallery-item-overlay">
            <div class="gallery-overlay-title">Weekly Living Room Clean</div>
            <div class="gallery-overlay-category">On-Going Cleaning</div>
          </div>
        </div>

      </div>

      <!-- BEFORE & AFTER SLIDER -->
      <div class="before-after-wrapper reveal-up">
        <div class="before-after-header">
          <h2 style="font-size: 2.5rem; color: var(--color-navy-dark); margin-bottom: 0.5rem; font-weight: 800;">See the Difference</h2>
          <p style="color: var(--color-gray-dark);">Interactive Before & After</p>
        </div>
        <div class="ba-slider" id="ba-slider-1" role="slider" aria-valuemin="0" aria-valuemax="100" aria-valuenow="50" tabindex="0">
          <!-- [Image Slot: After (Clean)] -->
          <div class="ba-image ba-after" style="background: #cbd5e1; display:grid; place-items:center; color:#475569; font-weight: bold;">[Image Slot: After (Clean)]</div>
          <!-- [Image Slot: Before (Dirty)] -->
          <div class="ba-image ba-before" style="background: #94a3b8; display:grid; place-items:center; color:#1e293b; font-weight: bold;">[Image Slot: Before (Dirty)]</div>
          
          <div class="ba-handle"></div>
          <div class="ba-label ba-label-before">Before</div>
          <div class="ba-label ba-label-after">After</div>
        </div>
      </div>
      
      <!-- CLOSING CTA -->
      <div class="cta-band reveal-up" style="background-color: var(--color-blue-light); padding: 4rem 2rem; border-radius: 16px; text-align: center; margin-block-end: 2rem;">
        <h2 style="font-size: 2rem; color: var(--color-navy-dark); margin-bottom: 1rem; font-weight: 800;">Ready for a spotless space?</h2>
        <p style="margin-bottom: 2rem; color: var(--color-text-main);">Contact us today for a free estimate or call us directly.</p>
        <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
          <a href="estimate.html" class="btn btn-primary">Get a Quote</a>
          <a href="tel:7373679177" class="btn btn-outline">(737) 367-9177</a>
        </div>
      </div>

    </section>
  </main>

  <!-- LIGHTBOX DIALOG -->
  <dialog id="gallery-lightbox" class="lightbox-dialog" aria-modal="true" aria-label="Image Lightbox">
    <div class="lightbox-container">
      <div class="lightbox-header">
        <div class="lightbox-info">
          <h3 id="lightbox-title">Title</h3>
          <p id="lightbox-category">Category</p>
        </div>
        <button class="lightbox-close-btn" id="lightbox-close" aria-label="Close Lightbox">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
        </button>
      </div>
      <div class="lightbox-content" id="lightbox-content">
        <!-- Image injected via JS -->
      </div>
      <button class="lightbox-nav-btn lightbox-prev" id="lightbox-prev" aria-label="Previous Image">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
      </button>
      <button class="lightbox-nav-btn lightbox-next" id="lightbox-next" aria-label="Next Image">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
      </button>
    </div>
  </dialog>
"""

# Replace the existing main tag content
html = re.sub(r'<main>.*?</main>', main_content, html, flags=re.DOTALL)

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(html)
