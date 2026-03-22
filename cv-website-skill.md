# SKILL.md — CV Website: Gauresh Naik
## For Claude Code | Complete Build Instructions

---

## PROJECT OVERVIEW

Build a personal CV/portfolio website for **Gauresh Naik**, a Marketing & Sales professional based in Kuwait. This is a hosted static website (HTML + CSS + JS, no frameworks required) that will live on GitHub Pages at:

**Repo:** `gaur61201/gauresh-naik-cv` (or similar)
**Live URL:** `https://gaur61201.github.io/gauresh-naik-cv/`

The site must function as both a CV and a portfolio — professional enough to pass recruiter screening, impressive enough to make a hiring manager remember him.

---

## AESTHETIC DIRECTION

### Vibe
**Dark Techy meets Corporate Modern.** Think: a senior product of a tech startup that also wears suits to client meetings. Not a developer portfolio. Not a boring CV. Something in between — with edge.

### Visual Identity
- **Background:** Near-black `#080C10` — deep, not flat black
- **Primary Accent:** Electric Teal `#00E5CC` — modern, techy, memorable
- **Secondary Accent:** Warm Amber `#F5A623` — used sparingly for highlights, tags, "currently learning"
- **Surface Cards:** `#0F1923` with subtle border `rgba(0,229,204,0.1)`
- **Text Primary:** `#F0F4F8`
- **Text Secondary:** `#7A8FA6`
- **Gradient Accent:** `linear-gradient(135deg, #00E5CC, #0066FF)`

### Typography
- **Display / Hero Font:** `Syne` (Google Fonts) — geometric, bold, modern
- **Body Font:** `DM Sans` (Google Fonts) — clean, readable, professional
- **Mono / Tag Font:** `JetBrains Mono` — used for skill tags, labels, code-like elements

### Motion & Effects
- Subtle grain texture overlay on hero (CSS noise)
- Staggered fade-up on page load (CSS animation-delay)
- Horizontal glowing line separator between sections
- Skill cards: hover lifts with teal glow box-shadow
- Scroll-triggered fade-in for sections (IntersectionObserver)
- Cursor: custom dot + ring that follows mouse (CSS + JS)
- Typing animation on hero subtitle
- NO heavy libraries. Vanilla JS + CSS only.

### Layout Philosophy
- Full-width sections, max-width `1100px` container centered
- Generous vertical spacing between sections (`120px`)
- Grid-breaking hero — name displayed large, left-aligned, raw
- Cards with subtle glassmorphism: `backdrop-filter: blur(10px)`
- Mobile-first responsive

---

## FILE STRUCTURE

```
gauresh-naik-cv/
├── index.html
├── style.css
├── script.js
├── assets/
│   ├── images/
│   │   ├── gauresh-photo.jpg       ← placeholder div if no photo
│   │   ├── og-image.jpg            ← social share preview
│   └── icons/                      ← SVG icons if needed
└── README.md
```

All code in 3 files: `index.html`, `style.css`, `script.js`. No build tools. No npm. Pure static.

---

## SECTIONS — FULL SPECIFICATION

### 1. HEAD & META

```html
<title>Gauresh Naik — Marketing & Sales Professional</title>
<meta name="description" content="Marketing & Sales professional with an operator's mindset. Based in Kuwait.">
<meta property="og:title" content="Gauresh Naik — CV">
<meta property="og:description" content="Revenue, Marketing & Operations — all three, solo.">
```

Import from Google Fonts:
```
Syne:wght@400;600;700;800
DM+Sans:wght@300;400;500;600
JetBrains+Mono:wght@400;500
```

---

### 2. NAVIGATION

**Type:** Fixed top, transparent → frosted glass on scroll
**Left:** `GN` monogram in teal
**Right links:** About · Skills · Experience · Projects · Contact
**Mobile:** Hamburger menu, full-screen overlay nav

```css
nav {
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 100;
  transition: background 0.3s ease;
}
nav.scrolled {
  background: rgba(8,12,16,0.85);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(0,229,204,0.1);
}
```

---

### 3. HERO SECTION

