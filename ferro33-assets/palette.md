# Ferro 33 hair club — Farbpalette „Club Noir Neon“

Abgeleitet aus dem Laden selbst: Hochglanzschwarz, weiße Lamellenstreifen, weiße Waschtische mit LED-Kante, blaues Neonlicht.

| Name | Hex | Rolle |
| --- | --- | --- |
| **Club Black** | `#0B0C0E` | Haupthintergrund, Logo-Farbe auf hellem Grund |
| **Lack-Graphit** | `#1A1D22` | Karten, Flächen, Navigation, Abschnittswechsel |
| **Lamellen-Weiß** | `#F4F5F7` | Text auf Dunkel, Streifen, helle Abschnitte |
| **Chrom-Grau** | `#8E959E` | Sekundärtext, Linien, Icons |
| **Ferro Neon** | `#1EB8F5` | Akzent: Buttons, LED-Kanten, Hover, Highlights (sparsam!) |
| **LED-Blau** | `#1F5BFF` | Tiefer Akzent für Verläufe und Glow (wie die Deckenringe im Laden) |

```css
:root {
  --ferro-black:   #0B0C0E;
  --ferro-graphite:#1A1D22;
  --ferro-white:   #F4F5F7;
  --ferro-chrome:  #8E959E;
  --ferro-neon:    #1EB8F5;
  --ferro-led:     #1F5BFF;
  --ferro-glow:    0 0 24px rgb(30 184 245 / .45);
}
```

**Regeln**
- 90 % Schwarz/Weiß, höchstens 10 % Neon. Neon ist Licht, keine Fläche.
- Keine warmen Töne (kein Gold, Kupfer, Holz, Rot) — das ist der Vintage-Barber-Kitsch, den Ferro 33 nicht ist.
- Neon nie als Textfarbe für Fließtext, nur für Akzente, Kanten und Buttons.
