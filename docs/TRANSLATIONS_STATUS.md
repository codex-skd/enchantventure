# Estado de traducciones — EnchantVenture Pack

> Generado leyendo el manifest real de cada JAR (`META-INF/neoforge.mods.toml` / `mods.toml` /
> `fabric.mod.json`) en `C:\Users\llagu\curseforge\minecraft\Instances\EnchantVenture\mods` (154 jars),
> el 2026-08-03. Auditoría completa de cobertura el 2026-08-04: se verificó que el `es_es` del jar o el
> override de este resource pack cubren el 100% de las claves de `en_us.json`, que ningún `es_es` es una
> copia idéntica del inglés y que los `modid` anotados coinciden con el namespace real usado por el jar.
> Revisión de mods nuevos/actualizados en la instancia el 2026-08-04 (misma fecha): 5 mods nuevos
> (AppleSkin, Better Party X Waystones, Configurable, Sophisticated Inventory Interactions, TT20) y 6
> mods ya trackeados que subieron de versión (Armor Cosmetic, Berezka API, Carry Mechanics, Equivalent
> Legacy, Tower Waystone, Warlockery — los `PROPIO` no requieren trabajo aquí, los `SI` se revisaron y
> siguen cubiertos al 100%).
>
> Limpieza y ampliación el 2026-08-08: se eliminaron los `lang/` de idiomas no-es_ES (279 archivos) y los
> folders obsoletos de mods ya eliminados/renombrados de la instancia (ancient-artifacts-2,
> better-compatibility-checker, better_party_x_waystones, gatewayofdoom, hammersandexcavators,
> moogsendstructures, moogsmissingvillages, moogsnetherstructures, moogstemplesreimagined,
> moogsvoyagerstructures, mr_dungeons_andtavernsancientcityoverhaul, mr_dungeons_andtavernspillageroutpostoverhaul,
> teleport_animation, netherportalfix, shogi). Se corrigió el `es_es` de `stellarity` (contenía ~36k claves
> del mapa de ofuscación del namespace `space`; ahora es traducción real de las 645 claves de `en_us`) y se
> añadió el mod nuevo `workhand_tools` (28 claves).
>
> - `SI` = el mod ya trae `lang/es_es.json` propio, no requiere trabajo aquí.
> - `PENDIENTE` = falta `es_es.json` y el mod SÍ tiene claves de texto (`lang/en_us.json`) — candidato real
>   a traducir en este resource pack.
> - `N/A` = el jar no contiene ninguna carpeta `lang/` (librerías, cores, mods de rendimiento/shaders sin
>   texto de UI: Architectury, Sodium, FerriteCore, GeckoLib, PuzzlesLib, etc.). No hay nada que traducir;
>   si en una futura revisión el mod pasara a tener `lang/en_us.json` (ej. tras una actualización que añada
>   opciones de config traducibles), reclasificar a `PENDIENTE`.
> - `PROPIO` = mod de Stalking Dragons (carpeta propia en `Mods_Minecraft/`) — la traducción se añade en
>   el mod, no aquí (fuera de alcance de este repo, se listan igualmente para tener el inventario completo).
>
> **Para qué sirve el campo Versión**: al traducir un mod, su fila queda "fija" con el archivo y la
> versión que se tradujeron. Si en una futura revisión el mod de la instancia tiene un `Archivo`/`Versión`
> distinto al anotado aquí, significa que se ha actualizado desde la última traducción — hay que revisar
> si añadió/quitó/cambió claves en su `en_us.json` antes de dar el mod por `SI` de nuevo.
>
> Al completar un mod: mover su fila a `SI` y actualizar `Última revisión` a la fecha del día.
>
> **Nota de auditoría (2026-08-04)**: se encontró que varios mods marcados `SI` traen un `es_es.json`
> propio incompleto (no cubren el 100% de su `en_us.json`). Para esos mods este resource pack añade un
> override en `resourcepack/assets/<modid>/lang/es_es.json` que completa la cobertura (marcados con
> "(override)" en la fila). También se corrigieron `modid` que no coincidían con el namespace real del
> jar (`ancient_artifacts_mod`→`ancient_artifacts`; los mods de Dungeons and Taverns usan el namespace
> `dnt`, no `mr_dungeons_andtaverns*`).
>
> **Limitación de Ancient Artifacts 2**: el jar no trae carpeta `lang/` bajo su namespace propio
> (`assets/ancient_artifacts/lang/` no existe), y registra su contenido (objetos de artefacto, entidades,
> efectos) directamente en el namespace `minecraft` vía datapack. Los nombres de ítems/bloques se ven en
> inglés en el juego porque se asignan con componentes de texto duro en las funciones del datapack, no
> mediante claves de lang localizables; no son traducibles vía resourcepack estándar salvo que se
> localicen los IDs exactos usados. Lo que sí se pudo traducir es el `es_es.json` de `assets/minecraft`
> que el mod inyecta con contenido idéntico al inglés (traducción falsa): este resource pack lo
> sobrescribe con la traducción real al español de esas claves (mensajes de muerte, sonidos de
> `entity.artifact_golem.*`/`entity.player.timewarp.*`, y las pociones de "Expansión"/"Antigravedad").
> Las claves `tooltip.bg.*` son códigos de icono y no se traducen.
>
> **Limitación de Better Villager Animations**: sus 14 claves de `lang/en_us.json` (nombre del mod,
> `offer.rare_for`, nombres de profesión) ya estaban 100% cubiertas por el `es_es.json` de este resource
> pack — no había nada pendiente ahí. Pero el texto que se ve en los bocadillos de diálogo sobre los
> aldeanos (saludos, comentarios ambientales, frases de venta, líneas de amenaza) **no sale de esas
> claves de lang**: está codificado como literales de texto directamente en el bytecode Java del mod
> (`VillagerDialogueCatalog`, `VillagerConversationCatalog`, `VillagerDialogueExpansion`,
> `VillagerThreatDialogueCatalog` — confirmado extrayendo y grepeando los `.class` del jar,
> ~136 frases en total entre las 4 clases). Un resource pack solo puede sobrescribir lo que el mod
> expone vía `lang/*.json`; esto no pasa por ahí, así que no es traducible desde este repo. Traducirlo
> requeriría un fork/parche del mod (fuera de alcance de un resource pack) — no hay acción posible aquí.
> Revisado el 2026-08-25: tampoco es traducible desde el datapack `EnchantVenture_fixes` — un datapack
> solo puede sobrescribir contenido data-driven (`data/`), nunca literales de texto compilados en
> bytecode Java. El jar no trae ningún `data/`/`assets/*.json` con estos diálogos (confirmado
> `unzip -l`: solo `.class` y `lang/*.json`), así que la limitación es total salvo forkear el mod.
>
> **Nota de Marsward**: su "Field Manual" en el juego (18 capítulos) tampoco sale de `lang/*.json` —
> está codificado como texto literal en `data/marsward/field_manual/field_manual.json` (un archivo de
> datapack del propio mod). A diferencia de Better Villager Animations, esto **sí** es data-driven, así
> que un datapack sí puede sobrescribirlo. Traducido en el datapack hermano `EnchantVenture_fixes`
> (`data/marsward/field_manual/field_manual.json`, ver su `README.md`) — no en este resource pack.
>
> **Nota de Occultism**: su `es_es.json` propio (dentro del jar) cubre 3583 de las 3943 claves de
> `en_us.json`: 390 claves faltan por completo y 2733 son copia idéntica del inglés (traducción falsa),
> mismo patrón de bug que se corrigió antes en `stellarity`. Este resource pack sobrescribe con una
> traducción completa y real de las 3943 claves (override en `resourcepack/assets/occultism/lang/es_es.json`).
>
> Reproducir este escaneo: `python` con `tomllib` (3.11+), leer `META-INF/neoforge.mods.toml` (NeoForge),
> `META-INF/mods.toml` (Forge) o `fabric.mod.json` (Fabric) de cada jar para sacar `modid`/`name`/`version`,
> y comprobar si existe `assets/<modid>/lang/es_es.json` dentro del jar. 4 mods (`aiimprovements`,
> `apexcore`, `jade`, `justenoughprofessions`) declaran la versión como `${file.jarVersion}` en su manifest
> (variable que solo se resuelve al compilar) — para esos se usó la versión visible en el nombre del archivo.

