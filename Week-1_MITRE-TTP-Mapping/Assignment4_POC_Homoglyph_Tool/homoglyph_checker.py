import re
import homoglyphs as hg

# Initialize homoglyph detector
glyphs = hg.Homoglyphs()

# Read input file
with open("testlinks.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Regex to find links
links = re.findall(r'(https?://[^\s]+|www\.[^\s]+)', text)

print("Links found:")
for link in links:
    print("  ", link)

print("\nSuspicious links:")
for link in links:
    # Normalize link and compare
    ascii_version = glyphs.to_ascii(link)
    if not link.isascii() and ascii_version != link:
        print("  ", link)

