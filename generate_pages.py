import os
import re

with open('services.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Extract header and footer from services.html
# We want to replace everything inside <main> except the page-header, which we'll update.
main_start = template.find('<main>')
main_end = template.find('</main>') + 7

header_part = template[:main_start + 6]
footer_part = template[main_end:]

# But we need to fix relative paths since these pages will be in `services/` directory.
# Wait, if we use absolute paths or change `href="css/style.css"` to `href="../css/style.css"`
def fix_paths(html):
    html = html.replace('href="css/style.css"', 'href="../css/style.css"')
    html = html.replace('href="js/main.js"', 'href="../js/main.js"')
    html = html.replace('src="js/main.js"', 'src="../js/main.js"')
    html = html.replace('href="index.html"', 'href="../index.html"')
    html = html.replace('href="about.html"', 'href="../about.html"')
    html = html.replace('href="services.html"', 'href="../services.html"')
    html = html.replace('href="gallery.html"', 'href="../gallery.html"')
    html = html.replace('href="estimate.html', 'href="../estimate.html')
    html = html.replace('src="assets/', 'src="../assets/')
    html = html.replace('href="services/', 'href="')
    return html

header_part = fix_paths(header_part)
footer_part = fix_paths(footer_part)

# Read extracted text
with open('services_extracted.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f.readlines()]

services = [
    {"slug": "home-cleaning", "lines": lines[0:17], "est": "residential"},
    {"slug": "on-going-cleaning", "lines": lines[17:34], "est": "ongoing"},
    {"slug": "commercial-cleaning", "lines": lines[34:51], "est": "commercial"},
    {"slug": "move-in-move-out", "lines": lines[51:67], "est": "move-in-out"},
    {"slug": "window-washing", "lines": lines[67:84], "est": "window"},
    {"slug": "carpet-cleaning", "lines": lines[84:101], "est": "carpet"},
    {"slug": "coaching", "lines": lines[101:112], "est": "coaching"},
]

os.makedirs('services', exist_ok=True)

for svc in services:
    s_lines = svc["lines"]
    title = s_lines[0]
    
    # Generate Page Header
    page_header = f'''
    <!-- PAGE HEADER -->
    <section class="page-header">
      <div class="container">
        <h1 class="page-title">{title}</h1>
        <nav class="page-breadcrumbs" aria-label="Breadcrumb">
          <a href="../index.html">Home</a>
          <span class="breadcrumbs-separator">/</span>
          <a href="../services.html">Services</a>
          <span class="breadcrumbs-separator">/</span>
          <span class="breadcrumbs-active">{title}</span>
        </nav>
      </div>
    </section>
'''

    # Generate Content Section
    content_html = f'''
    <section class="container" style="padding-block: 5rem; max-width: 800px;">
      <div style="margin-bottom: 3rem; text-align: center;">
        <span class="section-subtitle">{s_lines[1]}</span>
        <h2 class="section-title">{s_lines[2]}</h2>
      </div>
'''
    
    # Process remaining lines
    # Lines 3,4,5 are often specific contact details which we can skip or format.
    # We know "Serving Austin & Surrounding Areas", "(737) 367-9177", "Get a Quote"
    # Let's skip them because they are in the global footer/header, and just add the content.
    
    idx = 6 # Start after "Get a Quote"
    if s_lines[idx-1] != "Get a Quote" and s_lines[idx-2] != "(737) 367-9177":
        # Adjust if line indices slightly differ (e.g. Move-in cleaning doesn't have "You Can Count on Us" exactly)
        for i, l in enumerate(s_lines):
            if l == "Get a Quote":
                idx = i + 1
                break
    
    content_lines = s_lines[idx:]
    
    for l in content_lines:
        if len(l) < 100 and not l.endswith('.'):
            # Probably a heading
            content_html += f'      <h3 style="margin-top: 2.5rem; margin-bottom: 1rem; color: var(--color-navy-dark);">{l}</h3>\n'
        else:
            # Paragraph
            content_html += f'      <p style="margin-bottom: 1.5rem; color: var(--color-text-main); line-height: 1.8;">{l}</p>\n'
            
    content_html += f'''
      <div style="margin-top: 3rem; text-align: center;">
        <a href="../estimate.html?service={svc["est"]}" class="btn btn-primary">Get a Quote</a>
      </div>
    </section>
'''

    full_page = header_part + page_header + content_html + footer_part
    
    with open(f'services/{svc["slug"]}.html', 'w', encoding='utf-8') as out:
        out.write(full_page)
