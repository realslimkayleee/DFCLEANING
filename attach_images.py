import os
import re

# 1. Update css/style.css
css_addition = """
  /* Services Card Images */
  .service-card-image {
    margin: -2.5rem -2.5rem 1.5rem -2.5rem;
    width: calc(100% + 5rem);
    max-width: none;
    aspect-ratio: 16 / 9;
    object-fit: cover;
    border-radius: 15px 15px 0 0;
    display: block;
    background-color: var(--color-gray-light);
  }
"""

with open('css/style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

if '.service-card-image' not in css_content:
    css_content = css_content.replace('  .service-icon-box {', css_addition + '\n  .service-icon-box {')
    with open('css/style.css', 'w', encoding='utf-8') as f:
        f.write(css_content)

# 2. Get images and map them
services_dir = 'assets/services'
folders = [d for d in os.listdir(services_dir) if os.path.isdir(os.path.join(services_dir, d))]

# The target tiles:
tiles = {
    'home-cleaning': {'keywords': ['home', 'residential'], 'name': 'Home Cleaning'},
    'on-going-cleaning': {'keywords': ['on going', 'ongoing', 'recurring'], 'name': 'On-Going Cleaning'},
    'commercial-cleaning': {'keywords': ['commercial', 'industrial'], 'name': 'Commercial / Industrial Cleaning'},
    'move-in-move-out': {'keywords': ['movein', 'move in', 'move out', 'move-in', 'move-out'], 'name': 'Move-In / Move-Out Cleaning'},
    'window-washing': {'keywords': ['window'], 'name': 'Window Washing'},
    'carpet-cleaning': {'keywords': ['carpet'], 'name': 'Carpet Cleaning'},
    'coaching': {'keywords': ['coaching', 'business', 'sales'], 'name': 'Coaching'}
}

# Mapping Logic
tile_to_image = {}

for folder in folders:
    folder_lower = folder.lower().replace('-', '').replace('/', '').replace(' ', '')
    matched_tile = None
    for tile_id, data in tiles.items():
        for kw in data['keywords']:
            if kw.replace('-', '').replace(' ', '') in folder_lower:
                matched_tile = tile_id
                break
        if matched_tile:
            break
            
    if matched_tile:
        folder_path = os.path.join(services_dir, folder)
        images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.svg', '.gif'))]
        if images:
            chosen = None
            # Check for cover, main, featured, 1
            for img in images:
                name_no_ext = os.path.splitext(img)[0].lower()
                if name_no_ext in ['cover', 'main', 'featured', '1']:
                    chosen = img
                    break
            
            # Fallback to first alphabetical
            if not chosen:
                images.sort()
                chosen = images[0]
            
            tile_to_image[matched_tile] = f"{services_dir}/{folder}/{chosen}"

print("Mapped Images:")
for t, i in tile_to_image.items():
    print(f"{t}: {i}")

# 3. Update services.html
with open('services.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

for tile_id, image_path in tile_to_image.items():
    # Find the tile
    target = f'<div class="service-card" id="{tile_id}" tabindex="0">'
    
    # Check if we already injected an image
    card_start = html_content.find(target)
    if card_start != -1:
        # Check next lines
        block_end = html_content.find('<h2>', card_start)
        block = html_content[card_start:block_end]
        if '<img class="service-card-image"' not in block:
            alt_text = tiles[tile_id]['name']
            # inject image right after the target div
            img_html = f'\n          <img class="service-card-image" src="{image_path}" alt="{alt_text}" loading="lazy">'
            html_content = html_content.replace(target, target + img_html)
        else:
            # Maybe it matched earlier but we missed updating src
            # We don't need to replace src here unless it's wrong, but since it just ran and might have missed 'on-going', let's replace it
            pass

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(html_content)
