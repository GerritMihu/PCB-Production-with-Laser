# Design-Regeln (KiCad)

🇬🇧 [English](../en/03-design-rules.md) · [← Übersicht](../../README.de.md)

## Werte je Maschine

| Regel | xTool F2 Ultra | Trotec Speedy |
|---|---|---|
| Leiterbahn (Netzklasse Default) | 0,4 mm | TODO |
| Leiterbahn (Netzklasse Power) | 0,8 mm | TODO |
| Abstand Kupfer–Kupfer | 0,2 mm | TODO |
| Abstand Kupfer–Platinenrand | 1,0 mm | TODO |
| Via Bohrung | 0,8 mm | TODO |
| Via Pad (Außendurchmesser) | 1,6 mm | TODO |
| Teardrops | ein | TODO |
| Lötstopplack / Bestückungsdruck | nein | TODO |

*Stand xTool: 07/2026*

## Warum diese Werte?

- **0,4 mm Leiterbahn:** robust genug für Anfänger, verzeiht leichte Fokus- oder Ausrichtungsfehler und hält beim Löten.
- **Netzklasse „Power" 0,8 mm:** Versorgungsleitungen (z. B. bei NE555- oder Motorschaltungen) brauchen mehr Querschnitt.
- **Teardrops:** verstärken den Übergang Leiterbahn → Pad/Via. Bei dünnen Bahnen reißt sonst gerne das Kupfer beim Löten ab.
- **Große Vias (0,8/1,6 mm):** passen zu handgebohrten Löchern bzw. Durchkontaktierung per Draht/Niete.
- **1 mm zum Rand:** Kupfer am Rand wird beim Trennen leicht beschädigt.

## KiCad-Vorlage verwenden

Die Vorlage `kicad/template/Laser_PCB_xTool/` enthält alle Regeln oben, die Netzklassen *Default* und *Power* sowie Teardrop-Einstellungen.

**Einmalig einrichten:**

1. KiCad → *Einstellungen → Pfade konfigurieren*
2. `KICAD_USER_TEMPLATE_DIR` auf den Ordner `kicad/template` dieses Repos setzen
   (oder den Ordner `Laser_PCB_xTool` in das vorhandene Benutzer-Vorlagenverzeichnis kopieren).

**Neues Projekt:** *Datei → Neues Projekt aus Vorlage → Laser_PCB_xTool*

> Netze mit den Namen `GND`, `VCC`, `VBUS`, `VIN`, `+BATT` sowie `+…V…` (z. B. `+5V`, `+3V3`) landen automatisch in der Netzklasse **Power**.

**Bestehendes Projekt umstellen:** Im Leiterplatteneditor *Datei → Platinen-Einstellungen → Importieren…* und das Template-Projekt `Laser_PCB_xTool.kicad_pro` auswählen.

## Checkliste vor dem Export

- [ ] DRC ohne Fehler
- [ ] Platinenumriss auf `Edge.Cuts` geschlossen
- [ ] Massefläche gesetzt (spart Laserzeit)
- [ ] Teardrops erzeugt (*Bearbeiten → Teardrops hinzufügen/entfernen*)