**Layout:** Full viewport height. Left-aligned text block. Right side: photo placeholder (circular, teal glow border) or abstract geometric shape if no photo.

**Content:**

```
[Mono tag]  Based in Kuwait · Open to Opportunities

[Display — very large, Syne 800]
GAURESH
NAIK

[Subtitle — typing animation cycling through:]
"Marketing & Sales Professional"
"Revenue & Operations Lead"
"Systems Builder"
"Content Strategist"

[Body — DM Sans, secondary color]
I generate leads, close deals, build content — and automate
the systems that hold it all together. Hired for one role.
Built three.

[CTA Buttons]
[PRIMARY] View My Work ↓
[SECONDARY] Download CV (links to PDF version if available, else mailto)
```

**Background details:**
- Large faint `GN` lettermark behind the text, opacity 3%, Syne 800
- Subtle animated gradient glow at bottom-left corner
- Grain texture overlay

---

### 4. ABOUT SECTION

**Section label:** `<span class="mono-tag">// 01 — About</span>`

**Heading:** "An operator who markets. A marketer who closes."

**Body copy (3 short paragraphs):**

> I'm a Marketing & Sales professional with a hands-on background in content creation, lead generation, and sales — running all three simultaneously at Waves Printing Press in Kuwait.

> Beyond my job title, I design CRM workflows, build automation pipelines in n8n, and create client-facing websites. I don't just execute campaigns — I build the systems that make execution sustainable.

> Currently based in Kuwait. Fluent in English. Open to full-time roles across Marketing, Sales, Business Development, Social Media, and Operations.

**Right side of about:** 3 stat cards in a small grid:

```
[ 3       ]  [ 1 yr    ]  [ 3       ]
  Functions    Experience   Live Sites
  Managed      Kuwait       Built
```

---

### 5. SKILLS SECTION

**Section label:** `// 02 — Skills`
**Heading:** "What I Actually Know How to Do"

Layout: 3 columns — one per cluster. Each cluster has a header and skill pills.

---

**Cluster 1: Marketing & Content**
Color accent: Teal `#00E5CC`
Icon: 📣 (or SVG megaphone)

Skills as pills (JetBrains Mono, small caps):
`Social Media Strategy` · `Content Creation` · `Video Editing` · `Canva` · `Premiere Pro` · `Meta Ads` · `Instagram` · `TikTok` · `Freepik AI` · `Caption Writing` · `Content Calendars`

---

**Cluster 2: Sales & Revenue**
Color accent: Amber `#F5A623`
Icon: 🎯

Skills:
`Lead Generation` · `Cold Outreach` · `Cold Calling` · `DM Prospecting` · `Sales Proposals` · `Objection Handling` · `Pipeline Management` · `CRM (Airtable)` · `Follow-up Sequences` · `Deal Closing`

---

**Cluster 3: Operations & Systems**
Color accent: Blue `#0066FF`
Icon: ⚙️

Skills:
`n8n Automation` · `Airtable` · `Google Sheets` · `GitHub` · `Workflow Design` · `Claude Code` · `Web Development` · `HTML/CSS/JS` · `GitHub Pages` · `Process Documentation`

---

**Below clusters — "Currently Learning" bar:**

```
[ 🔄 Currently Learning ]
AI Video Production for Ads  ·  Freepik AI Tools  ·  Advanced n8n Workflows
```

Styled with amber accent, dashed border, italic label.

---

### 6. EXPERIENCE SECTION

**Section label:** `// 03 — Experience`
**Heading:** "Where I've Worked"

**Single entry card — full width:**

```
[Top row]
WAVES PRINTING PRESS                          Kuwait · 2024 – Present
Revenue & Operations Lead

[Subtitle line — mono, small, teal]
Hired as: Social Media Manager → Operated across: Marketing · Lead Gen · Sales · Automation

[Body]
Joined to manage Instagram. Ended up building the revenue infrastructure.
Took ownership of content strategy, lead generation, sales pipeline,
and CRM automation — designing systems the company had never had before.

[What I built — 4 bullet-style items in a 2x2 grid card]

◆ Designed full CRM & lead tracking system in Airtable with pipeline stages from New Lead → Closed Won

◆ Built n8n automation workflows for lead capture, follow-up sequencing, and content scheduling

◆ Created bilingual (English + Gulf Arabic) outreach templates for cold DM, email, and cold call campaigns

◆ Developed social media content strategy targeting corporate clients, event planners, and F&B businesses across Kuwait

[Tags at bottom]
#Airtable  #n8n  #LeadGen  #ContentStrategy  #SalesOps  #MetaAds
```

