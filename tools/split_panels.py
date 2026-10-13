"""Rebuild the panel images after editing the brochure in PowerPoint.

1. In PowerPoint: File > Export > PNG, "All slides" (slide 1 = outside, slide 2 = inside).
2. Run:  python tools/split_panels.py Slide1.PNG Slide2.PNG b1
   (use b2 for the second brochure). Needs: pip install pillow
"""
import sys
from PIL import Image
outside, inside, bid = sys.argv[1], sys.argv[2], sys.argv[3]
for path, names in [(outside, ["A", "B", "C"]), (inside, ["p1", "p2", "p3"])]:
    im = Image.open(path).convert("RGB")
    if im.width < 3000:  # upscale small exports so text stays sharp on phones
        im = im.resize((3507, round(3507 * im.height / im.width)), Image.LANCZOS)
    W, H = im.size
    for k, n in enumerate(names):
        im.crop((round(W * k / 3), 0, round(W * (k + 1) / 3), H)).save(f"assets/{bid}/{n}.webp", quality=88, method=6)
print("Panels updated in assets/" + bid)
