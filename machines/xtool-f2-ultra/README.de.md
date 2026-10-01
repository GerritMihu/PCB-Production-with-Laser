# xTool F2 Ultra

🇬🇧 [English](README.md) · [← Übersicht](../../README.de.md)

## Maschinendaten

| | |
|---|---|
| Laserquellen | 60 W MOPA-Faserlaser + 40 W Diodenlaser *(Herstellerangabe – vor Ort prüfen)* |
| Ablenkung | Galvo |
| Laserklasse | TODO (Typenschild) |
| Anbindung | USB / WLAN |
| Software | xTool Studio (Windows/macOS), Linux: [siehe Test](software-linux.de.md) |
| Standort | TODO |

## Design-Regeln

Siehe [Design-Regeln](../../docs/de/03-design-regeln.md) – KiCad-Vorlage `Laser_PCB_xTool`.

## Laser-Parameter Kupfer-Ablation

> **TODO:** Bewährte Werte eintragen. Je Material/Kupferstärke eine Zeile.

| Schritt | Laser | Leistung | Geschwindigkeit | Frequenz | Pulsbreite | Durchgänge | Linienabstand | Fokus |
|---|---|---|---|---|---|---|---|---|
| Kupfer abtragen (Füllung) | Faser | TODO | TODO | TODO | TODO | TODO | TODO | TODO |
| Konturen nachfahren | Faser | TODO | TODO | TODO | TODO | TODO | – | TODO |
| Reinigungsdurchgang | Faser | TODO | TODO | TODO | TODO | TODO | TODO | TODO |

Projektdateien/Materialvorlagen aus xTool Studio unter [`presets/`](presets/) ablegen.

## Ablauf in xTool Studio

1. SVG aus dem [Export](../../docs/de/04-export.md) importieren.
2. Maßstab prüfen (Platinenbreite messen).
3. TODO: Füllung invertieren / Fläche zwischen Leiterbahnen auswählen.
4. Platine einlegen und fixieren, Fokus einstellen.
5. Rahmen (Framing) fahren → Position kontrollieren.
6. Job starten, Absaugung läuft.
7. TODO: Ober-/Unterseite ausrichten (Anschlag, Passmarken, Kamera?).

## Lötstopplack

Stand 07/2026: **noch kein funktionierendes Verfahren.** Versuche hier dokumentieren.

| Datum | Versuch | Ergebnis |
|---|---|---|
| | | |