**Card style:** Full-width dark card, left teal border accent (4px), hover glow subtle.

---

### 7. PROJECTS SECTION

**Section label:** `// 04 — Projects`
**Heading:** "Things I've Built"
**Subheading:** "Client demo websites built to production standard — full design, copy, and deployment."

**Layout:** 2-column grid (stacks to 1 on mobile). 3 cards + 1 "Coming Soon" placeholder.

---

**Project Card 1: Healy Gymnastics Academy**

```
[Tag] Sports & Fitness · Kuwait
[Title] Healy Gymnastics Academy
[Description]
Full business website for Kuwait's #1 gymnastics academy. Built with
bilingual copy, program listings, coach profiles, animated gallery,
enrollment form, and WhatsApp CTA integration.

[Tech tags]  HTML · CSS · JS · GitHub Pages · Bilingual (EN/AR)

[Links]
[→ Live Site]  https://gaur61201.github.io/healy-gymnastics/
[→ GitHub]     https://github.com/gaur61201/healy-gymnastics
```

---

**Project Card 2: Hair Lounge Kuwait**

```
[Tag] Beauty & Wellness · Kuwait
[Title] Hair Lounge Kuwait
[Description]
Premium women's salon website with full service menu, video gallery,
Google Reviews integration, FAQ accordion, and multi-step booking
flow via WhatsApp. Clean luxury aesthetic.

[Tech tags]  HTML · CSS · JS · GitHub Pages · WhatsApp Integration

[Links]
[→ Live Site]  https://gaur61201.github.io/hairlounge-kuwait/
[→ GitHub]     https://github.com/gaur61201/hairlounge-kuwait
```

---

**Project Card 3: Waves Printing Press — Internal Automation**

```
[Tag] Operations & Automation · Internal Project
[Title] Lead & CRM Automation System
[Description]
Built and tested an end-to-end lead management system for a Kuwait
printing company. Includes Airtable CRM with pipeline stages, n8n
workflows for lead capture and follow-up sequencing, and a Google
Sheets reporting layer. Designed for solo operation.

[Tech tags]  n8n · Airtable · Google Sheets · Workflow Automation

[Status badge — amber]  Built & Tested · Internal

[No live link — badge reads: "Internal Project"]
```

---

**Project Card 4: [3rd Website — Coming Soon]**

```
[Tag] TBA · Industry TBA
[Title] New Client Demo Site
[Description]
Third portfolio website currently in progress. Different industry,
different aesthetic. Will be live shortly.

[Status badge — dashed border]  Coming Soon
```

---

### 8. CURRENTLY LEARNING SECTION

**Section label:** `// 05 — In Progress`
**Heading:** "What I'm Building Next"

3 horizontal cards:

```
[Card 1]
🎬 AI Video for Ads
Learning AI-generated video tools to produce
scroll-stopping ad creatives. Applying to social
media campaigns and paid advertising workflows.
Status: Active Learning

[Card 2]
🤖 Advanced n8n Workflows
Expanding automation skills — multi-step
pipelines, webhook triggers, API integrations,
and conditional logic for lead workflows.
Status: Active Learning

[Card 3]
🎨 Freepik AI Tools
Exploring AI design generation for fast content
creation — social assets, ad visuals, branded
graphics without heavy Photoshop dependency.
Status: Active Learning
```

Style: Dashed border cards, amber accent, slightly muted vs main sections — signals honesty and growth.

---

### 9. CONTACT SECTION

**Section label:** `// 06 — Contact`
**Heading:** "Let's Talk"
**Subheading:** "Open to full-time roles in Kuwait and remotely. Response within 24 hours."

**Layout:** Left side — copy + contact details. Right side — simple contact form (HTML form, no backend, uses `mailto:` action or Formspree).

