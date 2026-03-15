# Gauresh Naik — CV Website

Personal CV and portfolio website for **Gauresh Naik**, Marketing & Sales Professional based in Kuwait.

**Live URL:** https://gaur61201.github.io/gauresh-naik-cv/

---

## About

Built with pure HTML, CSS, and JavaScript — no frameworks, no build tools.
Hosted on GitHub Pages as a fully static site.

**Design:** Dark tech-modern aesthetic with electric teal accents, Syne display typography,
custom cursor, typing animation, and scroll-triggered reveals.

---

## Sections

| # | Section | Description |
|---|---------|-------------|
| 1 | **Hero** | Name, typing subtitle, CTA buttons, photo placeholder |
| 2 | **About** | Bio + stat cards (Functions / Experience / Sites Built) |
| 3 | **Skills** | Three clusters: Marketing & Content · Sales & Revenue · Operations & Systems |
| 4 | **Experience** | Waves Printing Press role with achievements and tags |
| 5 | **Projects** | Healy Gymnastics · Hair Lounge Kuwait · CRM Automation · Coming Soon |
| 6 | **In Progress** | Currently learning cards (AI Video · n8n · Freepik AI) |
| 7 | **Contact** | Contact details + contact form (Formspree) |

---

## Files

```
gauresh-naik-cv/
├── index.html        ← Single-page HTML
├── style.css         ← All styles, variables, animations, responsive rules
├── script.js         ← Typing animation, cursor, observers, mobile menu
├── assets/
│   ├── images/
│   │   └── gauresh-photo.jpg   ← (add your photo here)
│   └── icons/                  ← (SVG icons if needed)
└── README.md
```

---

## How to Update

### Add Your Photo

1. Add your photo to `assets/images/gauresh-photo.jpg`
2. In `index.html`, find the comment `<!-- REPLACE: add gauresh-photo.jpg -->` and replace the inner div:

```html
<!-- Before: -->
<div class="hero-photo-placeholder">
  <div class="initials">GN</div>
</div>

<!-- After: -->
<div class="hero-photo-placeholder">
  <img src="assets/images/gauresh-photo.jpg" alt="Gauresh Naik">
</div>
```

### Add a CV PDF for Download

1. Place your CV at `assets/gauresh-naik-cv.pdf`
2. In `index.html`, update the Download CV button:

```html
<a href="assets/gauresh-naik-cv.pdf" class="btn btn-secondary" download>Download CV</a>
```

### Connect the Contact Form

1. Create a free account at [formspree.io](https://formspree.io)
2. Create a new form → copy the form ID (looks like `xpwzabcd`)
3. In `index.html`, find the form `action` attribute and replace `REPLACE_WITH_ID`:

```html
action="https://formspree.io/f/YOUR_ACTUAL_ID"
```

### Add a New Project

Copy this block inside `.projects-grid` in `index.html`:

```html
<div class="project-card">
  <div class="project-tag">Industry · Location</div>
  <h3 class="project-title">Project Title</h3>
  <p class="project-desc">Description of the project.</p>
  <div class="project-tech">
    <span class="tech-tag">HTML</span>
    <span class="tech-tag">CSS</span>
  </div>
  <div class="project-links">
    <a href="LIVE_URL" class="link-btn primary" target="_blank">→ Live Site</a>
    <a href="GITHUB_URL" class="link-btn secondary" target="_blank">→ GitHub</a>
  </div>
</div>
```

### Update Contact Details

All contact details are in `index.html` inside `#contact`. Search for `naikg8033@gmail.com`
or `+965` to find and update them.

---

## Tech Stack

- **HTML5** — semantic markup, ARIA labels, accessible
- **CSS3** — custom properties, Grid, Flexbox, keyframe animations
- **Vanilla JS** — IntersectionObserver, typing animation, custom cursor, mobile menu
- **Google Fonts** — Syne · DM Sans · JetBrains Mono
- **GitHub Pages** — static hosting, zero config

---

## Deployment

```bash
git add .
git commit -m "Update content"
git push origin main
```

GitHub Pages will auto-deploy from the `main` branch root within ~1 minute.

---

## Contact

Gauresh Naik · [naikg8033@gmail.com](mailto:naikg8033@gmail.com) · Kuwait
