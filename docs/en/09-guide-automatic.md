# Automatic Path: Export with KiBot and GitHub Actions

🇩🇪 [Deutsch](../de/09-anleitung-automatisch.md) · [← Overview](../../README.md)

Instead of plotting by hand in KiCad ([Part C of the manual guide](08-guide-manual.md#part-c-export-for-the-laser-kicad)), **KiBot** generates all laser files automatically on every `git push`. The settings are the same as for the manual DXF export.

```
git push ──► GitHub Actions ──► KiBot (KiCad 10) ──► laser/dxf, laser/svg, laser/gerber
                                                        │
                                       commit to repo + download as artifact
```

## What is generated

Config: [`kibot/laser.kibot.yaml`](../../kibot/laser.kibot.yaml)

| Folder | File | Use |
|---|---|---|
| `laser/dxf/` | `<project>-F_Cu.dxf`, `<project>-B_Cu.dxf` | copper + outline → xTool **Engrave** |
| `laser/dxf/` | `<project>-Edge_Cuts.dxf` | outline → xTool **Cut** |
| `laser/svg/` | `<project>-F_Cu.svg`, `<project>-B_Cu.svg` (mirrored) | alternative to DXF, cropped to board size |
| `laser/gerber/` | Gerber + drill file + drill map (PDF) | archive / other machines |

Example output: [`examples/schnupperblinki/laser/`](../../examples/schnupperblinki/laser/)

## Setting it up in your own project repo

### 1. Copy the config

Copy from this repo into your own KiCad project repo:

```bash
cp "PCB-Production with Laser/kibot/laser.kibot.yaml" my-project/
mkdir -p my-project/.github/workflows
```

### 2. Create the workflow

File `my-project/.github/workflows/laser.yml`:

```yaml
name: Laser export

on:
  push:
    paths: ['**.kicad_pcb', 'laser.kibot.yaml']
  workflow_dispatch:

permissions:
  contents: write

jobs:
  laser:
    runs-on: ubuntu-latest
    container:
      image: ghcr.io/inti-cmnb/kicad10_auto_full:1.8.6
    steps:
      - uses: actions/checkout@v4
      - name: KiBot laser export
        run: kibot -c laser.kibot.yaml -d laser
      - uses: actions/upload-artifact@v4
        with:
          name: laser-export
          path: laser/
      - name: Commit exports
        run: |
          git config --global --add safe.directory "$GITHUB_WORKSPACE"
          git config --global user.name "GitHub Actions"
          git config --global user.email "actions@github.com"
          git add -f laser/
          git commit -m "Automatic laser export (KiBot)" || exit 0
          git push
```

> ⚠️ The image is called **`ghcr.io/inti-cmnb/kicad10_auto_full`**. The name used earlier, `kibot-docker:kicad-10`, does not exist, so a workflow using it fails as soon as the container starts.

### 3. Push

```bash
git add laser.kibot.yaml .github/workflows/laser.yml
git commit -m "Set up laser export with KiBot"
git push
```

### 4. Get the result

**Option A:** run `git pull`. The files are then in the `laser/` folder.

**Option B (without Git):**
1. Open the repo on GitHub and click **Actions** at the top.
2. Click the latest **Laser export** run.
3. Under **Artifacts** at the bottom, click **laser-export**. A ZIP file downloads.

📸 *GitHub Actions: successful run with artifact*

### 5. Continue in xTool Studio

From here, follow [Part D](08-guide-manual.md#part-d-laser-job-xtool-studio) of the manual guide. Import the files from `laser/dxf/` instead of `cam/`.

## Running locally (without GitHub)

With Docker:

```bash
docker run --rm -v "$PWD":/work -w /work ghcr.io/inti-cmnb/kicad10_auto_full:1.8.6 kibot -c laser.kibot.yaml -d laser
```

> A pipx-installed KiBot does not work with the Flatpak version of KiCad, because KiCad's Python modules (`pcbnew`) are missing. Use the Docker container instead.

## Differences from the manual export

| | Manual (KiCad) | KiBot |
|---|---|---|
| DXF layer names | `F.Cu` | `BLACK` / `WHITE` (copper / drill marks) |
| Everything else | identical: polygon mode, mm, small drill marks, outline on every layer | |

> **TODO:** test whether xTool Studio fills the KiBot DXF the same way as the manual DXF. Check at the machine on Friday.

## Ideas for later

- **DRC as a check before export:** KiBot aborts if the board violates the laser design rules (`preflight: run_drc: true`).
- **Generate the xTool project automatically:** the `.xs` format is a ZIP of JSON files. A script could pack the DXF and the parameters straight into a ready-made `.xs`, so xTool Studio only has to open it and start the job.
