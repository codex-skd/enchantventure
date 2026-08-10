# EnchantVenture Translations

Client-side resource pack for Minecraft 26.2 that adds Spanish (`es_ES`) language files for mods included
in the [EnchantVenture](https://www.curseforge.com/minecraft/modpacks/enchantventure) modpack that don't
ship their own — without touching the mods themselves.

## Coverage

Translations are added incrementally, mod by mod. See [`docs/TRANSLATIONS_STATUS.md`](docs/TRANSLATIONS_STATUS.md)
for the current status of every mod in the modpack.

## Requirements

- Minecraft **26.2** (pack format 88)
- The EnchantVenture modpack (or any subset of the mods it bundles)

## Installation

1. Download `EnchantVenture_translations-<version>.zip` from `build/`.
2. Place it in `resourcepacks/`.
3. Enable it in **Options → Resource Packs**.
4. Set your game language to **Español (España)**.

## Build

The resource pack content lives under `resourcepack/` (curated by hand, one `lang/es_es.json` per mod).
The build script validates the JSON files and zips them with `pack.mcmeta` at the root (loads directly):

```bash
python build_translation_pack.py
# → build/EnchantVenture_translations-<version>.zip
```

Version is read from `version.txt` (`0.0.0-beta.1`).

## License

All Rights Reserved.
