# xTool Studio on Linux

🇩🇪 [Deutsch](software-linux.de.md) · [← xTool F2 Ultra](README.md)

## Background (research 10/2026)

- xTool ships xTool Studio and xTool Creative Space for **Windows and macOS only**. There is no official Linux build ([xTool Support](https://support.xtool.com/article/2405), [system requirements](https://support.xtool.com/article/671)).
- **LightBurn is not an alternative:** the F2 Ultra uses a proprietary protocol and is controlled only through xTool Studio ([LightBurn forum](https://forum.lightburnsoftware.com/t/unable-to-connect-lightburn-with-xtool-f2-ultra/183981)). At best, LightBurn works as a design tool with SVG export.
- **Community project** [gregmatthewcrossley/xtool-studio-linux](https://github.com/gregmatthewcrossley/xtool-studio-linux): installer script for xTool Studio under Wine.
  - Requirements: Wine ≥ 11.5 (otherwise the script downloads its own Wine build), Vulkan driver, X11/XWayland, about 4 GB of disk space.
  - According to the project, these work: UI, projects, material settings, network device discovery.
  - **Untested:** real USB/Wi-Fi connection to the machine, sending jobs, camera.
  - Dismiss the CH340/RNDIS driver prompts on first start: Linux already ships `ch341` and `rndis_host` in the kernel.

## Options

| Option | Effort | Status |
|---|---|---|
| A: Wine + community script | low | **installed, launches** – device test pending |
| B: Windows VM (KVM/virt-manager) with USB passthrough | medium | fallback |
| C: dedicated Windows/Mac machine at the laser | – | last resort |

## Test log

**Test machine:** Debian 13, kernel 6.12, KDE (Wayland), AMD Radeon 680M (RADV/Vulkan 1.4), system Wine 10.0 (too old → script downloads its own Wine)

| Step | Result | Note |
|---|---|---|
| Installation (`install.sh`) | ✅ 2026-10-01 | xTool Studio 1.9.11, Wine 11.17 staging (Kron4ek) downloaded by the script, ~5 min |
| Launch / UI | ✅ 2026-10-01 | window appears after ~30 s, country/region dialog |
| Canvas / editing | ✅ 2026-10-01 | UI renders, objects can be edited |
| xTool account login | TODO | |
| Find device via Wi-Fi | TODO | |
| Find device via USB | TODO | |
| Send job & laser | TODO | |
| Camera / positioning | TODO | |

## Installation (option A)

The 1.9.11 installer is available directly from xTool: `storage.atomm.com/.../xTool-Studio-x64-1.9.11.exe`, URL taken from the official [winget manifest](https://github.com/microsoft/winget-pkgs/tree/master/manifests/m/Makeblock/xToolStudio).
SHA256: `3a2436980a9a6cfea6b7c75ffb34b2f4f8b8ed1966880e8cfb0002573954ac41`

Installs into `~/.local/share/wineprefixes/xtool-studio`, `~/.local/share/xtool-studio` (Wine + logs), launcher `~/.local/bin/xtool-studio` and a menu entry. No sudo needed except for the apt packages.


```bash
sudo -A apt install p7zip-full winetricks cabextract icoutils curl
git clone https://github.com/gregmatthewcrossley/xtool-studio-linux
cd xtool-studio-linux
./install.sh --exe ~/Downloads/xTool-Studio-x64-<VERSION>.exe
```

Download the Windows installer only from the [official xTool page](https://www.xtool.com/pages/software).

Removal: `./uninstall.sh` (add `--keep-wine` to keep the Wine build).

> Once option A runs reliably: turn it into an Ansible role in `lab_config`.
