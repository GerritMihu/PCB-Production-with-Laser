# Export: KiCad → Laser

🇩🇪 [Deutsch](../de/04-export.md) · [← Overview](../../README.md)

The laser only needs **copper layers, outline and drill data**. Solder mask and silkscreen are omitted.

## Option A: KiBot (recommended)

The config `kibot/laser.kibot.yaml` produces:

| Output | File(s) | Use |
|---|---|---|
| Gerber | `laser/gerber/*-F_Cu.gbr`, `*-B_Cu.gbr`, `*-Edge_Cuts.gbr` | archive / other machines |
| Drill | `laser/gerber/*.drl` + drill map PDF | drilling |
| SVG top | `laser/svg/*-F_Cu.svg` | import into laser software |
| SVG bottom | `laser/svg/*-B_Cu.svg` (**mirrored**) | import into laser software |
| SVG outline | `laser/svg/*-Edge_Cuts.svg` | contour cut / alignment |

**Locally:**

```bash
kibot -c "/path/to/PCB-Production with Laser/kibot/laser.kibot.yaml" -b MyBoard.kicad_pcb -d laser/
```

**In GitHub Actions** (same KiCad 10 container as the other repos): copy the config into the project repo and call it in the workflow:

```yaml
- name: Laser export
  run: kibot -c laser.kibot.yaml -d cam/
```

## Option B: manually in KiCad

1. PCB editor → *File → Plot*
2. Format **SVG**, layers `F.Cu` (+ `Edge.Cuts`), scale 1:1
3. For `B.Cu`: enable **Mirrored plot**
4. *Drill marks: Actual size* – helps when drilling after lasering

## Notes

- **Mirror the bottom side:** the board is flipped to laser the bottom, so the image must be mirrored.
- **Positive/negative:** depending on the laser software, the area *between* the tracks has to be filled. How this is done is machine-specific, see `machines/<machine>/`.
- **Check the scale:** after import, verify a known dimension (e.g. board width) in the laser software.
