# Changelog

Todos los cambios notables de EnchantVenture Translations se documentan en este archivo.

El formato sigue [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
y el proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Sin publicar]

### Cambiado

- `docs/TRANSLATIONS_STATUS.md` regenerado leyendo el manifest real de cada JAR (`neoforge.mods.toml` /
  `mods.toml` / `fabric.mod.json`) en vez de solo el nombre de archivo: ahora añade `modid` y nombre
  legible del mod, y clasifica los 12 mods propios de Stalking Dragons como `PROPIO` de forma consistente
  (2 de ellos se contaban antes como `SI` por error). Cifras corregidas: 33 `SI` · 105 `PENDIENTE` · 12
  `PROPIO`. Cada fila anota también el archivo y versión exactos usados en la revisión, para detectar
  actualizaciones de mods en revisiones futuras.
- Proyecto CurseForge creado (`project_id` 1638251, categoría `Data Packs` dentro de la clase Resource
  Packs) y logo (`resourcepack/pack.png`) integrado.

## [0.0.0-beta.12] - 2026-08-03

### Añadido

- Traducciones al español (es_ES): The Lost City, TNT Foundry, Tom's Simple Storage Mod, Universal
  Enchantment Info y UI Lib.

## [0.0.0-beta.11] - 2026-08-03

### Añadido

- Traducciones al español (es_ES): Shogi, Structurify, SuperMartijn642's Core Lib, It Takes a Pillage
  Continuation y The Birth of Steve.

## [0.0.0-beta.10] - 2026-08-03

### Añadido

- Traducciones al español (es_ES): NetherPortalFix, Not Enough Crashes, Pantry for Blockheads,
  Reliquary Reincarnations y Right Click Harvest.

## [0.0.0-beta.9] - 2026-08-03

### Añadido

- Traducciones al español (es_ES): Neroland Core, NeroLogistics, NeroQuests, NeroSpace y NeroTech.

## [0.0.0-beta.8] - 2026-08-03

### Añadido

- Traducciones al español (es_ES): MoogsTemplesReimagined, MoogsVoyagerStructures, Naraka,
  NeroAgriculture y NeroDecor.

## [0.0.0-beta.7] - 2026-08-03

### Añadido

- Traducciones al español (es_ES): MoogsNetherStructures, DrZhark's Mo'Creatures, Modonomicon,
  Dungeons and Taverns Ancient City Overhaul y Dungeons and Taverns Pillager Outpost Overhaul.

## [0.0.0-beta.6] - 2026-08-03

### Añadido

- Traducciones al español (es_ES): Just Enough Professions (JEP), Kenny, Marsward, MoogsEndStructures
  y MoogsMissingVillages.

## [0.0.0-beta.5] - 2026-08-03

### Añadido

- Traducciones al español (es_ES): Fusion, Gateway of Doom X Xaero's World Map, Hammers and
  Excavators, Inventory Essentials y JamLib.

## [0.0.0-beta.4] - 2026-08-03

### Añadido

- Traducciones al español (es_ES): Cristel Lib, Echo Relics, Enchanted Adventure, FallingTree,
  Fish of Thieves y Formations.

## [0.0.0-beta.3] - 2026-08-03

### Añadido

- Traducciones al español (es_ES): Better Party X Xaero's World Map, Better Villager Animations,
  Bridging Mod, CoK_Tools y Crafting Tweaks.

## [0.0.0-beta.2] - 2026-08-03

### Añadido

- Primeras traducciones al español (es_ES): ApexCore, Balm, Better Compatibility Checker, Berezka API
  y Better Party.
- Subida a CurseForge con el script `scripts/curseforge-upload.ps1` (primer uso real, valida
  `game_versions`).

## [0.0.0-beta.1] - 2026-08-03

### Añadido

- Primer versionado del resource pack contra GitLab (`26.2-0.0.0-beta.1`).
- `build_translation_pack.py` valida los `es_es.json` de `resourcepack/` y empaqueta
  `build/EnchantVenture_translations-<version>.zip` con `pack.mcmeta` en la raíz.
- Docs CurseForge (`docs/curseforge/`), workflow propio
  (`docs/WORKFLOW_ENCHANTVENTURE_TRANSLATIONS_26-2.md`) y tracker de cobertura por mod
  (`docs/TRANSLATIONS_STATUS.md`) con el escaneo inicial de los 150 mods de la instancia
  (35 ya traen `es_ES`, 105 pendientes, 10 son mods propios fuera de alcance).
- Sin traducciones de mods todavía — se irán añadiendo mod a mod en próximas versiones.
