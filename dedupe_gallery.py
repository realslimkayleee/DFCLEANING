import os
import hashlib

def hash_file(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()

services_dir = 'assets/services'
all_images = []

# Gather all images
for root, dirs, files in os.walk(services_dir):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.svg', '.gif')):
            rel_path = os.path.relpath(os.path.join(root, file), start='.')
            rel_path = rel_path.replace('\\', '/')
            all_images.append({'path': rel_path, 'name': file, 'full_path': os.path.join(root, file)})

# Sort alphabetically to keep stable ordering before deduplication
all_images.sort(key=lambda x: x['name'])
total_before = len(all_images)

seen_hashes = set()
unique_images = []

for img in all_images:
    file_hash = hash_file(img['full_path'])
    if file_hash not in seen_hashes:
        seen_hashes.add(file_hash)
        unique_images.append(img)

duplicates_removed = total_before - len(unique_images)
total_after = len(unique_images)

print(f"Total before: {total_before}")
print(f"Duplicates removed: {duplicates_removed}")
print(f"Unique images remain: {total_after}")

# Generate Grid HTML
grid_html = ""
for idx, img in enumerate(unique_images):
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
        </div>'''
    grid_html += item_html

# Update gallery.html
with open('gallery.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the start and end of gallery-grid
grid_start = html.find('<div class="gallery-grid" id="gallery-grid">')
if grid_start != -1:
    grid_end = html.find('</div>\n      \n      <!-- CLOSING CTA -->', grid_start)
    if grid_end == -1:
        grid_end = html.find('<!-- CLOSING CTA -->', grid_start)
        
    # extract everything after the last </div> of the grid, which should be right before CLOSING CTA
    # actually, just find the closing </div> of gallery-grid.
    # It's safer to find the CTA marker
    if grid_end != -1:
        # replace
        replacement = f'''<div class="gallery-grid" id="gallery-grid">
{grid_html}
      </div>
      
      '''
        # we need to make sure we don't duplicate `<!-- CLOSING CTA -->`
        # grid_end points to `</div>\n      \n      <!-- CLOSING CTA -->` or `<!-- CLOSING CTA -->`
        
        # Let's cleanly replace using regex or exact block replacement
        pass

# Let's use regex for safety:
import re
new_html = re.sub(
    r'<div class="gallery-grid" id="gallery-grid">.*?(?=<!-- CLOSING CTA -->)',
    f'<div class="gallery-grid" id="gallery-grid">\n{grid_html}\n      </div>\n      \n      ',
    html,
    flags=re.DOTALL
)

with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("gallery.html updated successfully.")
