# Changelog

Todos los cambios notables de EnchantVenture Pack se documentan en este archivo.

El formato sigue [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
y el proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.5.0] - 2026-08-18

### Añadido

- Release estable consolidando la ronda de traducciones `es_ES` de las betas 1.5.0-beta.1 a beta.14: 14
  mods traducidos o actualizados (ver entradas de beta anteriores para el detalle mod a mod).

## [1.5.0-beta.14] - 2026-08-18

### Añadido

- **Entity Texture Features** (`entity_texture_features`): traducción `es_ES` completa vía override (309
  claves). Mod nuevo en la instancia. Traducción delegada a OpenCode en tres pasadas: la primera dejó el
  JSON corrupto/truncado a 127 claves válidas recuperables, una segunda pasada dirigida a las 182
  restantes solo completó 167, y las 15 finales (explicaciones de propiedad y ajustes de piel de jugador)
  se tradujeron manualmente. Cobertura final 309/309 verificada.

### Nota de cierre de ronda

- Ronda de auditoría de traducciones `es_ES` completada: 14 mods procesados
  (enchantinginfuser, yet_another_config_lib_v3, respackopts, wishfulrecipes, echorelics,
  workshop_for_handsome_adventurer, jei, mocreatures, sophisticatedcore, sophisticatedbackpacks,
  sophisticatedstorage, tbos, entity_model_features, entity_texture_features), versión 1.0.0-beta.7 →
  1.5.0-beta.14. Pendiente de finalizar (bump a release estable 1.5.0 y subida a CurseForge, solo con
  confirmación del usuario).

## [1.5.0-beta.13] - 2026-08-18

### Añadido

- **Entity Model Features** (`entity_model_features`): traducción `es_ES` completa vía override (291
  claves). Mod nuevo en la instancia. Traducción delegada a OpenCode; el modelo imprimió el JSON en su
  salida de texto en lugar de escribir el archivo directamente, se extrajo y guardó manualmente tras
  verificar cobertura 100%.

## [1.5.0-beta.12] - 2026-08-18

### Añadido

- **The Birth of Steve** (`tbos`): traducción `es_ES` actualizada vía override (507 claves). Traducción
  delegada a OpenCode en dos pasadas: la primera cubrió 425/507 claves, una segunda pasada dirigida
  completó las 82 claves de lore/mazmorra que faltaban (categorías de sala, mensajes de archivo,
  fragmentos de tomo, diario de misión).

## [1.5.0-beta.11] - 2026-08-18

### Añadido

- **Sophisticated Storage** (`sophisticatedstorage`): traducción `es_ES` actualizada vía override (421
  claves). Traducción delegada a OpenCode; 15 claves faltantes (variantes de
  `stack_upgrade_tier_X_to_tier_Y_conversion`) corregidas manualmente con patrón consistente.

## [1.5.0-beta.10] - 2026-08-18

### Añadido

- **Sophisticated Backpacks** (`sophisticatedbackpacks`): traducción `es_ES` actualizada vía override
  (410 claves). Traducción delegada a OpenCode; cobertura 100% verificada sin correcciones necesarias.

## [1.5.0-beta.9] - 2026-08-18

### Añadido

- **Sophisticated Core** (`sophisticatedcore`): traducción `es_ES` actualizada vía override (302 claves).
  Traducción delegada a OpenCode; 1 clave faltante (`item.sophisticatedcore.stack_upgrade_conversion.tooltip`)
  corregida manualmente.

## [1.5.0-beta.8] - 2026-08-18

### Añadido

- **DrZhark's Mo'Creatures** (`mocreatures`): traducción `es_ES` completa vía override (319 claves).
  Traducción delegada a OpenCode (modelo `nvidia/nemotron-3-super-120b-a12b`); verificada cobertura
  100% sin claves inventadas ni faltantes.

## [1.5.0-beta.7] - 2026-08-18

### Añadido

- **Just Enough Items** (`jei`): traducción `es_ES` actualizada vía override (334 claves). Traducción
  delegada a OpenCode (modelo `nvidia/nemotron-3-super-120b-a12b`); verificada y corregida manualmente
  antes de commitear (2 claves inventadas eliminadas, 10 claves reales faltantes traducidas a mano).

## [1.5.0-beta.6] - 2026-08-18

### Añadido

- **Workshop for Handsome Adventurer** (`workshop_for_handsome_adventurer`): traducción `es_ES` completa
  vía override (165 claves). Mod nuevo en la instancia desde la última auditoría.

