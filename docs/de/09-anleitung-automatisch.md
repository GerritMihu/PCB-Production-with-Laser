# Automatischer Weg: Export per KiBot und GitHub Actions

🇬🇧 [English](../en/09-guide-automatic.md) · [← Übersicht](../../README.de.md)

Statt in KiCad von Hand zu plotten ([Teil C der manuellen Anleitung](08-anleitung-manuell.md#teil-c-export-für-den-laser-kicad)) erzeugt **KiBot** bei jedem `git push` automatisch alle Laser-Dateien. Die Einstellungen sind dieselben wie beim manuellen DXF-Export.

```
git push ──► GitHub Actions ──► KiBot (KiCad 10) ──► laser/dxf, laser/svg, laser/gerber
                                                        │
                                       Commit ins Repo + Download als Artefakt
```

## Was erzeugt wird

Config: [`kibot/laser.kibot.yaml`](../../kibot/laser.kibot.yaml)

| Ordner | Datei | Verwendung |
|---|---|---|
| `laser/dxf/` | `<projekt>-F_Cu.dxf`, `<projekt>-B_Cu.dxf` | Kupfer + Umriss → xTool **Gravieren** |
| `laser/dxf/` | `<projekt>-Edge_Cuts.dxf` | Umriss → xTool **Schnitt** |
| `laser/svg/` | `<projekt>-F_Cu.svg`, `<projekt>-B_Cu.svg` (gespiegelt) | Alternative zum DXF, auf die Platinengröße beschnitten |
| `laser/gerber/` | Gerber + Bohrdatei + Bohrplan (PDF) | Archiv / andere Maschinen |

Beispiel-Ausgabe: [`examples/schnupperblinki/laser/`](../../examples/schnupperblinki/laser/)

## Einrichten im eigenen Projekt-Repo

### 1. Dateien kopieren

Aus diesem Repo ins eigene KiCad-Projekt-Repo kopieren:

```bash
cp "PCB-Production with Laser/kibot/laser.kibot.yaml" mein-projekt/
mkdir -p mein-projekt/.github/workflows
```

### 2. Workflow anlegen

Datei `mein-projekt/.github/workflows/laser.yml`:

```yaml
name: Laser-Export

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
      - name: KiBot Laser-Export
        run: kibot -c laser.kibot.yaml -d laser
      - uses: actions/upload-artifact@v4
        with:
          name: laser-export
          path: laser/
      - name: Exporte committen
        run: |
          git config --global --add safe.directory "$GITHUB_WORKSPACE"
          git config --global user.name "GitHub Actions"
          git config --global user.email "actions@github.com"
          git add -f laser/
          git commit -m "Automatischer Laser-Export (KiBot)" || exit 0
          git push
```

> ⚠️ Das Image heißt **`ghcr.io/inti-cmnb/kicad10_auto_full`**. Der früher verwendete Name `kibot-docker:kicad-10` existiert nicht, der Workflow schlägt damit schon beim Container-Start fehl.

### 3. Pushen

```bash
git add laser.kibot.yaml .github/workflows/laser.yml
git commit -m "Laser-Export per KiBot einrichten"
git push
```

### 4. Ergebnis holen

**Variante A:** `git pull`. Danach liegen die Dateien im Ordner `laser/`.

**Variante B (ohne Git):**
1. Auf GitHub das Repo öffnen und oben auf **Actions** klicken.
2. Den letzten Lauf **Laser-Export** anklicken.
3. Unten unter **Artifacts** auf **laser-export** klicken. Eine ZIP-Datei wird heruntergeladen.

📸 *GitHub Actions: erfolgreicher Lauf mit Artefakt*

### 5. Weiter in xTool Studio

Ab hier wie in der manuellen Anleitung, [Teil D](08-anleitung-manuell.md#teil-d-laser-job-xtool-studio). Statt `cam/` die Dateien aus `laser/dxf/` importieren.

## Lokal ausführen (ohne GitHub)

Mit Docker:

```bash
docker run --rm -v "$PWD":/work -w /work ghcr.io/inti-cmnb/kicad10_auto_full:1.8.6 kibot -c laser.kibot.yaml -d laser
```

> Die per pipx installierte KiBot-Version funktioniert nicht mit der Flatpak-Version von KiCad, weil die Python-Module von KiCad (`pcbnew`) fehlen. Deshalb den Docker-Container verwenden.

## Unterschiede zum manuellen Export

| | Manuell (KiCad) | KiBot |
|---|---|---|
| DXF-Lagennamen | `F.Cu` | `BLACK` / `WHITE` (Kupfer / Bohrmarken) |
| Rest | identisch: Polygonmodus, mm, kleine Bohrmarken, Umriss auf jeder Lage | |

> **TODO:** Testen, ob xTool Studio die KiBot-DXF genauso füllt wie die manuelle DXF. Am Freitag an der Maschine prüfen.

## Ausbauideen

- **DRC als Prüfung vor dem Export:** KiBot bricht ab, wenn die Platine die Laser-Design-Regeln verletzt (`preflight: run_drc: true`).
- **xTool-Projekt automatisch erzeugen:** Das `.xs`-Format ist ein ZIP mit JSON-Dateien. Ein Skript könnte die DXF und die Parameter direkt in eine fertige `.xs` packen, dann muss in xTool Studio nur noch geöffnet und gestartet werden.
