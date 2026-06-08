import re

with open('services.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The structure is:
#           <div class="service-icon-box" aria-hidden="true">
#             <svg ...></svg>
#           </div>
# 
# We can use regex to remove it.

new_html = re.sub(
    r'\s*<div class="service-icon-box"[^>]*>.*?</div>',
    '',
    html,
    flags=re.DOTALL
)

with open('services.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Icons removed from service cards.")