**Contact details:**

```
📧  naikg8033@gmail.com
📱  +965 976 94436  (WhatsApp preferred)
📍  Kuwait · Open to relocation
```

**Social/link row:**
```
[GitHub]   github.com/gaur61201
[Email]    naikg8033@gmail.com
[WhatsApp] wa.me/96597694436
```

**Form fields:** Name · Email · Message · [Send Message] button

**Form button style:** Teal gradient, hover shifts to blue, subtle pulse animation on idle.

---

### 10. FOOTER

```
Gauresh Naik · Built by hand · Hosted on GitHub Pages
© 2025 · naikg8033@gmail.com

[Back to top ↑]
```

Minimal. Single line. No clutter.

---

## INTERACTION & ANIMATION SPEC

### Page Load Sequence (staggered, CSS animation-delay)
```
0ms   → Nav fades in
200ms → Hero mono tag slides up
400ms → Hero name slides up + fade
600ms → Hero subtitle starts typing animation
800ms → Hero body text fades in
1000ms → CTA buttons fade in
```

### Scroll Animations (IntersectionObserver)
- Each section fades up when 20% in viewport
- Skill pills animate in with staggered delay (30ms each)
- Project cards scale from 0.96 → 1.0 on entry

### Typing Animation (JS)
Cycle through hero subtitles with cursor blink:
```js
const titles = [
  "Marketing & Sales Professional",
  "Revenue & Operations Lead",
  "Systems Builder & Automator",
  "Content Strategist"
];
// Type forward → pause → delete → type next
```

### Custom Cursor
```js
// Small teal dot (8px) + larger ring (32px) that follows with slight lag
// Ring scales up on hover over links/buttons
// Hides on mobile (touch devices)
```

### Skill Pills Hover
```css
.skill-pill:hover {
  background: rgba(0, 229, 204, 0.15);
  border-color: #00E5CC;
  transform: translateY(-2px);
  box-shadow: 0 4px 20px rgba(0, 229, 204, 0.2);
}
```

---

## RESPONSIVE BREAKPOINTS

```css
/* Mobile first */
/* Base: 320px+ */
/* Tablet: 768px+ — 2 col grids activate */
/* Desktop: 1024px+ — full 3 col layout */
/* Wide: 1280px+ — max-width container caps */
```

Mobile rules:
- Nav collapses to hamburger
- Hero name size reduces (clamp)
- Skills: 1 column
- Projects: 1 column
- Custom cursor disabled
- Grain overlay reduced opacity

---

## PHOTO PLACEHOLDER

Until a real photo is provided, render this in the hero:

```html
<div class="hero-photo-placeholder">
  <div class="initials">GN</div>
</div>
```

```css
.hero-photo-placeholder {
  width: 280px;
  height: 280px;
  border-radius: 50%;
  border: 2px solid rgba(0, 229, 204, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 60px rgba(0, 229, 204, 0.15);
  background: rgba(0, 229, 204, 0.05);
}
.initials {
  font-family: 'Syne', sans-serif;
  font-size: 72px;
  font-weight: 800;
  color: #00E5CC;
}
```

When photo is ready: replace with `<img src="assets/images/gauresh-photo.jpg" alt="Gauresh Naik">` using same border/shadow styles.

---

## CSS VARIABLES (define in :root)

```css
:root {
  --bg-primary: #080C10;
  --bg-surface: #0F1923;
  --bg-card: #111C28;
  --accent-teal: #00E5CC;
  --accent-amber: #F5A623;
  --accent-blue: #0066FF;
  --gradient-accent: linear-gradient(135deg, #00E5CC, #0066FF);
  --text-primary: #F0F4F8;
  --text-secondary: #7A8FA6;
  --text-muted: #3D5166;
  --border-subtle: rgba(0, 229, 204, 0.1);
  --border-card: rgba(255, 255, 255, 0.05);
  --font-display: 'Syne', sans-serif;
  --font-body: 'DM Sans', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --radius-card: 12px;
  --radius-pill: 100px;
  --shadow-card: 0 4px 24px rgba(0, 0, 0, 0.4);
  --shadow-glow: 0 0 40px rgba(0, 229, 204, 0.12);
}
```

