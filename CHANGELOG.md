# Changelog

Todos los cambios notables de EnchantVenture Translations se documentan en este archivo.

El formato sigue [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
y el proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.0-beta.15] - 2026-08-04

### Añadido

- **Better Party X Waystones** (`better_party_x_waystones`): traducción completa (48 claves), mod nuevo
  en la instancia sin `es_es.json` propio.
- **Sophisticated Inventory Interactions** (`sophisticatedinventoryinteractions`): traducción completa
  (27 claves), mod nuevo en la instancia sin `es_es.json` propio.

### Cambiado

- Revisión de mods nuevos/actualizados en la instancia (2026-08-04): 5 mods nuevos detectados
  (AppleSkin — ya trae `es_es.json` completo, sin trabajo; Configurable y TT20 — sin `lang/`, `N/A`) y
  6 mods trackeados que subieron de versión (Armor Cosmetic, Carry Mechanics, Equivalent Legacy y Tower
  Waystone son `PROPIO`, sin trabajo aquí; Berezka API y Warlockery son `SI`, se revisó que su cobertura
  sigue al 100% tras la actualización).

## [0.0.0-beta.14] - 2026-08-04

### Cambiado

- Auditoría completa de cobertura de las traducciones (2026-08-04): se verificó que el `es_es.json` del
  jar o el override de este resource pack cubren el 100% de las claves de `en_us.json` para todos los
  mods, que ningún `es_es` es una copia idéntica del inglés y que los `modid` anotados coinciden con el
  namespace real usado por el jar. Se corrigieron `modid`: `ancient_artifacts_mod`→`ancient_artifacts`
  y los mods de Dungeons and Taverns (`mr_dungeons_andtaverns*`→`dnt`).
- `docs/TRANSLATIONS_STATUS.md` regenerado leyendo el manifest real de cada JAR (`neoforge.mods.toml` /
  `mods.toml` / `fabric.mod.json`) en vez de solo el nombre de archivo: ahora añade `modid` y nombre
  legible del mod, y clasifica los 12 mods propios de Stalking Dragons como `PROPIO` de forma consistente
  (2 de ellos se contaban antes como `SI` por error). Cifras corregidas: 33 `SI` · 105 `PENDIENTE` · 12
  `PROPIO`. Cada fila anota también el archivo y versión exactos usados en la revisión, para detectar
  actualizaciones de mods en revisiones futuras.
- Proyecto CurseForge creado (`project_id` 1638251, categoría `Data Packs` dentro de la clase Resource
  Packs) y logo (`resourcepack/pack.png`) integrado.

### Añadido

- **Overrides de completado de cobertura** (mods cuyo `es_es.json` propio era parcial o inexistente):
  EvilCraft (628 claves + 29 de `evilcraftcompat`), Better Combat (21), Configured (10), Corail
  Tombstone (142), Curios (12), Cyclops Core (42, el jar traía un `es_es.json` vacío), Ecologics (7),
  EnchantmentDescriptions (70), Iris (12), Jade (1), Just Enough Items (183), Mutant Monsters (41),
  Nature's Compass (1), Repurposed Structures (2), Sodium Extra (40), Sophisticated Backpacks (143),
  Sophisticated Core (15), Sophisticated Storage (116), Waystones (263), Xaero's Minimap (523) +
  Xaero's Better PVP (18), y el namespace `dnt` de Dungeons and Taverns (444 claves en total).
- **Override de `assets/minecraft/lang/es_es.json`** (nuevo namespace `minecraft` en este repo):
  traducción real al español de las claves que Ancient Artifacts 2 inyecta en `minecraft` con contenido
  idéntico al inglés (mensajes de muerte, sonidos de `entity.artifact_golem.*`/`entity.player.timewarp.*`,
  pociones de "Expansión"/"Antigravedad") y de las pociones de Dungeons and Taverns
  (`item.minecraft.*.effect.dnt_*`).
- `docs/TRANSLATIONS_STATUS.md` con los hallazgos de la auditoría y la limitación documentada de
  Ancient Artifacts 2 (nombres de ítems en inglés por texto duro en el datapack, no traducible vía
  resourcepack estándar).

## [0.0.0-beta.13] - 2026-08-03

### Añadido

- Traducciones al español (es_ES): Variants&Ventures, Visual Workbench, Wishful Recipes, Xaero's World
  Map y YAML Config. Con esta versión se completa la traducción de los 61 mods que estaban `PENDIENTE`.

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
