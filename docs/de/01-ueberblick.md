# Überblick & Ablauf

🇬🇧 [English](../en/01-overview.md) · [← Übersicht](../../README.de.md)

## Verfahren: Kupfer-Ablation

Eine kupferkaschierte Platine (FR4) wird in den Laser gelegt. Der Laser verdampft das Kupfer überall dort, wo **keine** Leiterbahn sein soll. Übrig bleiben Leiterbahnen und Pads.

| Vorteil | Nachteil |
|---|---|
| keine Chemie, kein Ätzbad | Laserzeit steigt mit der abzutragenden Kupferfläche |
| schnell vom Entwurf zur Platine | Lötstopplack derzeit nicht möglich |
| feine Strukturen möglich | Dämpfe/Rauch → Absaugung Pflicht |

> **Tipp:** Eine große Massefläche (GND-Zone) verringert die abzutragende Fläche und damit die Laserzeit deutlich.

## Ablauf

```
KiCad-Entwurf ──► DRC mit Laser-Template ──► Export (Gerber/SVG)
      │
      ▼
Laser-Software: Import, Ausrichten, Parameter wählen
      │
      ▼
Platine einlegen, fokussieren ──► Kupfer abtragen ──► (Bohren / Kontur)
      │
      ▼
Reinigen ──► Durchgang prüfen ──► Bestücken & Löten
```

1. **Entwurf** in KiCad mit der [Laser-Vorlage](03-design-regeln.md).
2. **Export** der Kupferlagen und des Umrisses → [Export](04-export.md).
3. **Laser-Job** vorbereiten – maschinenspezifisch, siehe `machines/`.
4. **Nachbearbeitung** → [Nachbearbeitung](05-nachbearbeitung.md).

## Material

| Material | Hinweis |
|---|---|
| FR4, einseitig/zweiseitig kupferkaschiert | TODO: Kupferstärke (z. B. 35 µm), Plattendicke, Bezugsquelle |
| Isopropanol, Pinsel/Zahnbürste | Reinigung |
| Multimeter | Durchgangsprüfung |

> **TODO:** Fotos vom Ablauf einfügen (`images/`).