Total: 175 mods documentados · 107 ya con `es_ES` · 0 pendientes (con texto real que traducir) · 47 sin
`lang/` (nada que traducir) · 21 propios (fuera de alcance de este repo). Tras la auditoría de 2026-08-04, 23
mods quedaron completados vía override de este resource pack (su `es_ES` propio era parcial o inexistente).
Revisión de mods nuevos del 2026-08-04: Better Party X Waystones (48 claves) y Sophisticated Inventory
Interactions (27 claves) se completaron también vía override; AppleSkin ya traía su propio `es_es.json`
completo. El 2026-08-08 se añadió el mod nuevo `workhand_tools` (28 claves, override) y se reescribió por
completo el `es_es.json` de `stellarity` (645 claves) que estaba corrupto.

Revisión de mods nuevos el 2026-08-21: 14 mods nuevos detectados en la instancia. `basalt_watchtower` (10
claves), `travel_bites` (21 claves) y `miniworkers` (477 claves) se tradujeron desde cero (no traían
`es_es.json`). `neofarmervillagers` ya traía su propio `es_es.json` completo (6/6 claves). `libjf` no tiene
`lang/` en el jar. 8 mods son `PROPIO` (van en su propio repo, no aquí): `ascendant_attributes`,
`ascendant_enchanting`, `ascendant_equipment`, `ascendant_spawners`, `common_toolkit`, `regalia_slots_api`,
`vellumli`; además `utility_core` (ya `PROPIO`) se dividió en 3 jars (`utility_core_admin`/`_fixes`/`_qol`),
solo se actualizó su fila. `occultism` (3943 claves) traía `es_es.json` propio incompleto (390 claves
faltantes + 2733 idénticas al inglés, mismo patrón de bug que `stellarity`) — completado vía override, ver
nota más abajo.

Revisión de mods nuevos el 2026-08-24: `theurgy` (2863 claves) no traía `es_es.json` propio (el jar
solo incluye `en_us`, `ja_jp`, `pt_br`, `ru_ru`, `zh_cn`) — se tradujo desde cero en este resource pack.

Revisión el 2026-08-25 (instancia `(Traducciones) EnchantVenture`): se encontró `slaughter_hide.jar` suelto
en `mods/`, pero no figura en `installedAddons` de `minecraftinstance.json` (161 entradas oficiales) — no es
parte real del modpack, es un jar añadido manualmente a esta instancia local. No se documenta aquí (si en el
futuro se añade oficialmente al modpack, sí traería `es_es.json` propio completo: 57/57 claves, ninguna
idéntica al inglés). Sin cambios respecto al escaneo del 2026-08-24: 0 pendientes.

Revisión el 2026-08-28 (modpack `EnchantVenture` v5.206.352, 162 addons — cambio grande de contenido). La
tabla se regeneró por completo desde el escaneo real de los 159 jars de la instancia; sólo se reclasificaron
las filas cuyo jar cambió (nada de reclasificación silenciosa de mods que siguen igual).
- **28 mods retirados del modpack** (marcados `RETIRADO DEL MODPACK (2026-08-28)`): Ancient Artifacts 2,
  Better Party X Waystones, Bridging Mod, Configurable, Configured, Connectivity, Curios API,
  Enchanted Adventure, FallingTree, Hammers and Excavators, los tres HopoBetter*, DnT Woodland Mansion
  Overhaul, Grim Kingdoms, Kenny, MoogsMissingVillages, Naraka, NetherPortalFix, Ore Vein Miner, Repurposed
  Structures, Right Click Harvest, The Lost City, TNT Foundry, Towns and Towers, Warlockery. (Los jars
  `dungeons-and-taverns-5.3.0` y `DnT-pillager-outpost-overhaul` también salieron, pero el modid `dnt`
  sobrevive vía el jar `DnT-ancient-city-overhaul`, así que esa fila sólo cambió de archivo.) Se borraron sus
  carpetas `resourcepack/assets/<modid>/` cuando existían (13 carpetas: adventureenchanting, bridgingmod,
  configured, curios, fallingtree, kenny, mmv, naraka, repurposed_structures, rightclickharvest,
  the_lost_city, tntfoundry, warlockery).
