# Testlayout Fertigungsverfahren

🇬🇧 [English](README.md) · [← Übersicht](../../README.de.md)

Einheitliche Testplatine (100 × 80 mm, einseitig F.Cu), um Fertigungsverfahren unter gleichen Bedingungen zu vergleichen:

1. Laser-Ablation direkt (xTool F2 Ultra, Faserlaser)
2. Laser-Maske + Ätzen (Lack mit dem Laser abtragen, dann Eisen(III)-chlorid)
3. CNC-Isolationsfräsen
4. Ätzen klassisch (Tonertransfer o. Ä.)

![Testlayout F.Cu](../../images/testlayout/testlayout-F_Cu.png)

## Teststrukturen

| Feld | Inhalt | Prüfung |
|---|---|---|
| Leiterbahn | Bahnen 0,10 / 0,15 / 0,20 / 0,30 / 0,40 / 0,50 mm, je 30 mm lang zwischen zwei Testpads | Durchgang und Widerstand (Multimeter), Breite unter Lupe/Mikroskop |
| Abstand | Kammstrukturen mit Spalt 0,10 … 0,50 mm (Bahnbreite 0,4 mm) | Isolation zwischen Pad A und Pad B (Multimeter: kein Durchgang) |
| SMD | 0603, 0805, 1206, SOT-23, SOIC-8, TSSOP-14 (KiCad-Standardbibliothek) | Pads vollständig und getrennt? Probebestückung |
| THT | Bohrung/Pad 0,6/1,2 · 0,8/1,6 · 1,0/2,0 · 1,2/2,4 mm | Restring nach dem Bohren, Ausrichtung |
| Text | Kupfertext 1,0 / 1,5 / 2,0 mm | Lesbarkeit |
| Maßstab | 50 mm (X) und 20 mm (Y) mit Teilstrichen | Maßhaltigkeit mit Messschieber |

Die Design-Regeln der Vorlage wurden für dieses Projekt bewusst gesenkt (min. 0,1 mm), damit die Teststrukturen DRC-fehlerfrei sind. Für normale Projekte gelten weiter die Werte aus [Design-Regeln](../../docs/de/03-design-regeln.md).

## Ablauf

1. Platinenmaterial (FR4, 35 µm Cu) reinigen, Material und Kupferdicke notieren.
2. Platine je Verfahren fertigen. Laser-Parameter, Fräser, Ätzmittel, Temperatur und Zeit notieren.
3. Zeit stoppen: Vorbereitung, Bearbeitung, Nacharbeit getrennt.
4. Prüfen nach dem Messprotokoll unten. Fotos (Lupe/Mikroskop) mit Maßstab aufnehmen.

## Messprotokoll (je Platine)

| | |
|---|---|
| Verfahren | |
| Datum / Prüfer\*in | |
| Material / Kupferdicke | |
| Parameter (Leistung, Geschwindigkeit, Frequenz, Durchgänge bzw. Fräser/Ätzmittel) | |
| Zeit Vorbereitung / Bearbeitung / Nacharbeit (min) | |
| Material- und Verschleißkosten (€) | |

| Leiterbahn (mm) | 0,10 | 0,15 | 0,20 | 0,30 | 0,40 | 0,50 |
|---|---|---|---|---|---|---|
| Durchgang (ja/nein) | | | | | | |
| Widerstand (Ω) | | | | | | |
| gemessene Breite (mm) | | | | | | |

| Abstand (mm) | 0,10 | 0,15 | 0,20 | 0,30 | 0,40 | 0,50 |
|---|---|---|---|---|---|---|
| isoliert (ja/nein) | | | | | | |
| Bemerkung (Grat, Brücke, Unterätzung) | | | | | | |

| Maßstab | Soll | Ist |
|---|---|---|
| X | 50,0 mm | |
| Y | 20,0 mm | |

SMD, THT, Text: je Feld „in Ordnung / mangelhaft / nicht fertigbar“ plus Bemerkung.

## Dateien

- `generate_testlayout.py` erzeugt `testlayout.kicad_pcb` und `testlayout.kicad_pro` (Werte oben im Skript änderbar). Danach in KiCad öffnen und DRC prüfen.
- Die Laser-Dateien (DXF, SVG, Gerber) erzeugt der KiBot-Workflow automatisch in `laser/`.
