# Overview & Workflow

🇩🇪 [Deutsch](../de/01-ueberblick.md) · [← Overview](../../README.md)

## Process: copper ablation

A copper-clad board (FR4) is placed in the laser. The laser vaporizes the copper everywhere there should be **no** track. Tracks and pads remain.

| Advantage | Disadvantage |
|---|---|
| no chemicals, no etching bath | laser time grows with the copper area to remove |
| fast from design to board | solder mask not possible at the moment |
| fine features possible | fumes/smoke → extraction mandatory |

> **Tip:** A large ground plane (GND zone) reduces the area to remove and therefore the laser time considerably.

## Workflow

```
KiCad design ──► DRC with laser template ──► export (Gerber/SVG)
      │
      ▼
Laser software: import, align, choose parameters
      │
      ▼
Place board, focus ──► ablate copper ──► (drill / contour)
      │
      ▼
Clean ──► continuity test ──► assemble & solder
```

1. **Design** in KiCad with the [laser template](03-design-rules.md).
2. **Export** copper layers and outline → [Export](04-export.md).
3. **Prepare the laser job** – machine-specific, see `machines/`.
4. **Post-processing** → [Post-processing](05-post-processing.md).

## Materials

| Material | Note |
|---|---|
| FR4, single/double-sided copper-clad | TODO: copper thickness (e.g. 35 µm), board thickness, supplier |
| Isopropanol, brush/toothbrush | cleaning |
| Multimeter | continuity test |

> **TODO:** add photos of the workflow (`images/`).
