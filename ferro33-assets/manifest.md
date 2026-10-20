# Manifest — Ferro 33 hair club Asset Pack

**Credits:** 16 von 16 (8 × nano_banana_pro, 2K, je 2 Credits). Kontostand vorher 286, nachher 270.  
**Kein Video** (bewusst, Budget). **Logo ohne KI** — Vektor-Nachbau, 0 Credits.

## Fotos (nano_banana_pro, 2K, 2752 × 1536)

Jeder Prompt endet mit dem gemeinsamen Style-Block:

> Consistent house style: premium commercial photography, 50mm look, high contrast, colour palette strictly club black, glossy graphite, clean white and electric neon blue accents only — no warm or orange tones, no red, no vintage barber pole, no skulls, no wood or leather-saloon kitsch. Photoreal, crisp, no text, no watermark.

| # | Datei(en) | Format | Job-ID | Credits |
|---|---|---|---|---|
| 1 | banner/ferro33-banner-hero.png | 16:9 + Referenzfoto Laden | `34e81014-c31a-4207-99c8-43df384266f5` | 2 |
| 2 | heroes/ferro33-hero-haarschnitt-16x9.png<br>heroes/ferro33-hero-haarschnitt-1x1.png (Crop) | 16:9 | `8f77d6d6-cf6e-4faa-a9dc-ca9160552b2d` | 2 |
| 3 | heroes/ferro33-hero-bart-rasur-1x1.png (Crop, siehe Hinweis) | 16:9 | `4e7ea112-e43f-4f93-aad3-109be2abc4e9` | 2 |
| 4 | heroes/ferro33-hero-dampf-maske-16x9.png<br>heroes/ferro33-hero-dampf-maske-1x1.png (Crop) | 16:9 | `318c1786-f433-4a17-bdfd-8a933e23c37c` | 2 |
| 5 | action/ferro33-action-kontur.png | 16:9 | `ac107067-e7b3-4136-94c6-ffea5d6b0788` | 2 |
| 6 | detail/ferro33-detail-werkzeug.png | 16:9 | `ce46562c-227c-4350-8d83-1d51db0bdf8c` | 2 |
| 7 | lifestyle/ferro33-lifestyle-nacken.png (Neonschild im Hintergrund weichgezeichnet) | 16:9 | `aa739d8e-b564-4289-b561-db51e9651799` | 2 |
| 8 | extras/textures/ferro33-textur-lamellen.png | 16:9 | `ccaabc06-5a54-4b5c-9360-d74bab33b79f` | 2 |

### Prompts

**1. ferro33-banner-hero**  
Wide cinematic interior of a modern men's hair club at night, inspired by the reference photo: a single black leather barber chair on the right third, glossy black walls with horizontal white lamella stripes, a long white solid-surface counter with a thin electric neon-blue LED edge glow, recessed ceiling downlights, black tiled floor with soft reflections. The left half of the frame is calm, dark and empty negative space for a headline. Nobody in frame. No signage, no screens with content, no readable text anywhere.

**2. ferro33-hero-haarschnitt**  
Macro close-up of a skin fade being cut: barber's hand holding a matte black cordless clipper against the back of a client's head, the gradient from skin to short dark hair razor sharp, tiny cut hairs floating in the light. Background deep black with a blurred band of white horizontal stripes and a thin neon-blue rim light tracing the edge of the head. No face visible, no logos, no text.

**3. ferro33-hero-bart-rasur**  
Macro close-up of a straight razor shave on a man's cheek and dark beard line: white shaving foam, the polished steel blade drawing one perfectly clean edge, the barber's hand steady with a black nitrile glove. Cool neon-blue rim light on the blade's edge, glossy black background, a soft white highlight. Jawline only, eyes not in frame, no logos, no text.

**4. ferro33-hero-dampf-maske**  
A man relaxing reclined in a black leather barber chair with a hot white towel wrapped over his face, thick soft steam rising and curling into a beam of cool neon-blue light against a black background, a barber's hands gently pressing the towel. Calm, luxurious winter ritual. Face fully covered by the towel, no logos, no text.

**5. ferro33-action-kontur**  
Extreme macro of a precision line-up: barber's fingers holding a black T-blade trimmer creating a crisp hairline edge at the temple, hair clippings scattered on skin, sharp focus on the steel teeth, deep black background with one thin neon-blue light streak. Physical, tactile, high-end commercial photography. No face, no logos, no text.

**6. ferro33-detail-werkzeug**  
Overhead flat-lay of barber tools on a glossy white solid-surface counter: matte black clipper, steel straight razor, black carbon comb, badger shaving brush, a black ceramic bowl of white lather, folded black towel. Strict geometric arrangement, generous negative space, one edge of the counter glowing with a thin neon-blue LED line. No brand names, no labels, no readable text.

**7. ferro33-lifestyle-nacken**  
Barber's hands in black sleeves using a soft neck duster brush to sweep the last cut hairs off a client's freshly faded neckline, the client wearing a black and white horizontally striped cutting cape. Warm human moment, shallow depth of field, black interior with a soft neon-blue glow in the background bokeh. Back of head only, no faces, no logos, no readable text anywhere.

**8. ferro33-textur-lamellen**  
Abstract architectural texture filling the whole frame: glossy black horizontal lamella slats alternating with thin matte white stripes, viewed slightly off-axis, a very faint neon-blue light bleeding from the slat gaps, very low contrast and dark, minimal and calm, suitable as a website section background under white text. No objects, no people, no text.

## Nachbearbeitung (lokal, 0 Credits)

- **Bart-Rasur:** die 16:9-Generierung hatte oben links einen schwarzen Artefakt-Block über dem Gesicht → nur als 1:1-Crop ausgeliefert (Messer, Schaum, Handschuh). Eine 16:9-Version bräuchte eine Neu-Generierung (2 Credits).
- **Lifestyle:** ein unlesbares Neonschild im Hintergrund wurde weichgezeichnet (Regel: keine Schrift im Foto).
- **1:1-Versionen** von Haarschnitt und Dampf & Maske: Mitten-Crops aus 16:9 statt eigener Generierung (Budget).
- **web/**: alle Fotos als WebP, max. 1920 px, für die Website.

## Logo (Vektor, 0 Credits)

- `logo/build_logo.py` baut alle Varianten reproduzierbar: monolineare Glyphen mit runden Enden (wie die Leuchtschrift am Laden), Claim „DAS BESTE VOM BESTEN“ in Michroma (in Pfade umgewandelt), ®-Zeichen, Barber-Profil per potrace vom Logo-Foto vektorisiert (`logo/src/barber-profile.svg`).
- Lockups: `logo-primary` (Bannerschild), `logo-stacked` (Pylon mit Profil), `wordmark-horizontal` (Fassade), `monogram` (33, Favicon/Avatar), `icon-barber`.
- Farbvarianten: `ink` (schwarz, transparent), `on-white`, `white-on-black`, `transparent-white`, `neon`.
- `logo/png/` = 2000 px PNG-Exporte, `logo/favicon/` = favicon.svg/.ico + 16–512 px.
