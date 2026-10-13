# AIBizs digital tri-fold brochures

Interactive version of the two printed tri-fold brochures. It opens like the paper brochure (cover, then inside flap, then full inside, then back cover) on PC, tablet and phone.

## Publish on GitHub Pages
1. Create a new repository (for example `brochure`) and upload **everything in this folder**, including the hidden `.nojekyll` file.
2. Repository **Settings → Pages → Build and deployment**: Source = *Deploy from a branch*, Branch = `main`, folder = `/ (root)` → Save.
3. After about a minute your link is `https://<your-github-name>.github.io/brochure/`.

Direct links:
- Both brochures: `.../brochure/`
- Brochure 1 (ConvergeX by AIBizs): `.../brochure/#b1`
- Brochure 2 (AIBizs × Infinity Thoughts): `.../brochure/#b2`

Tip: turn the link into a QR code for your booth stand.

## How it works
- `assets/b1`, `assets/b2`: each brochure panel as a high-resolution image (A, B, C = outside left to right; p1, p2, p3 = inside), so the design is identical on every device.
- Phone numbers, emails, websites and the QR code are tappable.
- The PDF button downloads the full brochure.

## Updating after a PowerPoint change
Export both slides from PowerPoint as PNG, then run `python tools/split_panels.py Slide1.PNG Slide2.PNG b1` (or `b2`) and upload the changed files.
If a phone number, email or website changes, update the links in `index.html` (search for `tel:` / `mailto:`).