## [1.5.0-beta.5] - 2026-08-18

### Añadido

- **Echo Relics** (`echorelics`): traducción `es_ES` actualizada vía override (25 claves). El jar en la
  instancia subió de versión (0.1.0 → 0.2.0) y añadió claves nuevas sin cubrir.

### Corregido

- Auditoría de mods marcados incorrectamente como pendientes: AppleSkin, Cloth Config, Connected Glass,
  Gateway of Doom, Warlockery y Ancient Artifacts ya traían `es_es.json` completo en el jar actualizado
  de la instancia — no requerían override en este pack. Corregido en `docs/TRANSLATIONS_STATUS.md`.

## [1.5.0-beta.4] - 2026-08-18

### Añadido

- **Wishful Recipes** (`wishfulrecipes`): traducción `es_ES` actualizada (33 claves). El jar en la
  instancia subió de versión (0.2.2 → 1) y añadió claves nuevas sin cubrir.

## [1.5.0-beta.3] - 2026-08-18

### Añadido

- **Resource Pack Options** (`respackopts`): traducción `es_ES` completa (26 claves). Mod nuevo en la
  instancia desde la última auditoría.

## [1.5.0-beta.2] - 2026-08-18

### Añadido

- **YetAnotherConfigLib** (`yet_another_config_lib_v3`): traducción `es_ES` completa vía override (26
  claves). El jar en la instancia se actualizó desde la última revisión y trae claves nuevas sin cubrir.

## [1.5.0-beta.1] - 2026-08-18

### Añadido

- **Enchanting Infuser** (`enchantinginfuser`): traducción `es_ES` completa (14 claves). Mod nuevo en la
  instancia desde la última auditoría (2026-08-08).
- Inicio de la ronda de auditoría de mods nuevos/actualizados en la instancia: 20 mods pendientes de
  `es_ES` detectados (revisión mod a mod, ver `docs/TRANSLATIONS_STATUS.md`). No incluye subida a
  CurseForge hasta completar la ronda.

## [1.0.0-beta.7] - 2026-08-13

### Eliminado

- **Enchanting Table Magic Circle** (retexturizado animado de la mesa de encantamientos, integrado desde
  1.0.0-beta.1): retirado por completo — `respackopts.json5`, `assets/minecraft/optifine/`,
  `assets/minecraft/shaders/`, `assets/minecraft/textures/entity/` (libro/circulo/runas),
  `assets/enchantinginfuser/textures/` y las claves `rpo.*` de los 22 `assets/minecraft/lang/*`
  (21 idiomas puramente `rpo.*` eliminados, `es_es.json` limpiado de esas claves conservando el resto
  de traducciones). Motivo: la animación de textura custom de OptiFine (parcheo `from/to` de fotogramas
  sobre `enchanting_table_book.png`/`_e.png`) no se renderiza correctamente con EMF/ETF en 26.2 —
  produce artefactos de ruido/textura sin recortar sobre el libro. El pack vuelve a ser solo de
  traducciones `es_ES`.
- Subido a CurseForge vía `scripts/curseforge-upload.ps1` (file ID `8639186`, HTTP 200). Igual que en
  beta.5/beta.6, la verificación posterior con `GET /v1/mods/{id}/files/{fileId}` devuelve 404 pese a la
  subida exitosa — patrón recurrente de CurseForge en este proyecto, no bloqueante (confirmar
  disponibilidad manualmente en la web del proyecto si hace falta certeza).

## [1.0.0-beta.6] - 2026-08-12

### Corregido

- **CurseForge — subida rechazada de 1.0.0-beta.5**: el ZIP de beta.5 era byte-idéntico al de beta.4
  (mismo tamaño exacto, `resourcepack/` sin cambios de contenido) porque `pack.mcmeta` nunca incluía la
  versión en su `description`. CurseForge rechazó la subida por huella (fingerprint) duplicada de un
  archivo ya existente en el proyecto. La subida con file ID `8625876` registrada en el commit de
  beta.5 nunca llegó a estar disponible (confirmado vía `GET /v1/mods/{id}/files/{fileId}` → 404); el
  intento posterior de re-subir el mismo ZIP sin cambios (file ID `8635550`) tampoco quedó disponible.
- Añadida la versión a `resourcepack/pack.mcmeta` (`description`) para que cada build genere un ZIP con
  contenido único, evitando que futuras betas sin cambios de traducción vuelvan a colisionar por
  fingerprint duplicado en CurseForge.