---

## REUSABLE COMPONENT PATTERNS

### Section Header
```html
<div class="section-header">
  <span class="mono-tag">// 01 — About</span>
  <h2 class="section-title">Heading Here</h2>
  <div class="section-line"></div>
</div>
```

```css
.mono-tag {
  font-family: var(--font-mono);
  font-size: 12px;
  color: var(--accent-teal);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 8px;
  display: block;
}
.section-title {
  font-family: var(--font-display);
  font-size: clamp(28px, 4vw, 48px);
  font-weight: 700;
  color: var(--text-primary);
}
.section-line {
  width: 48px;
  height: 2px;
  background: var(--gradient-accent);
  margin-top: 16px;
}
```

### Skill Pill
```html
<span class="skill-pill">n8n Automation</span>
```

```css
.skill-pill {
  display: inline-block;
  font-family: var(--font-mono);
  font-size: 11px;
  padding: 6px 14px;
  border: 1px solid var(--border-subtle);
  border-radius: var(--radius-pill);
  color: var(--text-secondary);
  background: rgba(0, 229, 204, 0.04);
  margin: 4px;
  cursor: default;
  transition: all 0.2s ease;
}
```

### Project Card
```html
<div class="project-card">
  <div class="project-tag">Industry · Location</div>
  <h3 class="project-title">Project Name</h3>
  <p class="project-desc">Description here.</p>
  <div class="project-tech">
    <span class="tech-tag">HTML</span>
  </div>
  <div class="project-links">
    <a href="#" class="link-btn primary">→ Live Site</a>
    <a href="#" class="link-btn secondary">→ GitHub</a>
  </div>
</div>
```

---

## IMPORTANT NOTES FOR CLAUDE CODE

1. **No frameworks.** Pure HTML, CSS, JS. Must work on GitHub Pages without any build step.
2. **Single page.** All sections in one `index.html`. Smooth scroll between sections.
3. **Performance.** No heavy libraries. Animate with CSS where possible, JS only for typing effect, cursor, and IntersectionObserver.
4. **Photo placeholder first.** Build with the `GN` initials placeholder. Add a comment `<!-- REPLACE: add gauresh-photo.jpg to assets/images/ -->` in the HTML.
5. **Form action.** Use `https://formspree.io/f/REPLACE_WITH_ID` as form action placeholder — add a comment to replace with real Formspree ID or change to `mailto:naikg8033@gmail.com`.
6. **GitHub links.** Use `https://github.com/gaur61201` as base for all GitHub links.
7. **WhatsApp link format.** `https://wa.me/96597694436` (Kuwait code 965 + number 97694436).
8. **Accessibility.** `alt` tags on all images. Semantic HTML (`<main>`, `<section>`, `<nav>`, `<footer>`). Tab-navigable.
9. **README.md.** Create a clean README with: project description, live URL, sections overview, how to update photo, how to update project links.
10. **Grain texture.** Implement as CSS pseudo-element using SVG filter, not an image file:

```css
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,..."); /* SVG noise */
  opacity: 0.03;
  pointer-events: none;
  z-index: 9999;
}
```

---

## DELIVERABLES CHECKLIST

Claude Code must produce:

- [ ] `index.html` — complete single-page CV website
- [ ] `style.css` — full stylesheet with all CSS variables, animations, responsive rules
- [ ] `script.js` — typing animation, custom cursor, scroll observer, nav scroll behavior, mobile menu
- [ ] `README.md` — documentation for how to update the site

All files production-ready. No placeholder `/* TODO */` blocks. No broken links. No console errors.

---

## OWNER DETAILS (for content reference)

```
Name:         Gauresh Naik
Role:         Revenue & Operations Lead (current)
Company:      Waves Printing Press, Kuwait
Email:        naikg8033@gmail.com
Phone/WA:     +965 976 94436
GitHub:       github.com/gaur61201
Location:     Kuwait
Languages:    English
```

---

*This SKILL.md was written to give Claude Code complete context to build this CV website in a single session with minimal back-and-forth. Follow all specifications exactly. When in doubt, make the design choice that looks more impressive.*
