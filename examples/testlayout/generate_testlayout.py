#!/usr/bin/env python3
"""Erzeugt testlayout.kicad_pcb: Testplatine zum Vergleich der Fertigungsverfahren
(Laser-Ablation, Laser-Maske + Ätzen, Isolationsfräsen, Ätzen).

Aufruf: python3 generate_testlayout.py  (schreibt testlayout.kicad_pcb + .kicad_pro daneben)
"""
import json
import re
import uuid
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
TEMPLATE = REPO / "kicad/template/Laser_PCB_xTool"
FP_LIB = Path("/usr/share/kicad/footprints")
VERSION = "v1.0"

WIDTHS = [0.10, 0.15, 0.20, 0.30, 0.40, 0.50]
GAPS = [0.10, 0.15, 0.20, 0.30, 0.40, 0.50]
COMB_W = 0.4
COMB_L = 6.0
TRACK_LEN = 30.0
TESTPAD = 1.6
THT = [(0.6, 1.2), (0.8, 1.6), (1.0, 2.0), (1.2, 2.4)]
TEXT_SIZES = [1.0, 1.5, 2.0]
SMD = [
    ("Resistor_SMD", "R_0603_1608Metric", "0603"),
    ("Resistor_SMD", "R_0805_2012Metric", "0805"),
    ("Resistor_SMD", "R_1206_3216Metric", "1206"),
    ("Package_TO_SOT_SMD", "SOT-23", "SOT23"),
    ("Package_SO", "SOIC-8_3.9x4.9mm_P1.27mm", "SO8"),
    ("Package_SO", "TSSOP-14_4.4x5mm_P0.65mm", "TSSOP"),
]

X0, Y0, BW, BH = 100.0, 50.0, 100.0, 80.0

nets = [""]
items = []
ref_counter = {}


def uid():
    return str(uuid.uuid4())


def net(name):
    if name not in nets:
        nets.append(name)
    return nets.index(name)


def ref(prefix):
    ref_counter[prefix] = ref_counter.get(prefix, 0) + 1
    return f"{prefix}{ref_counter[prefix]}"


def fmt(v):
    return f"{v:.4f}".rstrip("0").rstrip(".")


def segment(x1, y1, x2, y2, w, netname):
    items.append(
        f'\t(segment\n\t\t(start {fmt(x1)} {fmt(y1)})\n\t\t(end {fmt(x2)} {fmt(y2)})\n'
        f'\t\t(width {fmt(w)})\n\t\t(layer "F.Cu")\n\t\t(net {net(netname)})\n\t\t(uuid "{uid()}")\n\t)'
    )


def text(s, x, y, size, layer="F.Cu", justify=None):
    thick = max(0.15, round(size * 0.15, 2))
    j = f"\n\t\t\t(justify {justify})" if justify else ""
    items.append(
        f'\t(gr_text "{s}"\n\t\t(at {fmt(x)} {fmt(y)} 0)\n\t\t(layer "{layer}")\n\t\t(uuid "{uid()}")\n'
        f'\t\t(effects\n\t\t\t(font\n\t\t\t\t(size {fmt(size)} {fmt(size)})\n\t\t\t\t(thickness {fmt(thick)})\n\t\t\t){j}\n\t\t)\n\t)'
    )


def edge_line(x1, y1, x2, y2):
    items.append(
        f'\t(gr_line\n\t\t(start {fmt(x1)} {fmt(y1)})\n\t\t(end {fmt(x2)} {fmt(y2)})\n'
        f'\t\t(stroke\n\t\t\t(width 0.05)\n\t\t\t(type default)\n\t\t)\n\t\t(layer "Edge.Cuts")\n\t\t(uuid "{uid()}")\n\t)'
    )


def fp_props(reference, value):
    out = []
    for name, val, dy in (("Reference", reference, -2), ("Value", value, 2)):
        out.append(
            f'\t\t(property "{name}" "{val}"\n\t\t\t(at 0 {dy} 0)\n\t\t\t(layer "F.Fab")\n\t\t\t(hide yes)\n'
            f'\t\t\t(uuid "{uid()}")\n\t\t\t(effects\n\t\t\t\t(font\n\t\t\t\t\t(size 0.8 0.8)\n'
            f'\t\t\t\t\t(thickness 0.12)\n\t\t\t\t)\n\t\t\t)\n\t\t)'
        )
    return "\n".join(out)


