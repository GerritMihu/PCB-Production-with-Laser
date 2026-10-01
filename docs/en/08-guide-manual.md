# Manual Path: from KiCad Schematic to Lasered Board

🇩🇪 [Deutsch](../de/08-anleitung-manuell.md) · [← Overview](../../README.md)

This guide describes **every single click**, from the empty KiCad template to the cut-out board in the xTool F2 Ultra.

- **Software:** KiCad 10, xTool Studio 1.9.11
- **Example:** [Schnupperblinki](../../examples/schnupperblinki/)
- **Parameters:** [xTool F2 Ultra](../../machines/xtool-f2-ultra/README.md#laser-parameters-as-of-072026)

> The school PCs run the **German** UI. German labels are given in *(parentheses)* where it helps.
> `Menu → Item` means: click *Menu*, then *Item*.
> 📸 marks places where a screenshot will be added.

---

## Part A: Schematic (KiCad)

### A1. Create a project from the laser template

One-time setup: configure the template path, see [Design rules](03-design-rules.md#using-the-kicad-template).

1. Start KiCad.
2. Click `File → New Project...` *(Datei → Neues Projekt ...)*. The **Project Template Selector** *(Projektvorlagenauswahl)* window opens.
3. Select the user templates tab and click **Laser_PCB_xTool**.
4. Click **OK**.
5. Choose a location, enter a project name (e.g. `blinker`) and click **Save**.

📸 *Project Template Selector with Laser_PCB_xTool*

### A2. Draw the schematic

1. In the project manager, click **Schematic Editor** (or double-click `blinker.kicad_sch`).
2. Place parts: press **A** (add symbol), search for a part, e.g. `NE555`, and click **OK**. Then click in the schematic to place it.
3. Draw connections: press **W** (wire), click a pin end, then click the target pin.
4. Power: press **P** and place `GND` or `+5V`.
   > The template puts these nets into net class **Power** automatically, so they are routed 0.8 mm wide.

📸 *finished schematic*

### A3. Annotate, assign footprints, ERC

1. Open `Tools → Annotate Schematic...`, then click **Annotate** and **Close**.
2. Open `Tools → Assign Footprints...`. Assign a footprint from the right-hand list to each symbol on the left (double-click), then click **OK**.
   > Beginners should prefer **THT footprints** (through-hole). Their large pads are easier to laser and to solder.
3. Open `Inspect → Electrical Rules Checker` and click **Run ERC**. There must be **0 errors**.
4. Save with **Ctrl+S**.

📸 *ERC without errors*

---

## Part B: Board (KiCad)

### B1. Transfer the schematic to the board

1. In the schematic editor, open `Tools → Update PCB from Schematic...` (or press **F8**).
2. Click **Update PCB**, then **Close**.
3. The parts are attached to the mouse cursor: click on the canvas to drop them.

### B2. Draw the board outline

1. In the layer panel on the right, click layer **Edge.Cuts**.
2. Choose `Place → Draw Rectangle`.
3. Click the top-left corner, then the bottom-right corner.
   > Keep at least **1 mm** between copper and the outline (DRC checks this).

### B3. Place parts and route tracks

1. Move parts with the mouse, rotate them with **R**.
2. Select layer **B.Cu**. For single-sided boards the copper side is at the bottom and the parts sit on top.
   > **TODO:** decide which side. The Stiftklavier project was lasered on **F.Cu**.
3. Press **X** (Route Single Track), click a pad, then click the target pad.
   > The net class sets the width automatically: signal 0.4 mm, power 0.8 mm.

### B4. Add a ground plane (saves laser time)

1. Choose `Place → Add Zone` (or press **Ctrl+Shift+Z**).
2. Click one board corner. In **Copper Zone Properties**, tick the copper layer, select **Net:** `GND` and click **OK**.
3. Click the remaining corners, then double-click to finish.
4. Choose `Edit → Fill All Zones` (key **B**).

### B5. DRC

1. Open `Inspect → Design Rules Checker`.
2. Click **Run DRC**. There must be **0 violations**. Warnings about libraries or silkscreen don't matter for the laser.
3. Save with **Ctrl+S**.

📸 *finished board in the PCB editor*

---

## Part C: Export for the laser (KiCad)

The export is **DXF**, exactly as in the proven Stiftklavier project.

1. In the PCB editor, open `File → Fabrication Outputs → Plot...` *(Datei → Fertigungsdaten → Plotten ...)*. Depending on the version it may be `File → Plot...` directly.
2. Settings in the **Plot** window:

   | Field | Setting |
   |---|---|
   | **Plot format** | `DXF` |
   | **Output directory** | `cam/` |
   | **Include Layers** (left) | tick `F.Cu` (or `B.Cu`) and `Edge.Cuts` |
   | **Plot on All Layers** (right) | tick `Edge.Cuts`, so the outline ends up in every copper DXF |
   | **Drill marks** | `Small mark` (centre point for drilling) |
   | **Plot drawing sheet** | **off** |
   | **DXF Options** → *Plot graphic items using their contours* | **on** |
   | **DXF Options** → *Use KiCad font to plot text* | **on** |
   | **DXF Options** → *Export units* | `Millimeters` |

3. Click **Plot**.
4. Click **Close**.

**Result** in the `cam/` folder:

- `<project>-F_Cu.dxf`: copper + outline, gets engraved
- `<project>-Edge_Cuts.dxf`: outline only, gets cut

📸 *Plot dialog with all settings*

> KiCad stores these settings in the `.kicad_pcb`. Next time, `Plot...` → **Plot** is enough.

---

## Part D: Laser job (xTool Studio)

### D1. Create a project and select the device

1. Start xTool Studio (Linux: `xtool-studio` or the start menu).
2. Create a new project.
3. At the top, select the **F2 Ultra** device and connect it (Wi-Fi or USB).

📸 *xTool Studio, empty project with F2 Ultra*

### D2. Import the DXF files

1. Click **Import** and choose `<project>-F_Cu.dxf`.
2. Click **Import** again and choose `<project>-Edge_Cuts.dxf`.
3. Place both objects **exactly on top of each other**. Both contain the same outline: compare position and size (X/Y/W/H in the top bar).
4. **Check the scale:** width and height must match the board in KiCad exactly. For the Stiftklavier that is 57.05 × 38.55 mm.

📸 *imported objects on the canvas*

> **Why does the fill work?** The F_Cu DXF is a compound shape (outline + copper areas). xTool fills it with the even-odd rule, which fills exactly the area **between** the tracks, i.e. the copper that has to go.

### D3. Select the material

1. In the parameter panel on the right, under **Material**, select `User-defined material`.
2. Load the saved **Parameter Scheme** for copper ablation. If there is none, enter the values from D4/D5 and store them with `Save as a custom setting`.

### D4. Copper image: Engrave

Click the F_Cu object and set on the right:

| Field | Value |
|---|---|
| Processing type | **Engrave** |
| Laser type | **Fiber IR** |
| Power | 90 % |
| Speed | 2400 mm/s |
| Passes | 10 |
| Lines per cm | 240 |
| Engraving angle | 45° |
| Engraving mode | bidirectional |
| Outline tracing | on |
| Pulse width | 200 ns |
| Frequency | 65 kHz |

📸 *Engrave parameters*

### D5. Outline: Cut

Click the Edge.Cuts object and set on the right:

| Field | Value |
|---|---|
| Processing type | **Cut** |
| Laser type | **Fiber IR** |
| Power | 88 % |
| Speed | 300 mm/s |
| Passes | 160 |
| Z step-down | on, stepwise, 0.1 mm every 10 passes |
| Tabs | on, automatic, number of tabs 2, tab size 0.5 mm |
| Pulse width | 30 ns |
| Frequency | 130 kHz |

📸 *Cut parameters*

### D6. Place the board, focus, run framing *(at the machine)*

1. Lay the FR4 sheet flat with the copper side up and fix it in place.
2. Set the focus (autofocus or material thickness measurement).
3. Click **Framing**: the laser traces the outline with the pilot light. Check the position.
4. Switch the extraction **on**.

### D7. Start the job *(at the machine)*

1. Click **Start processing**. The processing path is automatic: **engrave first, then cut**.
2. Keep the lid closed and never leave the laser unattended.
3. When it finishes, let the extraction run on before opening.
4. Break the board out at the 2 tabs.

### D8. Save the project

1. Choose `Save as` and save the `.xs` next to the DXF files in `cam/`.

---

## Part E: Post-processing

Continue with [Post-processing](05-post-processing.md): clean, test continuity, drill and assemble.

---

**Automatic path:** Part C (export) can be done entirely by GitHub Actions. See [Automatic path](09-guide-automatic.md).
