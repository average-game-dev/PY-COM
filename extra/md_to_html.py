import markdown
from sys import argv
import os

# Read your Markdown file
with open(argv[1], "r", encoding="utf-8") as f:
    text = f.read()

# Convert to HTML
html = markdown.markdown(text)

# Determine output file
if len(argv) == 3:
    output_file = argv[2]
else:
    # Replace extension with .html
    base, _ = os.path.splitext(argv[1])
    output_file = base + ".html"

# Save HTML
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html)