def testpad(x, y, netname):
    items.append(
        f'\t(footprint "Testlayout:Testpad_{TESTPAD}mm"\n\t\t(layer "F.Cu")\n\t\t(uuid "{uid()}")\n'
        f'\t\t(at {fmt(x)} {fmt(y)})\n{fp_props(ref("TP"), "Testpad")}\n\t\t(attr smd)\n'
        f'\t\t(pad "1" smd rect\n\t\t\t(at 0 0)\n\t\t\t(size {TESTPAD} {TESTPAD})\n'
        f'\t\t\t(layers "F.Cu" "F.Mask")\n\t\t\t(net {net(netname)} "{netname}")\n\t\t\t(uuid "{uid()}")\n\t\t)\n'
        f'\t\t(embedded_fonts no)\n\t)'
    )


def tht_group(x, y, drill, pad, count=3, pitch=3.0):
    pads = []
    for i in range(count):
        pads.append(
            f'\t\t(pad "{i + 1}" thru_hole circle\n\t\t\t(at {fmt(i * pitch)} 0)\n\t\t\t(size {fmt(pad)} {fmt(pad)})\n'
            f'\t\t\t(drill {fmt(drill)})\n\t\t\t(layers "*.Cu" "*.Mask")\n\t\t\t(remove_unused_layers no)\n'
            f'\t\t\t(uuid "{uid()}")\n\t\t)'
        )
    items.append(
        f'\t(footprint "Testlayout:THT_D{fmt(drill)}_P{fmt(pad)}"\n\t\t(layer "F.Cu")\n\t\t(uuid "{uid()}")\n'
        f'\t\t(at {fmt(x)} {fmt(y)})\n{fp_props(ref("H"), f"Bohrung {fmt(drill)} / Pad {fmt(pad)}")}\n'
        f'\t\t(attr through_hole)\n' + "\n".join(pads) + "\n\t\t(embedded_fonts no)\n\t)"
    )


def library_fp(lib, name, x, y):
    src = (FP_LIB / f"{lib}.pretty" / f"{name}.kicad_mod").read_text()
    src = re.sub(r'^\(footprint "[^"]+"', f'(footprint "{lib}:{name}"', src, count=1)
    src = re.sub(r'\n\t\((version|generator|generator_version) [^\n]*\)', "", src)
    src = src.replace('\n\t(layer "F.Cu")', f'\n\t(layer "F.Cu")\n\t(uuid "{uid()}")\n\t(at {fmt(x)} {fmt(y)})', 1)
    src = re.sub(r'\(property "Reference" "REF\*\*"', f'(property "Reference" "{ref("U")}"', src)
    items.append("\n".join("\t" + line for line in src.strip().splitlines()))


# Platinenumriss
edge_line(X0, Y0, X0 + BW, Y0)
edge_line(X0 + BW, Y0, X0 + BW, Y0 + BH)
edge_line(X0 + BW, Y0 + BH, X0, Y0 + BH)
edge_line(X0, Y0 + BH, X0, Y0)

text(f"Testlayout Fertigungsverfahren {VERSION}", 103, 53.5, 1.5, justify="left")

# A: Leiterbahnbreite – Durchgangsprüfung zwischen zwei Testpads
text("Leiterbahn (mm)", 103, 57, 1.2, justify="left")
for i, w in enumerate(WIDTHS):
    y = 61 + 4 * i
    n = f"BAHN_{int(round(w * 100)):03d}"
    text(f"{w:.2f}", 106, y, 1.2)
    xa, xb = 113.0, 113.0 + TRACK_LEN
    testpad(xa, y, n)
    testpad(xb, y, n)
    segment(xa, y, xb, y, w, n)