- **Renombrados** (`RENOMBRADO`): la fila vieja `cloth_config` se corrige a `cloth-config2` (namespace real
  del jar); `utility_core` quedó dividido en `utility_core_admin/_fixes/_qol/_hud` (todos `PROPIO`).
- **Mods nuevos traducidos en este resource pack** (override): `survival_instinct` (279 claves),
  `frontier_armaments` (97), `horde_hoard` (27), `gateway_of_doom_x_xaeros_minimap` (4), `dangerous` (1).
  Actualizaciones que añadieron claves y se completaron: `croptopia` (+54), `mocreatures` (+10),
  `workhand_tools` (+3), `jei` (+2), `structurify` (+1). Traducción vía OpenCode (`opencode-go/mimo-v2.5-pro`),
  verificada clave por clave (0 missing / 0 extra / 0 placeholder roto); se corrigieron a mano 6 fallos de
  `survival_instinct` (mena de azufre/steellium mal traducidas, keybind "Impulso de traje exo").
- **Mods nuevos sin trabajo**: `aerialhell` y `bosscraft_2` (re-añadidos, sus overrides ya cubrían el 100%);
  `muchmoredungeons` y `epherolib` (sin `lang/` en el jar → N/A).
- `Stellarity` 5.5.5 sigue trayendo `assets/space/lang/en_us.json` (~36k claves, mapa de ofuscación) —
  fila `space` marcada `N/A`, no es texto de UI. La traducción real de `stellarity` (645 claves) sigue OK.

Estado tras la revisión: 162 filas activas (99 `SI` · 22 `PROPIO` · 41 `N/A`) · 0 pendientes · 26 retiradas
· 2 renombradas.

