# xTool F2 Ultra

🇬🇧 [English](README.md) · [← Übersicht](../../README.de.md)

## Maschinendaten

| | |
|---|---|
| Gerät (laut xTool Studio) | F2 Ultra, Gerätecode `GS004-CLASS-4` |
| Laserquellen | 60 W MOPA-Faserlaser (*Faser-IR*) + 40 W Diodenlaser (*Blaues Licht*) |
| Ablenkung | Galvo |
| Laserklasse | TODO (Typenschild) |
| Anbindung | USB / WLAN |
| Software | xTool Studio (Windows/macOS), Linux: [siehe Test](software-linux.de.md) |
| Standort | TODO |

## Design-Regeln

Siehe [Design-Regeln](../../docs/de/03-design-regeln.md) – KiCad-Vorlage `Laser_PCB_xTool`.

## Laser-Parameter (Stand 07/2026)

**Quelle:** xTool-Projekt [`presets/stiftklavier-F_Cu.xs`](presets/stiftklavier-F_Cu.xs) vom 02.07.2026 (Stiftklavier, einseitig). Die Werte wurden direkt aus der Projektdatei ausgelesen.

![Vorschau des xTool-Projekts](../../images/xtool/stiftklavier-xs-vorschau.png)

Das Projekt enthält **zwei Objekte**:

| Objekt | Herkunft | Bearbeitungsart |
|---|---|---|
| Kupferbild + Umriss (gefüllte Verbundform) | `…-F_Cu.dxf` | **Gravieren** (Füllung): trägt das Kupfer zwischen den Leiterbahnen ab |
| Platinenumriss | `…-Edge_Cuts.dxf` | **Schnitt**: schneidet die Platine aus dem FR4 |

### 1. Kupfer abtragen: Gravieren (Füllung)

| Parameter (xTool Studio) | Wert |
|---|---|
| Material | Benutzerdefiniertes Material (gespeichertes Parameter-Schema) |
| Laserart | **Faser-IR** |
| Leistung | **90 %** |
| Geschwindigkeit | **2400 mm/s** |
| Bearbeitungsanzahl (Durchgänge) | **10** |
| Linien pro cm | **240** (≈ 0,042 mm Linienabstand) |
| Gravurwinkel | **45°** |
| Gravurmodus | Bidirektional (Z-Modus) |
| Konturverfolgung | **ein** |
| Impulsbreite | **200 ns** |
| Frequenz | **65 kHz** |
| Defokus | aus |
| Schnittfugenkompensation | aus |

### 2. Platine ausschneiden: Schnitt

| Parameter (xTool Studio) | Wert |
|---|---|
| Laserart | **Faser-IR** |
| Leistung | **88 %** |
| Geschwindigkeit | **300 mm/s** |
| Bearbeitungsanzahl (Durchgänge) | **160** |
| Z-Absenkung | ein, schrittweise: **0,1 mm alle 10 Durchgänge** |
| Tabs (Haltestege) | ein, automatisch: **2 Stück, 0,5 mm** |
| Impulsbreite | **30 ns** |
| Frequenz | **130 kHz** |
| Flattern (Wobble) | aus |
| Schnittfugenkompensation | aus |

### Projekt-Einstellungen

| Einstellung | Wert |
|---|---|
| Bearbeitungsweg | automatisch: zuerst gravieren, dann schneiden |
| Scanrichtung | von oben nach unten |

> **TODO:** Kupferstärke und Plattendicke des verwendeten FR4 ergänzen. Erst damit sind die Werte auf andere Platten übertragbar.
> **TODO:** Doppelseitige Platinen sind noch nicht getestet (Ausrichtung beim Umdrehen).

Weitere Projektdateien bzw. Materialvorlagen unter [`presets/`](presets/) ablegen.

## Ablauf

Die vollständige Anleitung mit jedem einzelnen Klick: [Manueller Weg: KiCad → xTool](../../docs/de/08-anleitung-manuell.md).

## Lötstopplack

Stand 07/2026: **noch kein funktionierendes Verfahren.** Versuche hier dokumentieren.

| Datum | Versuch | Ergebnis |
|---|---|---|
| | | |
