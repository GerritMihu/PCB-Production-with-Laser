# Design Rules (KiCad)

🇩🇪 [Deutsch](../de/03-design-regeln.md) · [← Overview](../../README.md)

## Values per machine

| Rule | xTool F2 Ultra | Trotec Speedy |
|---|---|---|
| Track width (net class Default) | 0.4 mm | TODO |
| Track width (net class Power) | 0.8 mm | TODO |
| Copper–copper clearance | 0.2 mm | TODO |
| Copper–board edge clearance | 1.0 mm | TODO |
| Via drill | 0.8 mm | TODO |
| Via pad (outer diameter) | 1.6 mm | TODO |
| Teardrops | on | TODO |
| Solder mask / silkscreen | no | TODO |

*xTool values as of 07/2026*

## Why these values?

- **0.4 mm tracks:** robust enough for beginners, tolerant of small focus or alignment errors, and survive soldering.
- **Net class "Power" 0.8 mm:** supply lines (e.g. NE555 or motor circuits) need more cross-section.
- **Teardrops:** reinforce the track → pad/via transition. Thin tracks otherwise tend to lift during soldering.
- **Large vias (0.8/1.6 mm):** suit hand-drilled holes and through-connections with wire/rivets.
- **1 mm to the edge:** copper at the edge is easily damaged when separating the board.

## Using the KiCad template

The template `kicad/template/Laser_PCB_xTool/` contains all rules above, the net classes *Default* and *Power*, and the teardrop settings.

**One-time setup:**

1. KiCad → *Preferences → Configure Paths*
2. Set `KICAD_USER_TEMPLATE_DIR` to this repo's `kicad/template` folder
   (or copy `Laser_PCB_xTool` into your existing user template directory).

**New project:** *File → New Project from Template → Laser_PCB_xTool*

> Nets named `GND`, `VCC`, `VBUS`, `VIN`, `+BATT` and `+…V…` (e.g. `+5V`, `+3V3`) are automatically assigned to net class **Power**.

**Converting an existing project:** In the PCB editor *File → Board Setup → Import Settings…* and select the template project `Laser_PCB_xTool.kicad_pro`.

## Checklist before export

- [ ] DRC without errors
- [ ] Board outline on `Edge.Cuts` closed
- [ ] Ground plane added (saves laser time)
- [ ] Teardrops generated (*Edit → Add/Remove Teardrops*)