# B: Isolationsabstand – Kammstruktur, A und B dürfen keine Verbindung haben
text("Abstand (mm)", 152, 57, 1.2, justify="left")
for i, g in enumerate(GAPS):
    x0 = 155.0 + 15.0 * (i % 3)
    top = 62.0 + 14.0 * (i // 3)
    w = COMB_W
    p = 2 * (w + g)
    na, nb = (f"KAMM_{int(round(g * 100)):03d}_{s}" for s in "AB")
    y_b = top + COMB_L + w + g
    text(f"{g:.2f}", x0 + 1.75 * p, top - 2.2, 1.2)
    pad_a, pad_b = x0 - 2.5, x0 + 3.5 * p + 2.5
    testpad(pad_a, top, na)
    testpad(pad_b, y_b, nb)
    segment(pad_a, top, x0 + 3 * p, top, w, na)
    segment(x0 + 0.5 * p, y_b, pad_b, y_b, w, nb)
    for k in range(4):
        xa = x0 + k * p
        segment(xa, top, xa, top + COMB_L, w, na)
        segment(xa + 0.5 * p, y_b, xa + 0.5 * p, top + w + g, w, nb)

# C: SMD-Footprints aus der KiCad-Standardbibliothek
text("SMD", 103, 88, 1.2, justify="left")
for (lib, name, label), x in zip(SMD, (106, 115, 125, 135, 148, 163)):
    library_fp(lib, name, x, 95)
    text(label, x, 101.5, 1.2)

# D: Bohrungen / Lötaugen
text("THT Bohrung/Pad (mm)", 103, 106, 1.2, justify="left")
for (drill, pad), x in zip(THT, (104.5, 117.5, 130.5, 143.5)):
    tht_group(x, 111, drill, pad)
    text(f"{drill:.1f}/{pad:.1f}", x + 3, 115.5, 1.0)

# E: Textgrößen in Kupfer
for size, y in zip(TEXT_SIZES, (106, 110, 115)):
    text(f"Text {size:.1f} mm", 158, y, size, justify="left")

# F: Maßstäbe zur Prüfung der Maßhaltigkeit (X und Y)
segment(103, 125, 153, 125, 0.4, "")
for k in range(6):
    segment(103 + 10 * k, 125, 103 + 10 * k, 123, 0.4, "")
text("50 mm", 158, 125, 1.2, justify="left")
segment(196, 100, 196, 120, 0.4, "")
for k in range(5):
    segment(196, 100 + 5 * k, 194, 100 + 5 * k, 0.4, "")
text("20 mm", 186, 122.5, 1.2, justify="left")

# Board schreiben (Header aus der Vorlage, damit Lagen/Stackup identisch sind)
tpl = (TEMPLATE / "Laser_PCB_xTool.kicad_pcb").read_text()
head = tpl[: tpl.index('\t(net 0 "")')]
net_decl = "\n".join(f'\t(net {i} "{n}")' for i, n in enumerate(nets))
(HERE / "testlayout.kicad_pcb").write_text(
    head + net_decl + "\n" + "\n".join(items) + "\n\t(embedded_fonts no)\n)\n"
)

# Projekt: Regeln der Vorlage, aber Mindestwerte gesenkt, damit die Teststrukturen DRC-sauber sind
pro = json.loads((TEMPLATE / "Laser_PCB_xTool.kicad_pro").read_text())
rules = pro["board"]["design_settings"]["rules"]
rules["min_track_width"] = min(WIDTHS)
rules["min_clearance"] = min(GAPS)
rules["min_through_hole_diameter"] = min(d for d, _ in THT)
rules["min_via_annular_width"] = 0.1
for nc in pro["net_settings"]["classes"]:
    nc["clearance"] = min(GAPS)
sev = pro["board"]["design_settings"]["rule_severities"]
for key in ("track_dangling", "lib_footprint_issues", "lib_footprint_mismatch"):
    sev[key] = "ignore"  # offene Kammfinger/Maßstabstriche sind gewollt, Footprints stammen aus der Systembibliothek
pro["meta"]["filename"] = "testlayout.kicad_pro"
(HERE / "testlayout.kicad_pro").write_text(json.dumps(pro, indent=2) + "\n")
print(f"{len(items)} Elemente, {len(nets) - 1} Netze geschrieben")
