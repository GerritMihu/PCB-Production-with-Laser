# Export: KiCad → Laser

🇬🇧 [English](../en/04-export.md) · [← Übersicht](../../README.de.md)

Für den Laser werden nur **Kupferlagen, Umriss und Bohrungen** gebraucht. Lötstopplack und Bestückungsdruck werden weggelassen.

## Variante A: KiBot (empfohlen)

Die Config `kibot/laser.kibot.yaml` erzeugt:

| Ausgabe | Datei(en) | Verwendung |
|---|---|---|
| Gerber | `laser/gerber/*-F_Cu.gbr`, `*-B_Cu.gbr`, `*-Edge_Cuts.gbr` | Archiv / andere Maschinen |
| Bohrdaten | `laser/gerber/*.drl` + Bohrplan-PDF | Bohren |
| SVG oben | `laser/svg/*-F_Cu.svg` | Import in Laser-Software |
| SVG unten | `laser/svg/*-B_Cu.svg` (**gespiegelt**) | Import in Laser-Software |
| SVG Umriss | `laser/svg/*-Edge_Cuts.svg` | Konturschnitt / Ausrichtung |

**Lokal:**

```bash
kibot -c "/pfad/zu/PCB-Production with Laser/kibot/laser.kibot.yaml" -b MeinBoard.kicad_pcb -d laser/
```

**In GitHub Actions** (wie in den anderen Repos mit dem KiCad-10-Container): Config ins Projekt-Repo kopieren und im Workflow aufrufen:

```yaml
- name: Laser-Export
  run: kibot -c laser.kibot.yaml -d cam/
```

## Variante B: manuell in KiCad

1. Leiterplatteneditor → *Datei → Plotten*
2. Format **SVG**, Lagen `F.Cu` (+ `Edge.Cuts`), Maßstab 1:1
3. Für `B.Cu`: **Gespiegelt plotten** aktivieren
4. *Bohrmarken: Tatsächliche Größe* – hilft beim Bohren nach dem Lasern

## Hinweise

- **Unterseite spiegeln:** Die Platine wird zum Lasern der Unterseite umgedreht, daher muss das Bild gespiegelt sein.
- **Positiv/Negativ:** Je nach Laser-Software muss die Fläche *zwischen* den Leiterbahnen gefüllt werden. Wie das umgesetzt wird, steht maschinenspezifisch in `machines/<maschine>/`.
- **Maßstab prüfen:** Nach dem Import ein bekanntes Maß (z. B. Platinenbreite) in der Laser-Software kontrollieren.
