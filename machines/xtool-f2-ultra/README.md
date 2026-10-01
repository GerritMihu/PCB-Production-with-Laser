# xTool F2 Ultra

🇩🇪 [Deutsch](README.de.md) · [← Overview](../../README.md)

## Machine data

| | |
|---|---|
| Laser sources | 60 W MOPA fiber laser + 40 W diode laser *(manufacturer spec – verify on site)* |
| Beam steering | galvo |
| Laser class | TODO (rating plate) |
| Connection | USB / Wi-Fi |
| Software | xTool Studio (Windows/macOS), Linux: [see test](software-linux.md) |
| Location | TODO |

## Design rules

See [Design rules](../../docs/en/03-design-rules.md) – KiCad template `Laser_PCB_xTool`.

## Laser parameters for copper ablation

> **TODO:** enter proven values. One row per material/copper thickness.

| Step | Laser | Power | Speed | Frequency | Pulse width | Passes | Line spacing | Focus |
|---|---|---|---|---|---|---|---|---|
| Ablate copper (fill) | fiber | TODO | TODO | TODO | TODO | TODO | TODO | TODO |
| Trace outlines | fiber | TODO | TODO | TODO | TODO | TODO | – | TODO |
| Cleaning pass | fiber | TODO | TODO | TODO | TODO | TODO | TODO | TODO |

Store xTool Studio project files/material presets in [`presets/`](presets/).

## Workflow in xTool Studio

1. Import the SVG from the [export](../../docs/en/04-export.md).
2. Check the scale (measure board width).
3. TODO: invert fill / select area between tracks.
4. Place and fix the board, set focus.
5. Run framing → check position.
6. Start job, extraction running.
7. TODO: align top/bottom (stop, registration marks, camera?).

## Solder mask

As of 07/2026: **no working process yet.** Document attempts here.

| Date | Attempt | Result |
|---|---|---|
| | | |