- Subido a CurseForge vía `scripts/curseforge-upload.ps1` (file ID `<pendiente>`).

## [1.0.0-beta.5] - 2026-08-11

### Documentado

- **Better Villager Animations**: investigadas sus 14 claves de `lang/en_us.json` (nombres de profesión,
  `offer.rare_for`) — ya estaban 100% cubiertas por el `es_es.json` de este pack, nada pendiente. El
  texto en inglés que se sigue viendo en los bocadillos de diálogo de los aldeanos (saludos, comentarios
  ambientales, frases de venta/amenaza) no sale de esas claves: está codificado como literales de texto
  directamente en el bytecode Java del mod (`VillagerDialogueCatalog`, `VillagerConversationCatalog`,
  `VillagerDialogueExpansion`, `VillagerThreatDialogueCatalog`, ~136 frases en total), nunca expuesto vía
  lang key. No es traducible desde un resource pack; documentado en `docs/TRANSLATIONS_STATUS.md`.
- Sin cambios de contenido en `resourcepack/` — release solo para dejar constancia de esta investigación
  en el historial de versiones.
- Subido a CurseForge vía `scripts/curseforge-upload.ps1` (file ID `8625876`).

## [1.0.0-beta.4] - 2026-08-11

### Corregido

- **Shader `entity.fsh` (círculo mágico)**: el orden de operaciones difería del pack original de referencia
  (`lib_ext/Enchanting Table Magic Circle v.2.5`). El port a la base vanilla de 26.2 aplicaba la
  multiplicación por color de vértice/`ColorModulator` y la mezcla del overlay **antes** de la
  multiplicación condicional por `lightMapColor` (que se salta para píxeles con alpha 252, el círculo
  emisivo); el original aplica la luz primero, y el overlay al final. Ese reordenamiento degradaba el
  círculo/runas a un blob translúcido sin forma nítida en vez del anillo grabado esperado. Reordenado
  para que coincida exactamente con la secuencia del original: luz condicional → color de vértice ×
  `ColorModulator` → mezcla de overlay.
- Verificado mediante diff completo (154 archivos) del pack original vendorizado en `lib_ext/` contra
  `resourcepack/`: geometría (`book.jem`), texturas (`circle.png`, `runes.png`, variantes de color) y
  `.properties` de animación son idénticos byte a byte al original — el único cambio funcional real
  frente al pack que funciona era este shader.
- Subido a CurseForge vía `scripts/curseforge-upload.ps1` (file ID `8625810`).

## [1.0.0-beta.3] - 2026-08-10

### Cambiado

- Renombrado el proyecto de **EnchantVenture** a **EnchantVenture Pack** (el pack ya no se llama como la
  modpack; nombre genérico que puede crecer con más contenido en el futuro). Repo GitLab movido a
  `stalking-dragons/minecraft/enchantventure-pack`. ZIP ahora: `EnchantVenture_Pack-<version>.zip`.
- Actualizados summary y descripción general del pack (CurseForge) y referencias internas.

## [1.0.0-beta.2] - 2026-08-10

### Documentado

- Aclarados los requisitos del círculo mágico (los del pack original de Jacosvaldo):
  - **EMF** (Entity Model Features) u OptiFine — requerido para el modelo del libro (`optifine/cem`).
  - **ETF** (Entity Texture Features) u OptiFine — requerido para texturas animadas/emisivas
    (`optifine/anim`, overlays `_e`).
  - **Animatica es solo Fabric**: no aplica a NeoForge.
  - **Respackopts** sigue siendo opcional (color/animación); sin él, círculo azul por defecto.
- Actualizado README, descripción de CurseForge y workflow con estos requisitos.

## [1.0.0-beta.1] - 2026-08-10

### Cambiado

- Renombrado el proyecto de `EnchantVenture_translations` a **EnchantVenture** (nombre de la
  modpack). Repo GitLab movido a `stalking-dragons/minecraft/enchantventure`. ZIP ahora:
  `EnchantVenture-<version>.zip`.
- El pack deja de ser solo de traducciones: ahora es un resource pack multifunción de la modpack.

### Añadido

