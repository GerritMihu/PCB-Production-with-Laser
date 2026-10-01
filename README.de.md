# Leiterplattenfertigung mit dem Laser

🇬🇧 [English version](README.md)

Dokumentation der Leiterplattenfertigung in der Schulwerkstatt: Kupfer wird **direkt per Laser abgetragen** (Ablation) – ohne Fotolack, ohne Ätzen, ohne Chemie.

Die Doku ist maschinenunabhängig aufgebaut: Das Verfahren steht in `docs/`, maschinenspezifische Daten und Parameter in `machines/<maschine>/`.

## Maschinen

| | [xTool F2 Ultra](machines/xtool-f2-ultra/README.de.md) | [Trotec Speedy](machines/trotec-speedy/README.de.md) |
|---|---|---|
| Status | im Einsatz | Teststellung geplant |
| Verfahren | Kupfer-Ablation (Faser) | TODO |
| Leiterbahn min. | 0,4 mm | TODO |
| Abstand Kupfer–Kupfer | 0,2 mm | TODO |
| Abstand Kupfer–Rand | 1,0 mm | TODO |
| Via (Bohrung / Pad) | 0,8 / 1,6 mm | TODO |
| Lötstopplack | noch kein Verfahren | TODO |
| Software | xTool Studio | TODO |
| Linux | Wine: installiert & startet, Gerätetest offen – [Linux-Test](machines/xtool-f2-ultra/software-linux.de.md) | TODO |

## Inhalt

1. [Überblick & Ablauf](docs/de/01-ueberblick.md)
2. [Sicherheit](docs/de/02-sicherheit.md)
3. [Design-Regeln (KiCad)](docs/de/03-design-regeln.md)
4. [Export: KiCad → Laser](docs/de/04-export.md)
5. [Nachbearbeitung](docs/de/05-nachbearbeitung.md)
6. [Fehlerbilder](docs/de/06-fehlerbilder.md)
7. [Schüler-Kurzanleitung](docs/de/07-schueler-anleitung.md)

## Repo-Struktur

```
docs/de, docs/en       Verfahren (maschinenunabhängig)
machines/<maschine>/   Maschinendaten, Laser-Parameter, Presets, Software
kicad/template/        KiCad-Projektvorlage mit passenden Design-Regeln
kibot/                 KiBot-Config für den Laser-Export (Gerber + SVG)
images/                Fotos und Grafiken
```

## Neue Maschine hinzufügen

1. `machines/trotec-speedy/` als Vorlage kopieren → `machines/<neue-maschine>/`
2. Spalte in der Tabelle oben (DE + EN) ergänzen
3. Falls andere Design-Regeln nötig: eigenes Template unter `kicad/template/Laser_PCB_<maschine>/`

## Lizenz

[CC BY-SA 4.0](LICENSE)
