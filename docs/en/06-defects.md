# Common Defects

🇩🇪 [Deutsch](../de/06-fehlerbilder.md) · [← Overview](../../README.md)

| Defect | Possible cause | Fix |
|---|---|---|
| Copper residue between tracks | too little power / too few passes, wrong focus | repeat pass, check focus |
| Substrate burnt / dark | too much power, too many passes | reduce power |
| Track interrupted | track too thin, copper removed | track width ≥ 0.4 mm, check edge parameters |
| Bridges between pads | clearance too small, incomplete fill | check clearance, adjust fill pattern/line spacing |
| Image shifted/distorted | board not flat, wrong scale | fix board in place, verify scale after import |
| Top and bottom misaligned | alignment when flipping | use registration marks / a fixed stop |
| Copper lifts when soldering | heat, missing teardrops | teardrops, lower iron temperature |

> **TODO:** add a photo (`images/fehler-*.jpg`) and the actual parameters used for each defect.
