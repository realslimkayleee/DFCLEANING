import re

# 1. Update css/style.css
css_addition = """
/* CTA Card Specifics */
.service-card.cta-card {
  background: var(--color-navy-dark);
  color: var(--color-white);
  justify-content: center;
  align-items: center;
  text-align: center;
  border: none;
  cursor: default; /* Doesn't expand */
}
.service-card.cta-card:hover {
  transform: translateY(-5px); /* Keep hover lift */
  box-shadow: var(--shadow-md);
}
.service-card.cta-card h2 {
  color: var(--color-white);
  font-size: 1.8rem;
  margin-bottom: 1rem;
}
.service-card.cta-card p {
  color: rgba(255, 255, 255, 0.85);
  margin-bottom: 2rem;
}
.service-card.cta-card .btn {
  width: 100%;
}
"""

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace grid-template-columns with flexbox rules
css = css.replace(
"""  .services-card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 2rem;
    margin-block-start: 3rem;
  }""",
"""  .services-card-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 2rem;
    margin-block-start: 3rem;
  }
  .services-card-grid > * {
    flex: 1 1 320px;
    max-width: calc(33.3333% - 1.34rem);
  }
  @media (max-width: 1024px) {
    .services-card-grid > * {
      max-width: calc(50% - 1rem);
    }
  }
  @media (max-width: 768px) {
    .services-card-grid > * {
      max-width: 100%;
    }
  }"""
)

if 'cta-card' not in css:
    css += css_addition

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)


# 2. Update services.html
cta_html = """
        <!-- 8. CTA Card -->
        <div class="service-card cta-card">
          <h2>Not sure which service you need?</h2>
          <p>Tell us about your space and we'll put together a free custom quote.</p>
          <a href="estimate.html" class="btn btn-primary">Get a Quote</a>
          <p style="margin-top: 1rem; margin-bottom: 0; font-size: 0.9rem;">Or call us: <a href="tel:+17373679177" style="color: var(--color-yellow); font-weight: 600;">(737) 367-9177</a></p>
        </div>
"""
with open('services.html', 'r', encoding='utf-8') as f:
    html = f.read()

# find closing div of services-card-grid
if '<!-- 8. CTA Card -->' not in html:
    # Insert before the last </div> of .services-card-grid
    # Search for the final </div> that is followed by </section>
    
    html = html.replace('        </div>\n\n      </div>\n    </section>', f'        </div>\n{cta_html}\n      </div>\n    </section>')
    
with open('services.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("CTA Card and flexbox auto-centering added successfully.")
