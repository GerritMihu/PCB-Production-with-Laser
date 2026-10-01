# Export: KiCad → Laser

🇬🇧 [English](../en/04-export.md) · [← Übersicht](../../README.de.md)

Für den Laser werden nur **Kupferlagen, Umriss und Bohrmarken** gebraucht. Lötstopplack und Bestückungsdruck werden weggelassen.

**Bewährtes Format für xTool Studio: DXF**, mit dem Umriss in jeder Kupfer-DXF. xTool füllt die Verbundform so, dass genau das Kupfer zwischen den Leiterbahnen abgetragen wird.

| Weg | Anleitung |
|---|---|
| Manuell in KiCad (Plotten → DXF) | [Manueller Weg, Teil C](08-anleitung-manuell.md#teil-c-export-für-den-laser-kicad) |
| Automatisch per KiBot / GitHub Actions | [Automatischer Weg](09-anleitung-automatisch.md) |

## Die wichtigsten Einstellungen

| Einstellung | Wert | Warum |
|---|---|---|
| Plotformat | DXF | Import in xTool Studio als Vektor |
| Auf allen Lagen plotten | `Edge.Cuts` | Umriss + Kupfer = Verbundform, die gefüllt werden kann |
| Bohrlochmarkierungen | klein | Zentrierpunkt zum Bohren bleibt kupferfrei |
| Konturen (Polygonmodus) | ein | Flächen statt Mittellinien |
| Einheit | Millimeter | kein Umrechnungsfehler |

## Hinweise

- **Unterseite (B.Cu):** Die Platine wird umgedreht, daher muss das Bild gespiegelt werden, entweder in xTool Studio oder als gespiegeltes SVG (KiBot).
- **Maßstab prüfen:** Nach dem Import die Platinenbreite in xTool Studio kontrollieren.
- **SVG** geht als Alternative auch (KiBot erzeugt es auf die Platine beschnitten), ist aber noch nicht an der Maschine getestet.
