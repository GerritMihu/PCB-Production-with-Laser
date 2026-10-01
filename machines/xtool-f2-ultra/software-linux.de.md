# xTool Studio unter Linux

🇬🇧 [English](software-linux.md) · [← xTool F2 Ultra](README.de.md)

## Ausgangslage (Recherche 10/2026)

- xTool bietet xTool Studio und xTool Creative Space **nur für Windows und macOS** an. Es gibt keine offizielle Linux-Version ([xTool Support](https://support.xtool.com/article/2405), [Systemanforderungen](https://support.xtool.com/article/671)).
- **LightBurn ist keine Alternative:** Der F2 Ultra nutzt ein proprietäres Protokoll und wird nur über xTool Studio angesteuert ([LightBurn-Forum](https://forum.lightburnsoftware.com/t/unable-to-connect-lightburn-with-xtool-f2-ultra/183981)). LightBurn taugt höchstens als Design-Tool mit SVG-Export.
- **Community-Projekt** [gregmatthewcrossley/xtool-studio-linux](https://github.com/gregmatthewcrossley/xtool-studio-linux): Installationsskript für xTool Studio unter Wine.
  - Voraussetzungen: Wine ≥ 11.5 (das Skript lädt sonst einen eigenen Wine-Build), Vulkan-Treiber, X11/XWayland, ca. 4 GB Platz.
  - Laut Projekt funktionieren: UI, Projekte, Materialeinstellungen, Netzwerk-Gerätesuche.
  - **Ungetestet:** echte USB-/WLAN-Verbindung zur Maschine, Jobs senden, Kamera.
  - Die Abfrage nach CH340-/RNDIS-Treibern beim Start wegklicken: Linux bringt `ch341` und `rndis_host` im Kernel mit.

## Varianten

| Variante | Aufwand | Status |
|---|---|---|
| A: Wine + Community-Skript | gering | **installiert, startet** – Gerätetest offen |
| B: Windows-VM (KVM/virt-manager) mit USB-Passthrough | mittel | Fallback |
| C: eigener Windows-/Mac-Rechner an der Maschine | – | Notlösung |

## Testprotokoll

**Testrechner:** Debian 13, Kernel 6.12, KDE (Wayland), AMD Radeon 680M (RADV/Vulkan 1.4), System-Wine 10.0 (zu alt → Skript lädt eigenes Wine)

| Schritt | Ergebnis | Notiz |
|---|---|---|
| Installation (`install.sh`) | ✅ 2026-10-01 | xTool Studio 1.9.11, Wine 11.17 staging (Kron4ek) vom Skript geladen, ca. 5 min |
| Start / UI | ✅ 2026-10-01 | Fenster erscheint nach ca. 30 s, Dialog Land/Region; Arbeitsfläche (WebGL) noch prüfen |
| Login xTool-Konto | TODO | |
| Gerät per WLAN finden | TODO | |
| Gerät per USB finden | TODO | |
| Job senden & lasern | TODO | |
| Kamera / Positionierung | TODO | |

## Installation (Variante A)

Den Installer für 1.9.11 gibt es direkt bei xTool: `storage.atomm.com/.../xTool-Studio-x64-1.9.11.exe`, URL aus dem offiziellen [winget-Manifest](https://github.com/microsoft/winget-pkgs/tree/master/manifests/m/Makeblock/xToolStudio).
SHA256: `3a2436980a9a6cfea6b7c75ffb34b2f4f8b8ed1966880e8cfb0002573954ac41`

Installiert wird nach `~/.local/share/wineprefixes/xtool-studio`, `~/.local/share/xtool-studio` (Wine + Logs), Starter `~/.local/bin/xtool-studio` und Menüeintrag. Kein sudo nötig, abgesehen von den apt-Paketen.


```bash
sudo -A apt install p7zip-full winetricks cabextract icoutils curl
git clone https://github.com/gregmatthewcrossley/xtool-studio-linux
cd xtool-studio-linux
./install.sh --exe ~/Downloads/xTool-Studio-x64-<VERSION>.exe
```

Den Windows-Installer nur von der [offiziellen xTool-Seite](https://www.xtool.com/pages/software) laden.

Entfernen: `./uninstall.sh` (mit `--keep-wine`, um den Wine-Build zu behalten).

> Wenn Variante A stabil läuft: als Ansible-Rolle in `lab_config` übernehmen.
