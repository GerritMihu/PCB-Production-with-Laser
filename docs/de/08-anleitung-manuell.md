# Manueller Weg: vom KiCad-Schaltplan zur gelaserten Platine

🇬🇧 [English](../en/08-guide-manual.md) · [← Übersicht](../../README.de.md)

Diese Anleitung beschreibt **jeden einzelnen Klick**, von der leeren KiCad-Vorlage bis zur ausgeschnittenen Platine im xTool F2 Ultra.

- **Software:** KiCad 10 (deutsche Oberfläche), xTool Studio 1.9.11
- **Beispiel:** [Schnupperblinki](../../examples/schnupperblinki/)
- **Parameter:** [xTool F2 Ultra](../../machines/xtool-f2-ultra/README.de.md#laser-parameter-stand-072026)

> **Schreibweise:** `Menü → Eintrag` heißt: auf *Menü* klicken, dann auf *Eintrag*. Alle Menü- und Feldnamen stehen genau so da, wie sie in der Software erscheinen.
> 📸 markiert Stellen, an denen noch ein Screenshot eingefügt wird.

---

## Teil A: Schaltplan (KiCad)

### A1. Projekt aus der Laser-Vorlage anlegen

Einmalig vorher: Vorlagenpfad einrichten, siehe [Design-Regeln](03-design-regeln.md#kicad-vorlage-verwenden).

1. KiCad starten.
2. `Datei → Neues Projekt ...` anklicken. Das Fenster **Projektvorlagenauswahl** öffnet sich.
3. Den Reiter mit den Benutzervorlagen wählen und **Laser_PCB_xTool** anklicken.
4. **OK** klicken.
5. Speicherort wählen, Projektnamen eingeben (z. B. `blinker`) und **Speichern** klicken.

📸 *Projektvorlagenauswahl mit Laser_PCB_xTool*

### A2. Schaltplan zeichnen

1. In der Projektverwaltung auf **Schaltplaneditor** klicken (bzw. Doppelklick auf `blinker.kicad_sch`).
2. Bauteile setzen: Taste **A** drücken (Symbol hinzufügen), Bauteil suchen, z. B. `NE555`, und **OK** klicken. Dann zum Platzieren in den Schaltplan klicken.
3. Verbindungen ziehen: Taste **W** drücken (Leitung), am Pin-Ende anklicken, am Ziel-Pin wieder anklicken.
4. Versorgung: Taste **P** drücken und `GND` bzw. `+5V` setzen.
   > Diese Netze landen durch die Vorlage automatisch in der Netzklasse **Power** und werden 0,8 mm breit.

📸 *fertiger Schaltplan*

### A3. Annotieren, Footprints zuweisen, ERC

1. `Werkzeuge → Schaltplan annotieren ...` öffnen, dann **Annotieren** und **Schließen** klicken.
2. `Werkzeuge → Footprints zuweisen ...` öffnen. Jedem Symbol links einen Footprint aus der Liste rechts zuweisen (Doppelklick), dann **OK** klicken.
   > Für Anfänger **THT-Footprints** (bedrahtet) bevorzugen. Die großen Pads sind leichter zu lasern und zu löten.
3. `Inspektion → Elektrische Regeln überprüfen (ERC)` öffnen und **ERC starten** klicken. Es müssen **0 Fehler** sein.
4. Mit **Strg+S** speichern.

📸 *ERC ohne Fehler*

---

## Teil B: Platine (KiCad)

### B1. Platine aus Schaltplan übernehmen

1. Im Schaltplaneditor `Werkzeuge → Platine aus Schaltplan aktualisieren ...` öffnen (oder **F8** drücken).
2. **Platine aktualisieren** klicken, dann **Schließen**.
3. Die Bauteile hängen am Mauszeiger: Zum Ablegen in die Arbeitsfläche klicken.

### B2. Platinenumriss zeichnen

1. Rechts im Lagen-Panel die Lage **Edge.Cuts** anklicken.
2. `Hinzufügen → Rechteck zeichnen` wählen.
3. Ecke oben links anklicken, dann Ecke unten rechts anklicken.
   > Mindestens **1 mm Abstand** zwischen Kupfer und Umriss (prüft der DRC).

### B3. Bauteile platzieren und Leiterbahnen verlegen

1. Bauteile mit der Maus verschieben, mit **R** drehen.
2. Lage **B.Cu** wählen. Einseitig gelasert wird die Kupferseite unten, die Bauteile stecken oben.
   > **TODO:** Seite festlegen. Das Stiftklavier-Projekt wurde auf **F.Cu** gelasert.
3. Taste **X** drücken (Einzelne Leiterbahn routen), am Pad anklicken, am Ziel-Pad wieder anklicken.
   > Die Breite stellt die Netzklasse automatisch ein: Signal 0,4 mm, Power 0,8 mm.

### B4. Massefläche anlegen (spart Laserzeit)

1. `Hinzufügen → Zone hinzufügen` wählen (oder **Strg+Umschalt+Z** drücken).
2. Eine Ecke der Platine anklicken. Im Fenster **Kupferzonen-Eigenschaften** die Kupferlage anhaken, als **Netz:** `GND` wählen und **OK** klicken.
3. Die übrigen Ecken anklicken, mit Doppelklick abschließen.
4. `Bearbeiten → Alle Zonen füllen` wählen (Taste **B**).

### B5. DRC

1. `Inspektion → Designregeln überprüfen (DRC)` öffnen.
2. **DRC starten** klicken. Es müssen **0 Verstöße** sein. Warnungen zu Bibliotheken und Bestückungsdruck sind für den Laser egal.
3. Mit **Strg+S** speichern.

📸 *fertige Platine im Leiterplatteneditor*

---

## Teil C: Export für den Laser (KiCad)

Exportiert wird als **DXF**, genau wie beim bewährten Stiftklavier-Projekt.

1. Im Leiterplatteneditor `Datei → Fertigungsdaten → Plotten ...` öffnen. Je nach Version heißt der Eintrag direkt `Datei → Plotten ...`.
2. Einstellungen im Fenster **Plotten**:

   | Feld | Einstellung |
   |---|---|
   | **Plotformat:** | `DXF` |
   | **Ausgabeverzeichnis:** | `cam/` |
   | **Lagenauswahl** (links) | `F.Cu` (bzw. `B.Cu`) und `Edge.Cuts` anhaken |
   | **Auf allen Lagen plotten** (rechts) | `Edge.Cuts` anhaken: Der Umriss landet so in jeder Kupfer-DXF |
   | **Bohrlochmarkierungen:** | `Kleine Bohrlochmarkierung` (Zentrierpunkt zum Bohren) |
   | **Zeichnungsblatt plotten** | **aus** |
   | **Optionen DXF** → *Plotten grafischer Elemente anhand ihrer Konturen* | **ein** |
   | **Optionen DXF** → *KiCad-Schriftart verwenden, um Text zu plotten* | **ein** |
   | **Optionen DXF** → *Einheit für Export:* | `Millimeter` |

3. **Plotten** klicken.
4. **Schließen** klicken.

**Ergebnis** im Ordner `cam/`:

- `<projekt>-F_Cu.dxf`: Kupfer und Umriss, wird graviert
- `<projekt>-Edge_Cuts.dxf`: nur der Umriss, wird geschnitten

📸 *Plot-Dialog mit allen Einstellungen*

> Die Einstellungen werden in der `.kicad_pcb` gespeichert. Beim nächsten Mal genügt `Plotten ...` → **Plotten**.

---

## Teil D: Laser-Job (xTool Studio)

### D1. Projekt anlegen und Gerät wählen

1. xTool Studio starten (Linux: `xtool-studio` bzw. Startmenü).
2. Ein neues Projekt anlegen.
3. Oben das Gerät **F2 Ultra** auswählen und verbinden (WLAN oder USB).

📸 *xTool Studio, leeres Projekt mit F2 Ultra*

### D2. DXF-Dateien importieren

1. **Importieren** klicken und `<projekt>-F_Cu.dxf` wählen.
2. Noch einmal **Importieren** klicken und `<projekt>-Edge_Cuts.dxf` wählen.
3. Beide Objekte **deckungsgleich** übereinanderlegen. Beide enthalten denselben Umriss: Lage und Größe vergleichen (X/Y/B/H oben in der Leiste).
4. **Maßstab prüfen:** Breite und Höhe müssen genau der Platine in KiCad entsprechen. Beim Stiftklavier sind das 57,05 × 38,55 mm.

📸 *importierte Objekte auf der Arbeitsfläche*

> **Warum klappt die Füllung?** Die F_Cu-DXF ist eine Verbundform (Umriss + Kupferflächen). xTool füllt nach der Gerade/Ungerade-Regel und füllt damit genau die Fläche **zwischen** den Leiterbahnen, also das Kupfer, das weg soll.

### D3. Material wählen

1. Rechts im Parameterbereich unter **Material** `Benutzerdefiniertes Material` wählen.
2. Gespeichertes **Parameter-Schema** für Kupfer-Ablation laden. Falls keines vorhanden ist, die Werte aus D4/D5 eintragen und über `Als benutzerdefinierte Einstellung speichern` sichern.

### D4. Kupferbild: Gravieren

Das F_Cu-Objekt anklicken und rechts einstellen:

| Feld | Wert |
|---|---|
| Bearbeitungsart | **Gravieren** |
| Laserart | **Faser-IR** |
| Leistung | 90 % |
| Geschwindigkeit | 2400 mm/s |
| Bearbeitungsanzahl | 10 |
| Linien pro cm | 240 |
| Gravurwinkel | 45° |
| Gravurmodus | Bidirektional |
| Konturverfolgung | ein |
| Impulsbreite | 200 ns |
| Frequenz | 65 kHz |

📸 *Parameter Gravieren*

### D5. Umriss: Schnitt

Das Edge.Cuts-Objekt anklicken und rechts einstellen:

| Feld | Wert |
|---|---|
| Bearbeitungsart | **Schnitt** |
| Laserart | **Faser-IR** |
| Leistung | 88 % |
| Geschwindigkeit | 300 mm/s |
| Bearbeitungsanzahl | 160 |
| Z-Absenkung | ein, schrittweise, 0,1 mm, alle 10 Durchgänge |
| Tabs | ein, automatisch, Anzahl der Tabs 2, Tab-Größe 0,5 mm |
| Impulsbreite | 30 ns |
| Frequenz | 130 kHz |

📸 *Parameter Schnitt*

### D6. Platine einlegen, fokussieren, Rahmen fahren *(an der Maschine)*

1. FR4-Platte mit der Kupferseite nach oben flach einlegen und fixieren.
2. Fokus einstellen (Autofokus bzw. Messung der Materialstärke).
3. **Rahmen** klicken: Der Laser fährt den Umriss mit dem Pilotlicht ab. Die Position kontrollieren.
4. Absaugung **einschalten**.

### D7. Job starten *(an der Maschine)*

1. **Bearbeitung starten** klicken. Der Bearbeitungsweg ist automatisch: **zuerst gravieren, dann schneiden**.
2. Deckel geschlossen lassen, Laser nicht unbeaufsichtigt lassen.
3. Nach dem Ende die Absaugung nachlaufen lassen und erst dann öffnen.
4. Platine an den 2 Tabs herausbrechen.

### D8. Projekt speichern

1. `Speichern unter` wählen und als `.xs` neben die DXF-Dateien in `cam/` speichern.

---

## Teil E: Nachbearbeitung

Weiter mit [Nachbearbeitung](05-nachbearbeitung.md): reinigen, Durchgang prüfen, bohren und bestücken.

---

**Automatischer Weg:** Teil C (Export) lässt sich komplett von GitHub Actions erledigen. Siehe [Automatischer Weg](09-anleitung-automatisch.md).
