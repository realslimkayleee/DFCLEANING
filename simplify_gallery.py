import os
import re
import math

# 1. Gather all images recursively
services_dir = 'assets/services'
all_images = []

for root, dirs, files in os.walk(services_dir):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.svg', '.gif')):
            # Normalize path for HTML
            rel_path = os.path.relpath(os.path.join(root, file), start='.')
            rel_path = rel_path.replace('\\', '/')
            all_images.append({'path': rel_path, 'name': file})

# Sort alphabetically by filename
all_images.sort(key=lambda x: x['name'])
print(f"Total images found: {len(all_images)}")

# 2. Generate Grid HTML
grid_html = ""
for idx, img in enumerate(all_images):
    # Create masonry sizing predictably
    span_class = ""
    if idx % 7 == 0:
        span_class = " span-large"
    elif idx % 5 == 0:
        span_class = " span-tall"

    alt_text = f"DF Cleaning work sample {idx+1}"
    
    item_html = f'''
        <div class="gallery-item{span_class} reveal-up" tabindex="0" role="button" aria-label="View Fullscreen Image">
          <div class="gallery-img-container">
            <img class="gallery-img" src="{img['path']}" alt="{alt_text}" loading="lazy">
          </div>
          <div class="gallery-item-overlay">
            <div class="gallery-overlay-title">Work Sample</div>
          </div>
        </div>'''
    grid_html += item_html

# 3. Update gallery.html
with open('gallery.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the filter bar and the grid
# Find the start of filter bar and end of before-after wrapper
filter_start = html.find('<div class="gallery-filter-bar')
ba_end = html.find('</div>\n      \n      <!-- CLOSING CTA -->')
if ba_end == -1:
    ba_end = html.find('<!-- CLOSING CTA -->')

if filter_start != -1 and ba_end != -1:
    replacement = f'''<!-- GALLERY GRID -->
      <div class="gallery-grid" id="gallery-grid">
{grid_html}
      </div>
      
      '''
    html = html[:filter_start] + replacement + html[ba_end:]

# Update lightbox html to remove category
lb_category_start = html.find('<p id="lightbox-category">')
lb_category_end = html.find('</p>', lb_category_start) + 4
if lb_category_start != -1:
    html = html[:lb_category_start] + html[lb_category_end:]

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 4. Update js/main.js
with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Remove FLIP Logic
# We can just use regex or find to remove from "// --- Gallery Page: Filter & FLIP Animation ---"
# to "// --- Gallery Page: Lightbox ---"
flip_start = js.find('// --- Gallery Page: Filter & FLIP Animation ---')
lb_start = js.find('// --- Gallery Page: Lightbox ---')

if flip_start != -1 and lb_start != -1:
    js = js[:flip_start] + js[lb_start:]

# Remove Before/After Logic
ba_start = js.find('// --- Gallery Page: Before/After Slider ---')
ba_end = js.find('});', ba_start)

if ba_start != -1 and ba_end != -1:
    # Just remove to the end of the file except the very last '});'
    js = js[:ba_start]

# Update Lightbox Logic to not look for category
# Also change 'const visibleItems = ...' since everything is always visible now
js = js.replace("const visibleItems = () => Array.from(galleryItems).filter(item => !item.classList.contains('is-hidden'));", "const visibleItems = () => Array.from(galleryItems);")
js = js.replace("const category = item.querySelector('.gallery-overlay-category').textContent;", "")
js = js.replace("lightboxCategory.textContent = category;", "")
js = js.replace("const category = item.querySelector('.gallery-overlay-category')?.textContent || '';", "")
js = js.replace("if(lightboxCategory) lightboxCategory.textContent = category;", "")


with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js + "\n});\n")

print("Files successfully updated.")
