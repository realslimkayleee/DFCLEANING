import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace gallery grid
css = re.sub(
    r'\.gallery-grid\s*\{[^\}]*\}',
    '''.gallery-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 1.5rem;
    margin-block-end: 6rem;
    position: relative;
  }''',
    css
)

# Replace gallery item
css = re.sub(
    r'\.gallery-item\s*\{[^\}]*\}',
    '''.gallery-item {
    position: relative;
    border-radius: 16px;
    overflow: hidden;
    cursor: pointer;
    background-color: var(--color-gray-light);
    flex: 1 1 300px;
    height: 350px;
  }''',
    css
)

# Replace span-large
css = re.sub(
    r'\.gallery-item\.span-large\s*\{[^\}]*\}',
    '''.gallery-item.span-large {
    flex: 2 1 600px;
  }''',
    css
)

# Replace span-tall
css = re.sub(
    r'\.gallery-item\.span-tall\s*\{[^\}]*\}',
    '''.gallery-item.span-tall {
    flex: 1 1 300px;
  }''',
    css
)

# Strip out the media queries for spans
css = re.sub(
    r'@media \(max-width: 1024px\) \{\s*\.gallery-item,\s*\.gallery-item\.span-large,\s*\.gallery-item\.span-tall\s*\{[^\}]*\}\s*\}',
    '',
    css
)

css = re.sub(
    r'@media \(max-width: 640px\) \{\s*\.gallery-item,\s*\.gallery-item\.span-large,\s*\.gallery-item\.span-tall\s*\{[^\}]*\}\s*\}',
    '',
    css
)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Gallery grid updated to flexbox.")
