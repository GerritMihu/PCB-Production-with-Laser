# PCB Production with a Laser

🇩🇪 [Deutsche Version](README.de.md)

Documentation of PCB fabrication in our school workshop: copper is **removed directly by the laser** (ablation) – no photoresist, no etching, no chemicals.

The documentation is machine-independent: the process lives in `docs/`, machine-specific data and parameters in `machines/<machine>/`.

## Machines

| | [xTool F2 Ultra](machines/xtool-f2-ultra/README.md) | [Trotec Speedy](machines/trotec-speedy/README.md) |
|---|---|---|
| Status | in use | trial planned |
| Process | copper ablation (fiber) | TODO |
| Min. track width | 0.4 mm | TODO |
| Copper–copper clearance | 0.2 mm | TODO |
| Copper–edge clearance | 1.0 mm | TODO |
| Via (drill / pad) | 0.8 / 1.6 mm | TODO |
| Solder mask | no working process yet | TODO |
| Software | xTool Studio | TODO |
| Linux | Wine: installs & launches, device test pending – [Linux test](machines/xtool-f2-ultra/software-linux.md) | TODO |

## Contents

1. [Overview & workflow](docs/en/01-overview.md)
2. [Safety](docs/en/02-safety.md)
3. [Design rules (KiCad)](docs/en/03-design-rules.md)
4. [Export: KiCad → laser](docs/en/04-export.md)
5. [Post-processing](docs/en/05-post-processing.md)
6. [Common defects](docs/en/06-defects.md)
7. [Student quick guide](docs/en/07-student-guide.md)
8. [**Manual path step by step:** KiCad → xTool](docs/en/08-guide-manual.md)
9. [**Automatic path:** KiBot + GitHub Actions](docs/en/09-guide-automatic.md)

## Repository layout

```
docs/de, docs/en       process (machine-independent)
machines/<machine>/    machine data, laser parameters, presets, software
kicad/template/        KiCad project template with matching design rules
kibot/                 KiBot config for laser export (DXF + SVG + Gerber)
examples/              example projects incl. auto-generated laser files
images/                photos and graphics
```

## Adding a machine

1. Copy `machines/trotec-speedy/` → `machines/<new-machine>/`
2. Add a column to the table above (DE + EN)
3. If different design rules are needed: add a template under `kicad/template/Laser_PCB_<machine>/`

## License

[CC BY-SA 4.0](LICENSE)
