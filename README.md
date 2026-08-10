# EnchantVenture

Client-side resource pack for the EnchantVenture modpack (Minecraft 26.2). It bundles:

- **Spanish (`es_ES`) translations** for mods included in the modpack that don't ship their own —
  without touching the mods themselves.
- **Enchanting Table Magic Circle** — a retextured, animated magic circle around the enchanting
  table book, with 11 color options (adapted to 26.2 from the pack by Jacosvaldo).
- **Optional Respackopts options** to pick the circle color and animation mode in-game.

## Features

- 🗣️ `es_ES` language files for mods without Spanish support (88 asset folders, curated by hand).
- ✨ Animated magic circle on the enchanting table book + lectern/enchanting screen books.
- 🎨 11 circle colors (blue, purple, pink, red, orange, gold, green, dark, white, flame, water).
- 🎬 Animation modes: `normal`, `bruteforce`, `disabled` (via Respackopts, optional).
- 💡 Emissive rendering for the circle (custom `entity` shader adapted to 26.2).

## Requirements

- Minecraft **26.2** (pack format 88)
- The EnchantVenture modpack (or any subset of the mods it bundles)
- Required for the magic circle (NeoForge equivalents of the pack's requirements):
  - **EMF** (Entity Model Features) or **OptiFine** — custom book model (`optifine/cem`).
  - **ETF** (Entity Texture Features) or **OptiFine** — animated / emissive textures
    (`optifine/anim`, `_e` overlays). *Animatica is Fabric-only and does not apply to NeoForge.*
- Optional:
  - **Respackopts** — to pick the circle color / animation mode in-game. Without it, the
    default blue circle is used.

## Installation

1. Download `EnchantVenture-<version>.zip` from `build/`.
2. Place it in `resourcepacks/`.
3. Enable it in **Options → Resource Packs** (above any other resource pack that also translates
   the same mods, if applicable).
4. Set your game language to **Español (España)**.

## Coverage

Translations are added incrementally, mod by mod. See
[`docs/TRANSLATIONS_STATUS.md`](docs/TRANSLATIONS_STATUS.md) for the current status of every mod.

## Build

The resource pack content lives under `resourcepack/`. The build script validates the JSON files
and zips them with `pack.mcmeta` at the root (loads directly):

```bash
python build_pack.py
# → build/EnchantVenture-<version>.zip
```

Version is read from `version.txt` (`1.0.0-beta.1`).

## Credits

- Spanish translations: **Stalking Dragons**.
- Enchanting Table Magic Circle: **Jacosvaldo** (adapted to Minecraft 26.2, non-commercial use only).

## License

All Rights Reserved.
