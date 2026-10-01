# Export: KiCad → Laser

🇩🇪 [Deutsch](../de/04-export.md) · [← Overview](../../README.md)

The laser only needs **copper layers, outline and drill marks**. Solder mask and silkscreen are omitted.

**Proven format for xTool Studio: DXF**, with the outline in every copper DXF. xTool fills the compound shape so that exactly the copper between the tracks is removed.

| Path | Guide |
|---|---|
| Manually in KiCad (Plot → DXF) | [Manual path, Part C](08-guide-manual.md#part-c-export-for-the-laser-kicad) |
| Automatically with KiBot / GitHub Actions | [Automatic path](09-guide-automatic.md) |

## Key settings

| Setting | Value | Why |
|---|---|---|
| Plot format | DXF | imported into xTool Studio as vectors |
| Plot on All Layers | `Edge.Cuts` | outline + copper = compound shape that can be filled |
| Drill marks | small | the centre point for drilling stays copper-free |
| Contours (polygon mode) | on | areas instead of centre lines |
| Units | millimeters | no conversion errors |

## Notes

- **Bottom side (B.Cu):** the board is flipped, so the image must be mirrored, either in xTool Studio or as a mirrored SVG (KiBot).
- **Check the scale:** verify the board width in xTool Studio after importing.
- **SVG** also works as an alternative (KiBot crops it to the board), but has not been tested at the machine yet.
