import re

# 1. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix 1: Transparency on top, subtle opacity on scroll
css = css.replace(
    'background: linear-gradient(to bottom, rgba(255,255,255,0.95) 0%, rgba(255,255,255,0.5) 60%, transparent 100%);',
    'background: transparent;'
)
css = css.replace(
    'background-color: rgba(255, 255, 255, 0.85);\n  backdrop-filter: blur(16px);\n  -webkit-backdrop-filter: blur(16px);',
    'background-color: rgba(255, 255, 255, 0.25);\n  backdrop-filter: blur(8px);\n  -webkit-backdrop-filter: blur(8px);'
)

# Fix 3: Hide mobile accordion toggle on desktop
hide_css = """
@media (min-width: 1025px) {
  .mobile-accordion-toggle {
    display: none !important;
  }
}
"""
if 'min-width: 1025px' not in css:
    css += hide_css

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update js/header.js (Remove spacer for identical layout)
with open('js/header.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Fix 2: Remove the 90px spacer
js = js.replace('<!-- Spacer to prevent content from hiding behind fixed header -->\n    <div style="height: 90px;"></div>\n    \n    <header class="site-header-fixed">', '<header class="site-header-fixed">')

with open('js/header.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Nav fixes applied successfully.")