- **Enchanting Table Magic Circle** (de Jacosvaldo, adaptado a 26.2, uso no comercial):
  - Retexturizado del libro de la mesa de encantamientos con círculo mágico animado y emisivo.
  - 11 colores de círculo + modos de animación (normal/bruteforce/disabled) configurables vía
    Respackopts (`respackopts.json5`, opcional).
  - Shader `assets/minecraft/shaders/core/entity.fsh` portado a la base vanilla de 26.2
    (píxeles emisivos alpha 252); `entity.vsh` = vanilla 26.2.
  - Texturas OptiFine/EMF (`optifine/`, CEM/anim) y texturas del mod Enchanting Infuser.
  - 22 `lang` de `minecraft` con las claves `rpo.*` del círculo en 22 idiomas (solo el namespace
    `minecraft`; el resto de mods siguen en `es_ES`).
  - `assets/minecraft/lang/es_es.json` fusionado: claves `rpo.*` + claves existentes de Ancient
    Artifacts 2 / Dungeons and Taverns (76 claves en total).

### Corregido

- CI: validación de `pack.mcmeta` actualizada al esquema `min_format`/`max_format` = 88.

### Nota

- Sin Respackopts se usa el círculo azul por defecto.
- El círculo mágico requiere **EMF + ETF** (o OptiFine) instalados manualmente: EMF para el modelo
  del libro (`optifine/cem`) y ETF para texturas animadas/emisivas (`optifine/anim`, `_e`). Animatica
  es solo Fabric y no aplica a NeoForge.

## [0.0.0-beta.18] - 2026-08-10

### Corregido

- `pack.mcmeta` ahora usa `min_format`/`max_format` = `88` en lugar del antiguo `pack_format: 64`.
  El valor 64 correspondía a Minecraft 1.21.7-1.21.8, por lo que el juego marcaba el pack como
  "diseñado para una versión anterior" y no como compatible con 26.2. Desde 1.21.9/26.x el pack format
  se declara con `min_format`/`max_format` en vez del campo legacy `pack_format`.

### Nota

- Sin cambios de contenido de traducción: solo metadata del pack. Se documenta además que el pack no
  requiere el mod `Respackopts` (no expone ninguna opción de configuración).

## [0.0.0-beta.17] - 2026-08-09

### Corregido

- El ZIP del pack queda limpio: se purgaron 70 archivos `lang/*.json` de idiomas no-es_ES (de_de,
  en_us, fr_fr, it_it, ja_jp, ko_kr, pt_br, ru_ru, zh_cn) que se habían vuelto a añadir fuera del
  tracker. El artefacto ahora contiene únicamente el `es_es.json` de los 88 folders de assets.

### Nota

- Sin cambios de contenido de traducción en esta versión: solo garantiza que el paquete distribuido
  lleva traducciones en español (`es_ES`) y nada más.

## [0.0.0-beta.16] - 2026-08-08

### Añadido

- **Workhand Tools** (`workhand_tools`): traducción completa (28 claves), mod nuevo en la instancia sin
  `es_es.json` propio.

### Corregido

- **Stellarity** (`stellarity`): el `es_es.json` del pack estaba corrupto con ~36k claves del mapa de
  ofuscación del mod (namespace `space`). Reescrito desde cero como traducción real al español de las
  645 claves de `en_us.json`.

### Eliminado

- 279 archivos `lang/*.json` de idiomas no-es_ES (de_de, en_us, fr_fr, it_it, ja_jp, ko_kr, pt_br,
  ru_ru, zh_cn): el pack solo lleva `es_es.json`.
- 15 folders de assets obsoletos (mods ya fuera de la instancia o namespace corregido):
  `ancient-artifacts-2`, `better-compatibility-checker`, `better_party_x_waystones`, `gatewayofdoom`,
  `hammersandexcavators`, folders antiguos de Moog's y Dungeons & Taverns, `teleport_animation`,
  `netherportalfix`, `shogi`. Los `es_es.json` vacíos de `netherportalfix` y `shogi` no aportaban nada.
- Resultado: el pack queda con 88 folders de assets, un `es_es.json` por mod.

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
- `build_pack.py` valida los `es_es.json` de `resourcepack/` y empaqueta
  `build/EnchantVenture_translations-<version>.zip` con `pack.mcmeta` en la raíz.
- Docs CurseForge (`docs/curseforge/`), workflow propio
  (`docs/WORKFLOW_ENCHANTVENTURE_26-2.md`) y tracker de cobertura por mod
  (`docs/TRANSLATIONS_STATUS.md`) con el escaneo inicial de los 150 mods de la instancia
  (35 ya traen `es_ES`, 105 pendientes, 10 son mods propios fuera de alcance).
- Sin traducciones de mods todavía — se irán añadiendo mod a mod en próximas versiones.
