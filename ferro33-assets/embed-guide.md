# Embed-Guide — Ferro 33 hair club

Es gibt noch keine Website. Hier sind die Snippets zum Einfügen. `index.html` in diesem Ordner zeigt alle zusammen als Live-Vorschau (einfach im Browser öffnen).

Pfade gehen davon aus, dass der Ordner `ferro33-assets/` neben deiner `index.html` liegt.

## 1. Design-Tokens (einmal in dein CSS)

```css
:root {
  --ferro-black:#0B0C0E; --ferro-graphite:#1A1D22; --ferro-white:#F4F5F7;
  --ferro-chrome:#8E959E; --ferro-neon:#1EB8F5;   --ferro-led:#1F5BFF;
  --font-display:"Michroma", sans-serif; --font-body:"Saira", sans-serif;
}
body { background:var(--ferro-black); color:var(--ferro-white); font-family:var(--font-body); }
```
```html
<link href="https://fonts.googleapis.com/css2?family=Michroma&family=Saira:wght@400;500;600&display=swap" rel="stylesheet">
```

## 2. Logo in der Navigation + Favicon

```html
<link rel="icon" href="ferro33-assets/logo/favicon/favicon.svg" type="image/svg+xml">
<link rel="icon" href="ferro33-assets/logo/favicon/favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="ferro33-assets/logo/favicon/favicon-180.png">

<nav class="ferro-nav">
  <a href="/"><img src="ferro33-assets/logo/svg/ferro33-wordmark-horizontal-transparent-white.svg"
                   alt="Ferro 33 hair club" height="28"></a>
</nav>
```
```css
.ferro-nav { position:sticky; top:0; z-index:10; padding:18px 24px;
  background:rgb(11 12 14 / .85); backdrop-filter:blur(10px);
  border-bottom:1px solid rgb(30 184 245 / .35); }   /* LED-Kante wie am Waschtisch */
```

## 3. Hero (statisch — es gibt bewusst kein Video)

Das Banner hat links freie Fläche für die Headline.

```html
<section class="ferro-hero">
  <img src="ferro33-assets/web/ferro33-banner-hero.webp" alt="" class="ferro-hero__bg">
  <div class="ferro-hero__haze"></div>
  <div class="ferro-hero__content">
    <img src="ferro33-assets/logo/svg/ferro33-logo-primary-transparent-white.svg" alt="Ferro 33 hair club – Das Beste vom Besten" width="420">
    <p>Ohne Termin. 8 Stühle. Kaum Wartezeit. Mainzer Str. 2A, Worms.</p>
    <a class="ferro-btn" href="#leistungen">Leistungen & Preise</a>
  </div>
</section>
```
```css
.ferro-hero { position:relative; min-height:88vh; display:grid; align-items:center; overflow:hidden; }
.ferro-hero__bg { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:70% center; }
.ferro-hero__haze { position:absolute; inset:0;
  background:linear-gradient(90deg, var(--ferro-black) 0%, rgb(11 12 14 / .75) 40%, transparent 75%),
             radial-gradient(60% 50% at 20% 100%, rgb(31 91 255 / .25), transparent 70%); }
.ferro-hero__content { position:relative; max-width:520px; padding:0 6vw; }
.ferro-btn { display:inline-block; padding:14px 26px; border:1.5px solid var(--ferro-neon); border-radius:999px;
  color:var(--ferro-white); text-decoration:none; font-family:var(--font-display); font-size:.8rem; letter-spacing:.12em;
  box-shadow:0 0 24px rgb(30 184 245 / .35), inset 0 0 12px rgb(30 184 245 / .2); }
.ferro-btn:hover { background:var(--ferro-neon); color:var(--ferro-black); }
```

## 4. Leistungskarten (Hero-Shots, 1:1)

```html
<section id="leistungen" class="ferro-cards">
  <article class="ferro-card">
    <img src="ferro33-assets/web/ferro33-hero-haarschnitt-1x1.webp" alt="Präziser Skin Fade mit der Maschine">
    <h3>Haarschnitt</h3><p>Schneiden, waschen, föhnen, stylen</p><span>20 €</span>
  </article>
  <article class="ferro-card">
    <img src="ferro33-assets/web/ferro33-hero-bart-rasur-1x1.webp" alt="Bartrasur mit dem Rasiermesser">
    <h3>Bart & Rasur</h3><p>Trimmen, Konturen, Rasiermesser, Färben</p><span>ab 10 €</span>
  </article>
  <article class="ferro-card">
    <img src="ferro33-assets/web/ferro33-hero-dampf-maske-1x1.webp" alt="Heißes Tuch und Dampf im Barberstuhl">
    <h3>Dampf & Maske</h3><p>Das Winter-Ritual zum Abschalten</p><span>Saison</span>
  </article>
</section>
```
```css
.ferro-cards { display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:20px; padding:80px 6vw; }
.ferro-card { background:var(--ferro-graphite); border-radius:18px; overflow:hidden; border:1px solid #ffffff10;
  transition:border-color .3s, box-shadow .3s; }
.ferro-card:hover { border-color:var(--ferro-neon); box-shadow:0 0 32px rgb(30 184 245 / .25); }
.ferro-card img { width:100%; aspect-ratio:1; object-fit:cover; display:block; }
.ferro-card h3 { font-family:var(--font-display); font-size:1rem; margin:20px 20px 6px; }
.ferro-card p { color:var(--ferro-chrome); margin:0 20px; }
.ferro-card span { display:block; margin:14px 20px 22px; color:var(--ferro-neon); font-weight:600; }
```

## 5. Textur hinter Abschnitten + Lamellen-Streifen (CSS-Extra, 0 Credits)

```html
<section class="ferro-textured"> … Inhalt … </section>
<div class="ferro-lamella" aria-hidden="true"></div>
```
```css
.ferro-textured { position:relative; isolation:isolate; }
.ferro-textured::before { content:""; position:absolute; inset:0; z-index:-1; opacity:.18;
  background:url(ferro33-assets/web/ferro33-textur-lamellen.webp) center/cover; }
/* Weiß-schwarze Lamellen wie an den Spiegelsäulen – als Trenner zwischen Abschnitten */
.ferro-lamella { height:64px;
  background:repeating-linear-gradient(180deg, var(--ferro-white) 0 6px, var(--ferro-black) 6px 14px);
  -webkit-mask:linear-gradient(90deg, transparent, #000 15%, #000 85%, transparent);
          mask:linear-gradient(90deg, transparent, #000 15%, #000 85%, transparent); }
/* Neon-Glow-Overlay (ersetzt ein generiertes Haze-Bild) */
.ferro-glow::after { content:""; position:absolute; inset:auto 0 0 0; height:40%; pointer-events:none;
  background:radial-gradient(50% 100% at 50% 100%, rgb(30 184 245 / .22), transparent 70%); }
```

## 6. Story-/Galerie-Bilder

| Bild | Wofür |
| --- | --- |
| `web/ferro33-action-kontur.webp` | „Präzision“-Abschnitt, Konturenschnitt |
| `web/ferro33-detail-werkzeug.webp` | „Unser Handwerk“, heller Abschnitt (weißer Waschtisch-Look) |
| `web/ferro33-lifestyle-nacken.webp` | Über uns / Bewertungen („Es juckt danach nichts am Hals“) |
| `web/ferro33-hero-haarschnitt-16x9.webp`, `…dampf-maske-16x9.webp` | breite Abschnittsbilder |
