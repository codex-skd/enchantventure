# EnchantVenture Pack

Client-side resource pack for the EnchantVenture modpack (Minecraft 26.2). It bundles:

- **Spanish (`es_ES`) translations** for mods included in the modpack that don't ship their own —
  without touching the mods themselves.

## Features

- 🗣️ `es_ES` language files for mods without Spanish support (88 asset folders, curated by hand).

## Requirements

- Minecraft **26.2** (pack format 88)
- The EnchantVenture modpack (or any subset of the mods it bundles)

## Installation

1. Download `EnchantVenture_Pack-<version>.zip` from `build/`.
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
# → build/EnchantVenture_Pack-<version>.zip
```

Version is read from `version.txt` (`1.0.0-beta.2`).

## Credits

- Spanish translations: **Stalking Dragons**.

## License

All Rights Reserved.