| Mod | modid | Archivo | Versión | Estado | Última revisión |
|---|---|---|---|---|---|
| Advanced Netherite | `advancednetherite` | `advancednetherite-neoforge-2.4.2-26.2.jar` | `2.4.2` | SI | 2026-08-28 |
| Aerial Hell | `aerialhell` | `aerialhell-0.7.7.8_neoforge26.2.jar` | `1.0.0` | SI (override) | 2026-08-28 |
| Ageforged Armor | `ageforged_armor` | `ageforged_armor-26.2-neoforge-26.2.0.57-1.2.7.jar` | `1.2.7` | PROPIO | 2026-08-28 |
| AI-Improvements | `aiimprovements` | `AI-Improvements-26.1.1-0.5.4.jar` | `26.1.1 (del nombre)` | N/A (sin lang/ en el jar) | 2026-08-28 |
| ApexCore | `apexcore` | `apexcore-26.2.3.jar` | `26.2.3 (del nombre)` | SI | 2026-08-28 |
| AppleSkin | `appleskin` | `appleskin-neoforge-mc26.2-3.0.10.jar` | `3.0.10 (del nombre)` | SI | 2026-08-28 |
| Architectury | `architectury` | `architectury-neoforge-21.0.7.jar` | `21.0.7` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Armor Cosmetic | `armor_cosmetic` | `armor_cosmetic-26.2-neoforge-26.2.0.45-beta-1.0.18.jar` | `1.0.18` | PROPIO | 2026-08-28 |
| Ascendant Attributes | `ascendant_attributes` | `ascendant_attributes-26.2-neoforge-26.2.0.57-1.1.0.jar` | `1.1.0` | PROPIO | 2026-08-28 |
| Ascendant Enchanting | `ascendant_enchanting` | `ascendant_enchanting-26.2-neoforge-26.2.0.57-1.1.0.jar` | `1.1.0` | PROPIO | 2026-08-28 |
| Ascendant Equipment | `ascendant_equipment` | `ascendant_equipment-26.2-neoforge-26.2.0.57-1.2.1.jar` | `1.2.1` | PROPIO | 2026-08-28 |
| Ascendant Spawners | `ascendant_spawners` | `ascendant_spawners-26.2-neoforge-26.2.0.57-1.0.0.jar` | `1.0.0` | PROPIO | 2026-08-28 |
| AttributeFix | `attributefix` | `AttributeFix-neoforge-MC26.2-26.2.0.1.jar` | `26.2.0.1` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Balm | `balm` | `balm-neoforge-26.2-26.2.0.6.jar` | `26.2.0.6` | SI | 2026-08-28 |
| Basalt Watchtower | `basalt_watchtower` | `basalt_watchtower-1.0.0 Neoforge 26.2.jar` | `1.0.0` | SI (override) | 2026-08-28 |
| Berezka API | `berezka_api` | `berezka_api-1.2.9.5-beta.4-neoforge-1.26.2.jar` | `1.2.9.5-beta.4` | SI (override) | 2026-08-28 |
| Better Combat | `bettercombat` | `bettercombat-neoforge-3.2.2+26.2.jar` | `3.2.2` | SI (override) | 2026-08-28 |
| Better Compatibility Checker | `bcc` | `better-compatability-checker-neoforge-26.2.0.1.jar` | `26.2.0.1` | SI | 2026-08-28 |
| Better Connections | `better_connections` | `better_connections-26.2-neoforge-26.2.0.57-1.1.0.jar` | `1.1.0` | PROPIO | 2026-08-28 |
| Better Party | `better_party` | `better-party-neoforge-26.2-1.1.3.jar` | `1.1.3` | SI | 2026-08-28 |
| Better Party X Xaero's World Map | `better_party_x_xaeros_world_map` | `better-party-x-xaeros-world-map-neoforge-26.2-1.0.0.jar` | `1.0.0` | SI | 2026-08-28 |
| Better Villager Animations | `bettervillageranimations` | `better-villager-animations-neoforge-26.2.jar` | `1.0.0` | SI (ver nota: diálogos hardcodeados no traducibles) | 2026-08-28 |
| Bosscraft 2 Remake | `bosscraft_2` | `Bosscraft_2_Remake-1.2.0-neoforge-26.x.jar` | `1.2.0` | SI (override) | 2026-08-28 |
| Carry Mechanics | `carry_mechanics` | `carry_mechanics-26.2-neoforge-26.2.0.57-1.1.0.jar` | `1.1.0` | PROPIO | 2026-08-28 |
| clientcrafting mod | `clientcrafting` | `clientcrafting-26.1-2.1.jar` | `2.1` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Cloth Config v26.2 API | `cloth-config2` | `cloth-config-26.2.155.jar` | `26.2.155 (del nombre)` | SI (override) | 2026-08-28 |
| CoK_Tools | `coktools` | `CoKTools-Neoforge-mc26.2-26.2.0.3.jar` | `26.2.0.3` | SI | 2026-08-28 |
| Common Toolkit | `common_toolkit` | `common_toolkit-26.2-neoforge-26.2.0.57-1.1.0.jar` | `1.1.0` | PROPIO | 2026-08-28 |
| Complementary Core | `complementary_core` | `cc-2.3.1-neoforge_1.21.5-26.1.2.jar` | `2.3.1` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Complementary Structures: Towers | `cs_towers` | `cs_towers-0.2.0-neoforge_1.21.x.jar` | `0.2.0` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Connected Glass | `connectedglass` | `connectedglass-1.1.14-neoforge-mc26.2.jar` | `1.1.14` | SI | 2026-08-28 |
| Corail Tombstone | `tombstone` | `tombstone-neoforge-26.2-9.9.3.jar` | `9.9.3` | SI (override) | 2026-08-28 |
| Crafting Tweaks | `craftingtweaks` | `craftingtweaks-neoforge-26.2-26.2.0.3.jar` | `26.2.0.3` | SI | 2026-08-28 |
| Cristel Lib | `cristellib` | `cristellib-neoforge-26.2-3.1.10.jar` | `3.1.10` | SI | 2026-08-28 |
| Croptopia | `croptopia` | `croptopia-neoforge-26.2-4.3.1.jar` | `4.3.1` | SI (override) | 2026-08-28 |
| Cupboard mod | `cupboard` | `cupboard-26.2-4.0.jar` | `4.0` | N/A (sin lang/ en el jar) | 2026-08-28 |
| CustomSkinLoader Bootstrap | `customskinloader-bootstrap` | `CustomSkinLoader_Universal-15.0.1.jar` | `15.0.1` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Cyclops Core | `cyclopscore` | `cyclopscore-26.2-neoforge-1.30.0-1083.jar` | `1.30.0-1083` | SI (override) | 2026-08-28 |
| Dangerous | `dangerous` | `Dangerous NeoForge - 26.2 v1.5.2.jar` | `1.5.2` | SI (override) | 2026-08-28 |
| Data Miner | `data_miner` | `data_miner-26.2-neoforge-26.2.0.57-1.2.0.jar` | `1.2.0` | PROPIO | 2026-08-28 |
| Deimos | `deimos` | `deimos-26.2-neoforge-2.7.jar` | `2.7` | N/A (sin lang/ en el jar) | 2026-08-28 |
| DrZhark's Mo'Creatures | `mocreatures` | `mocreatures-neoforge-26.2.0+26.2.jar` | `26.2.0` | SI (override) | 2026-08-28 |
| Dungeons and Taverns | `dnt` | `DnT-ancient-city-overhaul-3.4 [NeoForge].jar` | `5.3.0` | SI (override) | 2026-08-28 |
| Dungeons and Taverns Nether Fortress Overhaul | `mr_dungeons_andtavernsnetherfortressoverhaul` | `DnT-nether-fortress-overhaul-v3.1 [NeoForge].jar` | `1-v3.1` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Echo Relics | `echorelics` | `echorelics-0.2.0.jar` | `0.2.0` | SI (override) | 2026-08-28 |
| Ecologics | `ecologics` | `Ecologics-NeoFab-26.2-2.6.0.jar` | `2.6.0` | SI (override) | 2026-08-28 |
| Enchanting Infuser | `enchantinginfuser` | `EnchantingInfuser-v26.2.0-mc26.2.x-NeoForge.jar` | `26.2.0` | SI (override) | 2026-08-28 |
| EnchantmentDescriptions | `enchdesc` | `EnchantmentDescriptions-neoforge-MC26.2-26.2.0.2.jar` | `26.2.0.2` | SI (override) | 2026-08-28 |
| Entity Model Features (EMF) | `entity_model_features` | `entity_model_features-3.2.6-26.2-neoforge.jar` | `3.2.6` | SI (override) | 2026-08-28 |
| Entity Texture Features (ETF) | `entity_texture_features` | `entity_texture_features-7.1.1-26.2-neoforge.jar` | `7.1.1` | SI (override) | 2026-08-28 |
| EpheroLib | `epherolib` | `epherolib-neoforge-26.2-1.3.0.jar` | `1.3.0` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Equivalent Legacy | `equivalent_legacy` | `equivalent_legacy-26.2-neoforge-26.2.0.57-1.6.2.jar` | `1.6.2` | PROPIO | 2026-08-28 |
| EvilCraft | `evilcraft` | `evilcraft-26.2-neoforge-1.2.98-1046.jar` | `1.2.98-1046` | SI (override) | 2026-08-28 |
| EvilCraft-Compat | `evilcraftcompat` | `evilcraft-26.2-neoforge-1.2.98-1046.jar` | `1.1.0-137` | SI (override) | 2026-08-28 |
| Explorer's Compass | `explorerscompass` | `ExplorersCompass-26.2-3.3.0-neoforge.jar` | `26.2-3.3.0-neoforge` | SI | 2026-08-28 |
| Fast IP Ping | `fastipping` | `fast-ip-ping-v1.0.11-mc26.1.2.jar` | `1.0.11` | N/A (sin lang/ en el jar) | 2026-08-28 |
| fastasyncworldsave mod | `fastasyncworldsave` | `fastasyncworldsave-26.2-2.6.jar` | `2.6` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Ferrite Core | `ferritecore` | `ferritecore-9.0.0-neoforge.jar` | `9.0.0` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Fish of Thieves | `fishofthieves` | `fish_of_thieves-mc26.2-v26.2.1.1-neoforge.jar` | `26.2.1.1` | SI | 2026-08-28 |
| FokusAPI | `fokusapi` | `FokusAPI-v4.5_MOD.jar` | `4.5` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Formations | `formations` | `formations-1.0.4-neoforge-mc26.2.jar` | `1.0.4` | SI | 2026-08-28 |
| Formations Nether | `formationsnether` | `formationsnether-1.0.5a-mc1.21+.jar` | `1.0.5+a` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Formations Overworld | `formationsoverworld` | `formationsoverworld-1.0.5a-mc1.21+.jar` | `1.0.5+a` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Frontier Armaments | `frontier_armaments` | `frontier_armaments-neoforge-1.0.0+26.2.jar` | `1.0.0` | SI (override) | 2026-08-28 |
| Fusion | `fusion` | `fusion-1.3.14-neoforge-mc26.2.jar` | `1.3.14` | SI | 2026-08-28 |
| Gateway of Doom | `gateway_of_doom` | `gatewayofdoom-neoforge-26.2-2.2.0.jar` | `2.2.0` | SI | 2026-08-28 |
| Gateway of Doom X Xaero's Minimap | `gateway_of_doom_x_xaeros_minimap` | `gateway_of_doom_x_xaeros_minimap-neoforge-26.2-1.1.1.jar` | `1.1.1` | SI (override) | 2026-08-28 |
| Gateway of Doom X Xaero's World Map | `gateway_of_doom_x_xaeros_world_map` | `gateway_of_doom_x_xaeros_world_map-neoforge-26.2-1.0.1.jar` | `1.0.1` | SI | 2026-08-28 |
| GeckoLib 5 | `geckolib` | `geckolib-neoforge-26.2-5.5.3.jar` | `5.5.3` | N/A (sin lang/ en el jar) | 2026-08-28 |
| GlitchCore | `glitchcore` | `GlitchCore-neoforge-26.2-26.2.0.0.0.jar` | `26.2.0.0.0` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Gpu memory leak fix | `gpumemleakfix` | `gpumemleakfix-26.1-1.9.jar` | `1.9` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Horde Hoard | `horde_hoard` | `horde_hoard-neoforge-1.1.0.jar` | `1.1.0` | SI (override) | 2026-08-28 |
| Iceberg | `iceberg` | `Iceberg-26.2-neoforge-1.4.2.1.jar` | `1.4.2.1` | N/A (sin lang/ en el jar) | 2026-08-28 |
| ImmediatelyFast | `immediatelyfast` | `ImmediatelyFast-NeoForge-1.16.3+26.2.jar` | `1.16.3+26.2` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Immersive Armors | `immersive_armors` | `immersive_armors-1.8.2+26.2-neoforge.jar` | `1.8.2+26.2` | SI | 2026-08-28 |
| Info TAB | `info_tab` | `info_tab-26.2-neoforge-26.2.0.57-1.1.0.jar` | `1.1.0` | PROPIO | 2026-08-28 |
| Inventory Essentials | `inventoryessentials` | `inventoryessentials-neoforge-26.2-26.2.0.4.jar` | `26.2.0.4` | SI | 2026-08-28 |
| Iris | `iris` | `iris-neoforge-1.11.2+mc26.2.jar` | `${version}` | SI (override) | 2026-08-28 |
| Iris Shader Folder | `iris_shader_folder` | `iris_shader_folder-1.4.1-neoforge.jar` | `1.4.1-neoforge` | N/A (sin lang/ en el jar) | 2026-08-28 |
| It Takes a Pillage Continuation | `takesapillage` | `takesapillage-neoforge-1.0.12+mc26.2.jar` | `1.0.12` | SI | 2026-08-28 |
| Jade | `jade` | `Jade-mc26.2-NeoForge-26.2.9.jar` | `26.2.9 (del nombre)` | SI (override) | 2026-08-28 |
| JamLib | `jamlib` | `jamlib-neoforge-2.3.1+26.2.x.jar` | `2.3.1+26.2.x` | SI | 2026-08-28 |
| Just Enough Items | `jei` | `jei-26.2-neoforge-30.25.0.177.jar` | `30.25.0.177` | SI (override) | 2026-08-28 |
| Just Enough Professions (JEP) | `justenoughprofessions` | `JustEnoughProfessions-neoforge-26.2-12.0.0.jar` | `26.2 (del nombre)` | SI | 2026-08-28 |
| Legendary Tooltips | `legendarytooltips` | `LegendaryTooltips-26.2-neoforge-1.6.2.jar` | `1.6.2` | N/A (sin lang/ en el jar) | 2026-08-28 |
| LibJF | `libjf` | `libjf-26.2.2+forge.jar` | `26.2.2+forge` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Lithostitched | `lithostitched` | `lithostitched-1.8.0+beta3-neoforge-26.2.jar` | `1.8.0+beta3` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Lootr | `lootr` | `lootr-neoforge-26.2-1.24.39.121.jar` | `1.24.39.121` | SI | 2026-08-28 |
| Marsward | `marsward` | `marsward-1.0.6.jar` | `1.0.6` | SI | 2026-08-28 |
| Miniworkers | `miniworkers` | `miniworkers-0.1.5.jar` | `0.1.5` | SI (override) | 2026-08-28 |
| Modonomicon | `modonomicon` | `modonomicon-26.2-neoforge-2.4.0.jar` | `2.4.0` | SI | 2026-08-28 |
| Moog's Structure Lib | `moogs_structures` | `moogs_structures-neoforge-26.2-3.0.6.jar` | `3.0.6` | N/A (sin lang/ en el jar) | 2026-08-28 |
| MoogsEndStructures | `mes` | `MoogsEndStructures-1.21-2.0.3.jar` | `2.0.3` | SI | 2026-08-28 |
| MoogsNetherStructures | `mns` | `MoogsNetherStructures-1.21-3.0.0.jar` | `3.0.0` | SI | 2026-08-28 |
| MoogsTemplesReimagined | `mtr` | `MoogsTemplesReimagined-1.21-1.1.3.jar` | `1.1.3` | SI | 2026-08-28 |
| MoogsVoyagerStructures | `mvs` | `MoogsVoyagerStructures-1.21-5.0.11.jar` | `5.0.11` | SI | 2026-08-28 |
| Mouse Tweaks | `mousetweaks` | `MouseTweaks-neoforge-mc26.2-2.31.jar` | `2.31` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Much More Dungeons | `muchmoredungeons` | `muchmoredungeons-neoforge-26.2-1.1.3.jar` | `1.1.3` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Mutant Monsters | `mutantmonsters` | `MutantMonsters-v26.2.1-mc26.2.x-NeoForge.jar` | `26.2.1` | SI (override) | 2026-08-28 |
| Nature's Compass | `naturescompass` | `NaturesCompass-26.2-3.3.0-neoforge.jar` | `26.2-3.3.0-neoforge` | SI (override) | 2026-08-28 |
| Neo Farmer Villagers | `neofarmervillagers` | `neofarmervillagers-1.0.1-neoforge-26.2.jar` | `1.0.0` | SI | 2026-08-28 |
| NeroAgriculture | `neroagriculture` | `neroagriculture-neoforge-26.2-0.1.0-beta.1.jar` | `0.1.0-beta.1` | SI | 2026-08-28 |
| NeroDecor | `nerodecor` | `nerodecor-neoforge-26.2-0.1.0-beta.1.jar` | `0.1.0-beta.1` | SI | 2026-08-28 |
| Neroland Core | `nerolandcore` | `nerolandcore-neoforge-26.2-1.11.0.jar` | `1.11.0` | SI | 2026-08-28 |
| NeroLink | `nerolink` | `nerolink-neoforge-26.2-0.0.1-alpha.2.jar` | `0.0.1-alpha.2` | N/A (sin lang/ en el jar) | 2026-08-28 |
| NeroLogistics | `nerologistics` | `nerologistics-neoforge-26.2-0.1.0-alpha.1.jar` | `0.1.0-alpha.1` | SI | 2026-08-28 |
| NeroQuests | `neroquests` | `neroquests-neoforge-26.2-0.1.0-beta.1.jar` | `0.1.0-beta.1` | SI | 2026-08-28 |
| NeroSpace | `nerospace` | `nerospace-neoforge-26.2-1.0.2.jar` | `1.0.2` | SI | 2026-08-28 |
| NeroTech | `nerotech` | `nerotech-neoforge-26.2-0.1.0-beta.1.jar` | `0.1.0-beta.1` | SI | 2026-08-28 |
| Not Enough Crashes | `notenoughcrashes` | `notenoughcrashes-neoforge-4.4.9+26.2.jar` | `4.4.9+26.2` | SI | 2026-08-28 |
| Occultism | `occultism` | `occultism-26.2-neoforge-1.251.1.jar` | `1.251.1` | SI (override, ver nota) | 2026-08-28 |
| Pantry for Blockheads | `pantryforblockheads` | `pantryforblockheads-neoforge-26.2-26.2.0.6.jar` | `26.2.0.6` | SI | 2026-08-28 |
| Player Activity View | `player_activity_view` | `player_activity_view-26.2-neoforge-26.2.0.57-1.1.0.jar` | `1.1.0` | PROPIO | 2026-08-28 |
| Player Animation Library | `player_animation_library` | `PlayerAnimationLibMerged-1.2.6+mc.26.2.jar` | `1.2.6+mc.26.2` | N/A (sin lang/ en el jar) | 2026-08-28 |
| PrickleMC | `prickle` | `PrickleMC-neoforge-MC26.2-26.2.0.3.jar` | `26.2.0.3` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Prism | `prism` | `Prism-26.2-neoforge-1.1.2.jar` | `1.1.2` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Puzzles Lib | `puzzleslib` | `PuzzlesLib-v26.2.3-mc26.2.x-NeoForge.jar` | `26.2.3` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Regalia Slots API | `regalia_slots_api` | `regalia_slots_api-26.2-neoforge-26.2.0.57-1.1.0.jar` | `1.1.0` | PROPIO | 2026-08-28 |
| Reliquary Reincarnations | `reliquary` | `reliquary-26.2-2.0.92.1568.jar` | `2.0.92` | SI | 2026-08-28 |
| Resource Pack Options | `respackopts` | `respackopts-26.2.1.jar` | `26.2.1` | SI | 2026-08-28 |
| Resourceful Lib | `resourcefullib` | `ResourcefulLib-5.0.3.jar` | `5.0.3` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Shogi | `shogi` | `shogi-neoforge-26.2-26.2.0.5.jar` | `26.2.0.5` | SI | 2026-08-28 |
| SKD Menu | `skd_menu` | `skd_menu-26.2-neoforge-26.2.0.57-1.2.4.jar` | `1.2.4` | PROPIO | 2026-08-28 |
| Smoothchunk mod | `smoothchunk` | `smoothchunk-26.1-4.2.jar` | `4.2` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Sodium | `sodium` | `sodium-neoforge-0.9.1+mc26.2.jar` | `0.9.1+mc26.2` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Sodium Extra | `sodium-extra` | `sodium-extra-neoforge-0.9.3+mc26.2.jar` | `0.9.3 (del nombre)` | SI (override) | 2026-08-28 |
| Sophisticated Backpacks | `sophisticatedbackpacks` | `sophisticatedbackpacks-26.2-3.25.92.2105.jar` | `3.25.92` | SI (override) | 2026-08-28 |
| Sophisticated Core | `sophisticatedcore` | `sophisticatedcore-26.2-1.4.104.2315.jar` | `1.4.104` | SI (override) | 2026-08-28 |
| Sophisticated Inventory Interactions | `sophisticatedinventoryinteractions` | `sophisticatedinventoryinteractions-26.2-0.1.18.205.jar` | `0.1.18` | SI (override) | 2026-08-28 |
| Sophisticated Storage | `sophisticatedstorage` | `sophisticatedstorage-26.2-1.5.113.2122.jar` | `1.5.113` | SI (override) | 2026-08-28 |
| Stellarity | `stellarity` | `Stellarity-5.5.5.jar` | `5.5.5` | SI (override) | 2026-08-28 |
| Stellarity (namespace `space`) | `space` | `Stellarity-5.5.5.jar` | `5.5.5` | N/A (mapa de ofuscación ~36k claves, no es texto de UI — no traducir; ver nota) | 2026-08-28 |
| Structure Essentials mod | `structureessentials` | `structureessentials-26.2-5.0.jar` | `5.0` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Structurify | `structurify` | `structurify-neoforge-2.0.34+mc26.2.jar` | `2.0.34` | SI | 2026-08-28 |
| SuperMartijn642's Core Lib | `supermartijn642corelib` | `supermartijn642corelib-1.1.24a-neoforge-mc26.2.jar` | `1.1.24+a` | SI | 2026-08-28 |
| Survival Instinct | `survival_instinct` | `Survival_Instinct_NeoForge_Port.jar` | `1.0.2-neoforge-26.2-private-port` | SI (override) | 2026-08-28 |
| Teleport Animation | `teleport_animation` | `teleport_animation-26.2-neoforge-26.2.0.57-1.2.0.jar` | `1.2.0` | PROPIO | 2026-08-28 |
| The Birth of Steve | `tbos` | `tbos-neoforge-26.2-0.7.1.jar` | `0.7.1` | SI (override) | 2026-08-28 |
| Theurgy | `theurgy` | `theurgy-26.2-neoforge-1.116.0.jar` | `1.116.0` | SI | 2026-08-28 |
| Tom's Simple Storage Mod | `toms_storage` | `toms_storage-26.2-2.11.1.jar` | `2.11.1` | SI | 2026-08-28 |
| Tower Waystone | `tower_waystone` | `tower_waystone-26.2-neoforge-26.2.0.57-1.1.0.jar` | `1.1.0` | PROPIO | 2026-08-28 |
| Travel Bites | `travel_bites` | `travelbites-2.0.0-neoforge-26.1.2.jar` | `2.0.0` | SI (override) | 2026-08-28 |
| TT20 | `tt20` | `tt20-0.8.4+mc26.1.1-neoforge.jar` | `0.8.4` | N/A (sin lang/ en el jar) | 2026-08-28 |
| UI Lib | `uilib` | `uilib-neoforge-21.1.1.jar` | `21.1.1` | SI | 2026-08-28 |
| Universal Bone Meal | `universalbonemeal` | `UniversalBoneMeal-v26.2.0-mc26.2.x-NeoForge.jar` | `26.2.0` | N/A (sin lang/ en el jar) | 2026-08-28 |
| Universal Enchantment Info | `uei` | `UniversalEnchantmentInfo-26.2-neoforge-1.2.0.jar` | `1.2.0` | SI | 2026-08-28 |
| Utility Core Admin | `utility_core_admin` | `utility_core_admin-26.2-neoforge-26.2.0.57-2.4.0.jar` | `2.4.0` | PROPIO | 2026-08-28 |
| Utility Core Fixes | `utility_core_fixes` | `utility_core_fixes-26.2-neoforge-26.2.0.57-2.5.1.jar` | `2.5.1` | PROPIO | 2026-08-28 |
| Utility Core HUD | `utility_core_hud` | `utility_core_hud-26.2-neoforge-26.2.0.57-1.0.1.jar` | `1.0.1` | PROPIO | 2026-08-28 |
| Utility Core QoL | `utility_core_qol` | `utility_core_qol-26.2-neoforge-26.2.0.57-2.4.0.jar` | `2.4.0` | PROPIO | 2026-08-28 |
| Variants&Ventures | `variantsandventures` | `variantsandventures-neoforge-1.0.26+mc26.2.jar` | `1.0.26` | SI | 2026-08-28 |
| Vellumli | `vellumli` | `vellumli-26.2-neoforge-26.2.0.57-1.2.0.jar` | `1.2.0` | PROPIO | 2026-08-28 |
| Visual Workbench | `visualworkbench` | `VisualWorkbench-v26.2.1-mc26.2.x-NeoForge.jar` | `26.2.1` | SI | 2026-08-28 |
| Waystones | `waystones` | `waystones-neoforge-26.2-26.2.0.9.jar` | `26.2.0.9` | SI (override) | 2026-08-28 |
| Wishful Recipes | `wishfulrecipes` | `wishfulrecipes-26.2-neoforge-1.jar` | `1` | SI | 2026-08-28 |
| Workhand Tools | `workhand_tools` | `workhand_tools-26.2-neoforge-26.2.0.57-1.22.4.jar` | `1.22.4` | SI (override) | 2026-08-28 |
| Workshop for Handsome Adventurer | `workshop_for_handsome_adventurer` | `workshop_for_handsome_adventurer--mc26.2--neoforge--1.36.0.jar` | `1.36.0` | SI (override) | 2026-08-28 |
| Xaero's Minimap | `xaerobetterpvp` | `xaerominimap-neoforge-26.2-26.4.2.jar` | `26.2 (del nombre)` | SI (override) | 2026-08-28 |
| Xaero's Minimap | `xaerominimap` | `xaerominimap-neoforge-26.2-26.4.2.jar` | `26.4.2` | SI (override) | 2026-08-28 |
| Xaero's World Map | `xaeroworldmap` | `xaeroworldmap-neoforge-26.2-1.44.2.jar` | `1.44.2` | SI | 2026-08-28 |
| YAML Config | `yamlconfig` | `yamlconfig-neoforge-21.1.0.jar` | `21.1.0` | SI | 2026-08-28 |
| YetAnotherConfigLib | `yet_another_config_lib_v3` | `yet_another_config_lib_v3-3.9.5+26.2-neoforge.jar` | `3.9.5+26.2-neoforge` | SI (override) | 2026-08-28 |
| Ancient Artifacts 2 | `ancient_artifacts` | `Ancient Artifacts 2 V2.5.5g for 1.21.6-26.2.jar` | `2.5.5g` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-04 |
| Better Party X Waystones | `better_party_x_waystones` | `better-party-x-waystones-neoforge-26.2-1.0.0.jar` | `1.0.0` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-04 |
| Bridging Mod | `bridgingmod` | `BridgingMod-2.7.0+26.2.neoforge-release.jar` | `2.7.0+26.2` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-03 |
| Cloth Config v26.2 API | `cloth_config` | `cloth-config-26.2.155.jar` | `26.2.155` | RENOMBRADO -> modid real del jar es `cloth-config2` (ver esa fila) | 2026-08-28 |
| Configurable | `configurable` | `configurable-3.5.2+26.2-neoforge.jar` | `3.5.2+26.2` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-04 |
| Configured | `configured` | `configured-neoforge-26.2-2.7.5.jar` | `2.7.5` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-04 |
| Connectivity Mod | `connectivity` | `connectivity-26.1-7.6.jar` | `7.6` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-03 |
| Curios API | `curios` | `curios-neoforge-15.0.0-beta.2+26.2.jar` | `15.0.0-beta.2+26.2` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-04 |
| Dungeons and Taverns Woodland Mansion Overhaul | `mr_dungeons_andtavernswoodlandmansionoverhaul` | `DnT-woodland-mansion-overhaul-2.1 [NeoForge].jar` | `2.1` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-03 |
| Enchanted Adventure | `adventureenchanting` | `adventureenchanting-0.1.0.jar` | `0.1.0` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-03 |
| FallingTree | `fallingtree` | `FallingTree-26.2-25.jar` | `25` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-03 |
| Grim kingdoms: structures & ruins | `mr_grim_kingdomsloststructuresruins` | `grim-kingdoms-lost-structures-ruins-2.0.3.jar` | `2.0.3` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-03 |
| Hammers and Excavators | `hammersandexcavators` | `hammersandexcavators-1.0.3-26.2.jar` | `1.0.3-26.2` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-03 |
| HopoBetterMineshaft | `hopo` | `HopoBetterMineshaft-[26.2]-1.3.7.jar` | `1.3.7` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-03 |
| HopoBetterRuinedPortals | `hoporp` | `HopoBetterRuinedPortals-[26.2]-1.5.1.jar` | `1.5.1` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-03 |
| HopoBetterUnderwaterRuins | `hopour` | `HopoBetterUnderwaterRuins-[26.2]-1.2.8.jar` | `1.2.8` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-03 |
| Kenny | `kenny` | `Kenny-6.0.0-neoforge+mc26.2.jar` | `6.0.0` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-03 |
| MoogsMissingVillages | `mmv` | `MoogsMissingVillages-1.21-2.1.2.jar` | `2.1.2` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-03 |
| Naraka | `naraka` | `naraka-neoforge-26.2-1.1.1.jar` | `1.1.1` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-03 |
| NetherPortalFix | `netherportalfix` | `netherportalfix-neoforge-26.2-26.2.0.1.jar` | `26.2.0.1` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-03 |
| Ore Vein Miner | `mr_ore_veinminer` | `ore-vein-miner-26.2snap.jar` | `26.1` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-03 |
| Repurposed Structures | `repurposed_structures` | `repurposed_structures-7.7.5+26.2-neoforge.jar` | `7.7.5+26.2-neoforge` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-04 |
| Right Click Harvest | `rightclickharvest` | `rightclickharvest-neoforge-4.6.2+26.2.x.jar` | `4.6.2+26.2.x` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-03 |
| The Lost City | `the_lost_city` | `the_lost_city-1.4.1-neoforge-1.26.1.jar` | `1.4.1` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-03 |
| TNT Foundry | `tntfoundry` | `tntfoundry-1.0.0.jar` | `1.0.0` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-03 |
| Towns and Towers | `t_and_t` | `t_and_t-fabric-neoforge-1.13.11.jar` | `1.13.11` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-03 |
| Utility Core (Admin) | `utility_core` | `utility_core_admin-26.2-neoforge-26.2.0.57-2.3.0.jar` | `2.3.0` | RENOMBRADO -> ahora `utility_core_admin/_fixes/_qol/_hud` (PROPIO, ver esas filas) | 2026-08-21 |
| Warlockery | `warlockery` | `warlockery-neoforge-1.4.0-LlaGuiT0-26.2.0.45.jar` | `1.4.0-LlaGuiT0-26.2.0.45` | RETIRADO DEL MODPACK (2026-08-28) | 2026-08-18 |
