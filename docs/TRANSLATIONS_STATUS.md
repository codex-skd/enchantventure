# Estado de traducciones — EnchantVenture Translations

> Generado leyendo el manifest real de cada JAR (`META-INF/neoforge.mods.toml` / `mods.toml` /
> `fabric.mod.json`) en `C:\Users\llagu\curseforge\minecraft\Instances\EnchantVenture\mods` (150 jars),
> el 2026-08-03.
>
> - `SI` = el mod ya trae `lang/es_es.json` propio, no requiere trabajo aquí.
> - `PENDIENTE` = falta `es_es.json`, candidato a traducir en este resource pack.
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
> Reproducir este escaneo: `python` con `tomllib` (3.11+), leer `META-INF/neoforge.mods.toml` (NeoForge),
> `META-INF/mods.toml` (Forge) o `fabric.mod.json` (Fabric) de cada jar para sacar `modid`/`name`/`version`,
> y comprobar si existe `assets/<modid>/lang/es_es.json` dentro del jar. 4 mods (`aiimprovements`,
> `apexcore`, `jade`, `justenoughprofessions`) declaran la versión como `${file.jarVersion}` en su manifest
> (variable que solo se resuelve al compilar) — para esos se usó la versión visible en el nombre del archivo.

Total: 150 mods · 33 ya con `es_ES` · 105 pendientes · 12 propios (fuera de alcance de este repo).

| Mod | modid | Archivo | Versión | Estado | Última revisión |
|---|---|---|---|---|---|
| Advanced Netherite | `advancednetherite` | `advancednetherite-neoforge-2.4.2-26.2.jar` | `2.4.2` | SI | 2026-08-03 |
| Ageforged Armor | `ageforged_armor` | `ageforged_armor-26.2-neoforge-1.1.3.jar` | `1.1.3` | PROPIO | 2026-08-03 |
| AI-Improvements | `aiimprovements` | `AI-Improvements-26.1.1-0.5.4.jar` | `0.5.4` (del nombre de archivo, el manifest no resuelve la variable) | PENDIENTE | 2026-08-03 |
| Ancient Artifacts 2 | `ancient_artifacts_mod` | `Ancient Artifacts 2 V2.5.5g for 1.21.6-26.2.jar` | `2.5.5g` | SI | 2026-08-03 |
| ApexCore | `apexcore` | `apexcore-26.2.0.jar` | `26.2.0` (del nombre de archivo, el manifest no resuelve la variable) | PENDIENTE | 2026-08-03 |
| Architectury | `architectury` | `architectury-neoforge-21.0.6.jar` | `21.0.6` | PENDIENTE | 2026-08-03 |
| Armor Cosmetic | `armor_cosmetic` | `armor_cosmetic-26.2-neoforge-1.0.3.jar` | `1.0.3` | PROPIO | 2026-08-03 |
| AttributeFix | `attributefix` | `AttributeFix-neoforge-MC26.2-26.2.0.1.jar` | `26.2.0.1` | PENDIENTE | 2026-08-03 |
| Balm | `balm` | `balm-neoforge-26.2-26.2.0.5.jar` | `26.2.0.5` | PENDIENTE | 2026-08-03 |
| Berezka API | `berezka_api` | `berezka_api-1.2.9.5-beta.3-neoforge-1.26.2.jar` | `1.2.9.5-beta.3` | PENDIENTE | 2026-08-03 |
| Better Combat | `bettercombat` | `bettercombat-neoforge-3.2.2+26.2.jar` | `3.2.2` | SI | 2026-08-03 |
| Better Compatibility Checker | `bcc` | `better-compatability-checker-neoforge-26.2.0.1.jar` | `26.2.0.1` | PENDIENTE | 2026-08-03 |
| Better Connections | `better_connections` | `better_connections-26.2-neoforge-1.0.0.jar` | `1.0.0` | PROPIO | 2026-08-03 |
| Better Party | `better_party` | `better-party-neoforge-26.2-1.1.1.jar` | `1.1.1` | PENDIENTE | 2026-08-03 |
| Better Party X Xaero's World Map | `better_party_x_xaeros_world_map` | `better-party-x-xaeros-world-map-neoforge-26.2-1.0.0.jar` | `1.0.0` | PENDIENTE | 2026-08-03 |
| Better Villager Animations | `bettervillageranimations` | `better-villager-animations-neoforge-26.2.jar` | `1.0.0` | PENDIENTE | 2026-08-03 |
| Bridging Mod | `bridgingmod` | `BridgingMod-2.7.0+26.2.neoforge-release.jar` | `2.7.0+26.2` | PENDIENTE | 2026-08-03 |
| Carry Mechanics | `carry_mechanics` | `carry_mechanics-26.2-neoforge-1.0.4.jar` | `1.0.4` | PROPIO | 2026-08-03 |
| clientcrafting mod | `clientcrafting` | `clientcrafting-26.1-2.1.jar` | `2.1` | PENDIENTE | 2026-08-03 |
| Cloth Config v26.2 API | `cloth_config` | `cloth-config-26.2.155.jar` | `26.2.155` | SI | 2026-08-03 |
| CoK_Tools | `coktools` | `CoKTools-Neoforge-mc26.2-26.2.0.2.jar` | `26.2.0.2` | PENDIENTE | 2026-08-03 |
| Complementary Core | `complementary_core` | `cc-2.3.1-neoforge_1.21.5-26.1.2.jar` | `2.3.1` | PENDIENTE | 2026-08-03 |
| Complementary Structures: Towers | `cs_towers` | `cs_towers-0.2.0-neoforge_1.21.x.jar` | `0.2.0` | PENDIENTE | 2026-08-03 |
| Configured | `configured` | `configured-neoforge-26.2-2.7.5.jar` | `2.7.5` | SI | 2026-08-03 |
| Connected Glass | `connectedglass` | `connectedglass-1.1.14-neoforge-mc26.2.jar` | `1.1.14` | SI | 2026-08-03 |
| Connectivity Mod | `connectivity` | `connectivity-26.1-7.6.jar` | `7.6` | PENDIENTE | 2026-08-03 |
| Corail Tombstone | `tombstone` | `tombstone-neoforge-26.2-9.9.3.jar` | `9.9.3` | SI | 2026-08-03 |
| Crafting Tweaks | `craftingtweaks` | `craftingtweaks-neoforge-26.2-26.2.0.2.jar` | `26.2.0.2` | PENDIENTE | 2026-08-03 |
| Cristel Lib | `cristellib` | `cristellib-neoforge-26.2-3.1.10.jar` | `3.1.10` | PENDIENTE | 2026-08-03 |
| Cupboard mod | `cupboard` | `cupboard-26.2-3.9.jar` | `3.9` | PENDIENTE | 2026-08-03 |
| Curios API | `curios` | `curios-neoforge-15.0.0-beta.2+26.2.jar` | `15.0.0-beta.2+26.2` | SI | 2026-08-03 |
| CustomSkinLoader Bootstrap | `customskinloader-bootstrap` | `CustomSkinLoader_Universal-15.0.1.jar` | `15.0.1` | PENDIENTE | 2026-08-03 |
| Cyclops Core | `cyclopscore` | `cyclopscore-26.2-neoforge-1.30.0-1066.jar` | `1.30.0-1066` | SI | 2026-08-03 |
| Data Miner | `data_miner` | `data_miner-26.2-neoforge-1.0.0.jar` | `1.0.0` | PROPIO | 2026-08-03 |
| Deimos | `deimos` | `deimos-26.2-neoforge-2.7.jar` | `2.7` | PENDIENTE | 2026-08-03 |
| DrZhark's Mo'Creatures | `mocreatures` | `mocreatures-neoforge-26.2.0+26.2.jar` | `26.2.0` | PENDIENTE | 2026-08-03 |
| Dungeons and Taverns | `mr_dungeons_andtaverns` | `dungeons-and-taverns-5.3.0 [NeoForge].jar` | `5.3.0` | SI | 2026-08-03 |
| Dungeons and Taverns Ancient City Overhaul | `mr_dungeons_andtavernsancientcityoverhaul` | `DnT-ancient-city-overhaul-3.4 [NeoForge].jar` | `3.4` | PENDIENTE | 2026-08-03 |
| Dungeons and Taverns Nether Fortress Overhaul | `mr_dungeons_andtavernsnetherfortressoverhaul` | `DnT-nether-fortress-overhaul-v3.1 [NeoForge].jar` | `1-v3.1` | PENDIENTE | 2026-08-03 |
| Dungeons and Taverns Pillager Outpost Overhaul | `mr_dungeons_andtavernspillageroutpostoverhaul` | `DnT-pillager-outpost-overhaul-v3.3 [NeoForge].jar` | `1-v3.3` | PENDIENTE | 2026-08-03 |
| Dungeons and Taverns Woodland Mansion Overhaul | `mr_dungeons_andtavernswoodlandmansionoverhaul` | `DnT-woodland-mansion-overhaul-2.1 [NeoForge].jar` | `2.1` | PENDIENTE | 2026-08-03 |
| Echo Relics | `echorelics` | `echorelics-0.1.0.jar` | `0.1.0` | PENDIENTE | 2026-08-03 |
| Ecologics | `ecologics` | `Ecologics-NeoFab-26.2-2.6.0.jar` | `2.6.0` | SI | 2026-08-03 |
| Enchanted Adventure | `adventureenchanting` | `adventureenchanting-0.1.0.jar` | `0.1.0` | PENDIENTE | 2026-08-03 |
| EnchantmentDescriptions | `enchdesc` | `EnchantmentDescriptions-neoforge-MC26.2-26.2.0.1.jar` | `26.2.0.1` | SI | 2026-08-03 |
| Equivalent Legacy | `equivalent_legacy` | `equivalent_legacy-26.2-neoforge-1.0.2.jar` | `1.0.2` | PROPIO | 2026-08-03 |
| EvilCraft | `evilcraft` | `evilcraft-26.2-neoforge-1.2.98-1004.jar` | `1.2.98-1004` | SI | 2026-08-03 |
| Explorer's Compass | `explorerscompass` | `ExplorersCompass-26.2-3.3.0-neoforge.jar` | `26.2-3.3.0-neoforge` | SI | 2026-08-03 |
| FallingTree | `fallingtree` | `FallingTree-26.2-25.jar` | `25` | PENDIENTE | 2026-08-03 |
| Fast IP Ping | `fastipping` | `fast-ip-ping-v1.0.11-mc26.1.2.jar` | `1.0.11` | PENDIENTE | 2026-08-03 |
| fastasyncworldsave mod | `fastasyncworldsave` | `fastasyncworldsave-26.2-2.6.jar` | `2.6` | PENDIENTE | 2026-08-03 |
| Ferrite Core | `ferritecore` | `ferritecore-9.0.0-neoforge.jar` | `9.0.0` | PENDIENTE | 2026-08-03 |
| Fish of Thieves | `fishofthieves` | `fish_of_thieves-mc26.2-v26.2.1.1-neoforge.jar` | `26.2.1.1` | PENDIENTE | 2026-08-03 |
| FokusAPI | `fokusapi` | `FokusAPI-v4.5_MOD.jar` | `4.5` | PENDIENTE | 2026-08-03 |
| Formations | `formations` | `formations-1.0.4-neoforge-mc26.2.jar` | `1.0.4` | PENDIENTE | 2026-08-03 |
| Formations Nether | `formationsnether` | `formationsnether-1.0.5a-mc1.21+.jar` | `1.0.5+a` | PENDIENTE | 2026-08-03 |
| Formations Overworld | `formationsoverworld` | `formationsoverworld-1.0.5a-mc1.21+.jar` | `1.0.5+a` | PENDIENTE | 2026-08-03 |
| Fusion | `fusion` | `fusion-1.3.12-neoforge-mc26.2.jar` | `1.3.12` | PENDIENTE | 2026-08-03 |
| Gateway of Doom | `gateway_of_doom` | `gatewayofdoom-neoforge-26.2-2.1.1.jar` | `2.1.1` | SI | 2026-08-03 |
| Gateway of Doom X Xaero's World Map | `gateway_of_doom_x_xaeros_world_map` | `gateway_of_doom_x_xaeros_world_map-neoforge-26.2-1.0.0.jar` | `1.0.0` | PENDIENTE | 2026-08-03 |
| GeckoLib 5 | `geckolib` | `geckolib-neoforge-26.2-5.5.3.jar` | `5.5.3` | PENDIENTE | 2026-08-03 |
| GlitchCore | `glitchcore` | `GlitchCore-neoforge-26.2-26.2.0.0.0.jar` | `26.2.0.0.0` | PENDIENTE | 2026-08-03 |
| Gpu memory leak fix | `gpumemleakfix` | `gpumemleakfix-26.1-1.9.jar` | `1.9` | PENDIENTE | 2026-08-03 |
| Grim kingdoms: structures & ruins | `mr_grim_kingdomsloststructuresruins` | `grim-kingdoms-lost-structures-ruins-2.0.3.jar` | `2.0.3` | PENDIENTE | 2026-08-03 |
| Hammers and Excavators | `hammersandexcavators` | `hammersandexcavators-1.0.3-26.2.jar` | `1.0.3-26.2` | PENDIENTE | 2026-08-03 |
| HopoBetterMineshaft | `hopo` | `HopoBetterMineshaft-[26.2]-1.3.7.jar` | `1.3.7` | PENDIENTE | 2026-08-03 |
| HopoBetterRuinedPortals | `hoporp` | `HopoBetterRuinedPortals-[26.2]-1.5.1.jar` | `1.5.1` | PENDIENTE | 2026-08-03 |
| HopoBetterUnderwaterRuins | `hopour` | `HopoBetterUnderwaterRuins-[26.2]-1.2.8.jar` | `1.2.8` | PENDIENTE | 2026-08-03 |
| Iceberg | `iceberg` | `Iceberg-26.2-neoforge-1.4.2.1.jar` | `1.4.2.1` | PENDIENTE | 2026-08-03 |
| ImmediatelyFast | `immediatelyfast` | `ImmediatelyFast-NeoForge-1.16.2+26.2.jar` | `1.16.2+26.2` | PENDIENTE | 2026-08-03 |
| Immersive Armors | `immersive_armors` | `immersive_armors-1.8.2+26.2-neoforge.jar` | `1.8.2+26.2` | SI | 2026-08-03 |
| Info TAB | `info_tab` | `info_tab-26.2-neoforge-1.0.0.jar` | `1.0.0` | PROPIO | 2026-08-03 |
| Inventory Essentials | `inventoryessentials` | `inventoryessentials-neoforge-26.2-26.2.0.3.jar` | `26.2.0.3` | PENDIENTE | 2026-08-03 |
| Iris | `iris` | `iris-neoforge-1.11.2+mc26.2.jar` | `1.11.2+mc26.2` | SI | 2026-08-03 |
| Iris Shader Folder | `iris_shader_folder` | `iris_shader_folder-1.4.1-neoforge.jar` | `1.4.1-neoforge` | PENDIENTE | 2026-08-03 |
| It Takes a Pillage Continuation | `takesapillage` | `takesapillage-neoforge-1.0.12+mc26.2.jar` | `1.0.12` | PENDIENTE | 2026-08-03 |
| Jade | `jade` | `Jade-mc26.2-NeoForge-26.2.8.jar` | `26.2.8` (del nombre de archivo, el manifest no resuelve la variable) | SI | 2026-08-03 |
| JamLib | `jamlib` | `jamlib-neoforge-2.3.1+26.2.x.jar` | `2.3.1+26.2.x` | PENDIENTE | 2026-08-03 |
| Just Enough Items | `jei` | `jei-26.2-neoforge-30.15.0.121.jar` | `30.15.0.121` | SI | 2026-08-03 |
| Just Enough Professions (JEP) | `justenoughprofessions` | `JustEnoughProfessions-neoforge-26.2-12.0.0.jar` | `12.0.0` (del nombre de archivo, el manifest no resuelve la variable) | PENDIENTE | 2026-08-03 |
| Kenny | `kenny` | `Kenny-6.0.0-neoforge+mc26.2.jar` | `6.0.0` | PENDIENTE | 2026-08-03 |
| Legendary Tooltips | `legendarytooltips` | `LegendaryTooltips-26.2-neoforge-1.6.2.jar` | `1.6.2` | PENDIENTE | 2026-08-03 |
| Lithostitched | `lithostitched` | `lithostitched-1.7.13-neoforge-26.2.jar` | `1.7.13` | PENDIENTE | 2026-08-03 |
| Lootr | `lootr` | `lootr-neoforge-26.2-1.24.39.121.jar` | `1.24.39.121` | SI | 2026-08-03 |
| Marsward | `marsward` | `marsward-1.0.6.jar` | `1.0.6` | PENDIENTE | 2026-08-03 |
| Modonomicon | `modonomicon` | `modonomicon-26.2-neoforge-2.2.0.jar` | `2.2.0` | PENDIENTE | 2026-08-03 |
| Moog's Structure Lib | `moogs_structures` | `moogs_structures-neoforge-26.2-3.0.6.jar` | `3.0.6` | PENDIENTE | 2026-08-03 |
| MoogsEndStructures | `mes` | `MoogsEndStructures-1.21-2.0.3.jar` | `2.0.3` | PENDIENTE | 2026-08-03 |
| MoogsMissingVillages | `mmv` | `MoogsMissingVillages-1.21-2.1.2.jar` | `2.1.2` | PENDIENTE | 2026-08-03 |
| MoogsNetherStructures | `mns` | `MoogsNetherStructures-1.21-3.0.0.jar` | `3.0.0` | PENDIENTE | 2026-08-03 |
| MoogsTemplesReimagined | `mtr` | `MoogsTemplesReimagined-1.21-1.1.3.jar` | `1.1.3` | PENDIENTE | 2026-08-03 |
| MoogsVoyagerStructures | `mvs` | `MoogsVoyagerStructures-1.21-5.0.11.jar` | `5.0.11` | PENDIENTE | 2026-08-03 |
| Mouse Tweaks | `mousetweaks` | `MouseTweaks-neoforge-mc26.2-2.31.jar` | `2.31` | PENDIENTE | 2026-08-03 |
| Mutant Monsters | `mutantmonsters` | `MutantMonsters-v26.2.1-mc26.2.x-NeoForge.jar` | `26.2.1` | SI | 2026-08-03 |
| Naraka | `naraka` | `naraka-neoforge-26.2-1.1.1.jar` | `1.1.1` | PENDIENTE | 2026-08-03 |
| Nature's Compass | `naturescompass` | `NaturesCompass-26.2-3.3.0-neoforge.jar` | `26.2-3.3.0-neoforge` | SI | 2026-08-03 |
| NeroAgriculture | `neroagriculture` | `neroagriculture-neoforge-26.2-0.1.0-beta.1.jar` | `0.1.0-beta.1` | PENDIENTE | 2026-08-03 |
| NeroDecor | `nerodecor` | `nerodecor-neoforge-26.2-0.1.0-beta.1.jar` | `0.1.0-beta.1` | PENDIENTE | 2026-08-03 |
| Neroland Core | `nerolandcore` | `nerolandcore-neoforge-26.2-1.9.0.jar` | `1.9.0` | PENDIENTE | 2026-08-03 |
| NeroLink | `nerolink` | `nerolink-neoforge-26.2-0.0.1-alpha.2.jar` | `0.0.1-alpha.2` | PENDIENTE | 2026-08-03 |
| NeroLogistics | `nerologistics` | `nerologistics-neoforge-26.2-0.1.0-alpha.1.jar` | `0.1.0-alpha.1` | PENDIENTE | 2026-08-03 |
| NeroQuests | `neroquests` | `neroquests-neoforge-26.2-0.1.0-beta.1.jar` | `0.1.0-beta.1` | PENDIENTE | 2026-08-03 |
| NeroSpace | `nerospace` | `nerospace-neoforge-26.2-1.0.1.jar` | `1.0.1` | PENDIENTE | 2026-08-03 |
| NeroTech | `nerotech` | `nerotech-neoforge-26.2-0.1.0-beta.1.jar` | `0.1.0-beta.1` | PENDIENTE | 2026-08-03 |
| NetherPortalFix | `netherportalfix` | `netherportalfix-neoforge-26.2-26.2.0.1.jar` | `26.2.0.1` | PENDIENTE | 2026-08-03 |
| Not Enough Crashes | `notenoughcrashes` | `notenoughcrashes-neoforge-4.4.9+26.2.jar` | `4.4.9+26.2` | PENDIENTE | 2026-08-03 |
| Ore Vein Miner | `mr_ore_veinminer` | `ore-vein-miner-26.2snap.jar` | `26.1` | PENDIENTE | 2026-08-03 |
| Pantry for Blockheads | `pantryforblockheads` | `pantryforblockheads-neoforge-26.2-26.2.0.5.jar` | `26.2.0.5` | PENDIENTE | 2026-08-03 |
| Player Activity View | `player_activity_view` | `player_activity_view-26.2-neoforge-1.0.0.jar` | `1.0.0` | PROPIO | 2026-08-03 |
| Player Animation Library | `player_animation_library` | `PlayerAnimationLibMerged-1.2.5+mc.26.2.jar` | `1.2.5+mc.26.2` | PENDIENTE | 2026-08-03 |
| PrickleMC | `prickle` | `PrickleMC-neoforge-MC26.2-26.2.0.3.jar` | `26.2.0.3` | PENDIENTE | 2026-08-03 |
| Prism | `prism` | `Prism-26.2-neoforge-1.1.2.jar` | `1.1.2` | PENDIENTE | 2026-08-03 |
| Puzzles Lib | `puzzleslib` | `PuzzlesLib-v26.2.1-mc26.2.x-NeoForge.jar` | `26.2.1` | PENDIENTE | 2026-08-03 |
| Reliquary Reincarnations | `reliquary` | `reliquary-26.2-2.0.89.1531.jar` | `2.0.89` | PENDIENTE | 2026-08-03 |
| Repurposed Structures | `repurposed_structures` | `repurposed_structures-7.7.5+26.2-neoforge.jar` | `7.7.5+26.2-neoforge` | SI | 2026-08-03 |
| Resourceful Lib | `resourcefullib` | `ResourcefulLib-5.0.3.jar` | `5.0.3` | PENDIENTE | 2026-08-03 |
| Right Click Harvest | `rightclickharvest` | `rightclickharvest-neoforge-4.6.2+26.2.x.jar` | `4.6.2+26.2.x` | PENDIENTE | 2026-08-03 |
| Shogi | `shogi` | `shogi-neoforge-26.2-26.2.0.4.jar` | `26.2.0.4` | PENDIENTE | 2026-08-03 |
| SKD Menu | `skd_menu` | `skd_menu-26.2-neoforge-1.2.0.jar` | `1.2.0` | PROPIO | 2026-08-03 |
| Smoothchunk mod | `smoothchunk` | `smoothchunk-26.1-4.2.jar` | `4.2` | PENDIENTE | 2026-08-03 |
| Sodium | `sodium` | `sodium-neoforge-0.9.1+mc26.2.jar` | `0.9.1+mc26.2` | PENDIENTE | 2026-08-03 |
| Sodium Extra | `sodium_extra` | `sodium-extra-neoforge-0.9.3+mc26.2.jar` | `0.9.3+mc26.2` | SI | 2026-08-03 |
| Sophisticated Backpacks | `sophisticatedbackpacks` | `sophisticatedbackpacks-26.2-3.25.83.2018.jar` | `3.25.83` | SI | 2026-08-03 |
| Sophisticated Core | `sophisticatedcore` | `sophisticatedcore-26.2-1.4.90.2199.jar` | `1.4.90` | SI | 2026-08-03 |
| Sophisticated Storage | `sophisticatedstorage` | `sophisticatedstorage-26.2-1.5.101.2028.jar` | `1.5.101` | SI | 2026-08-03 |
| Stellarity | `stellarity` | `Stellarity-5.5.4.jar` | `5.5.4` | SI | 2026-08-03 |
| Structure Essentials mod | `structureessentials` | `structureessentials-26.2-5.0.jar` | `5.0` | PENDIENTE | 2026-08-03 |
| Structurify | `structurify` | `structurify-neoforge-2.0.30+mc26.2.jar` | `2.0.30` | PENDIENTE | 2026-08-03 |
| SuperMartijn642's Core Lib | `supermartijn642corelib` | `supermartijn642corelib-1.1.22a-neoforge-mc26.2.jar` | `1.1.22+a` | PENDIENTE | 2026-08-03 |
| Teleport Animation | `teleport_animation` | `teleport_animation-26.2-neoforge-1.0.1.jar` | `1.0.1` | PROPIO | 2026-08-03 |
| The Birth of Steve | `tbos` | `tbos-neoforge-26.2-0.4.0.jar` | `0.4.0` | PENDIENTE | 2026-08-03 |
| The Lost City | `the_lost_city` | `the_lost_city-1.4.1-neoforge-1.26.1.jar` | `1.4.1` | PENDIENTE | 2026-08-03 |
| TNT Foundry | `tntfoundry` | `tntfoundry-1.0.0.jar` | `1.0.0` | PENDIENTE | 2026-08-03 |
| Tom's Simple Storage Mod | `toms_storage` | `toms_storage-26.2-2.11.1.jar` | `2.11.1` | PENDIENTE | 2026-08-03 |
| Tower Waystone | `tower_waystone` | `tower_waystone-26.2-neoforge-1.0.1.jar` | `1.0.1` | PROPIO | 2026-08-03 |
| Towns and Towers | `t_and_t` | `t_and_t-fabric-neoforge-1.13.11.jar` | `1.13.11` | PENDIENTE | 2026-08-03 |
| UI Lib | `uilib` | `uilib-neoforge-21.1.1.jar` | `21.1.1` | PENDIENTE | 2026-08-03 |
| Universal Bone Meal | `universalbonemeal` | `UniversalBoneMeal-v26.2.0-mc26.2.x-NeoForge.jar` | `26.2.0` | PENDIENTE | 2026-08-03 |
| Universal Enchantment Info | `uei` | `UniversalEnchantmentInfo-26.2-neoforge-1.2.0.jar` | `1.2.0` | PENDIENTE | 2026-08-03 |
| Utility Core | `utility_core` | `utility_core-26.2-neoforge-1.11.0.jar` | `1.11.0` | PROPIO | 2026-08-03 |
| Variants&Ventures | `variantsandventures` | `variantsandventures-neoforge-1.0.26+mc26.2.jar` | `1.0.26` | PENDIENTE | 2026-08-03 |
| Visual Workbench | `visualworkbench` | `VisualWorkbench-v26.2.1-mc26.2.x-NeoForge.jar` | `26.2.1` | PENDIENTE | 2026-08-03 |
| Warlockery | `warlockery` | `warlockery-neoforge-1.2.2.jar` | `1.2.2` | SI | 2026-08-03 |
| Waystones | `waystones` | `waystones-neoforge-26.2-26.2.0.7.jar` | `26.2.0.7` | SI | 2026-08-03 |
| Wishful Recipes | `wishfulrecipes` | `wishfulrecipes-26.2-neoforge-0.2.2.jar` | `0.2.2` | PENDIENTE | 2026-08-03 |
| Xaero's Minimap | `xaerominimap` | `xaerominimap-neoforge-26.2-26.4.2.jar` | `26.4.2` | SI | 2026-08-03 |
| Xaero's World Map | `xaeroworldmap` | `xaeroworldmap-neoforge-26.2-1.44.2.jar` | `1.44.2` | PENDIENTE | 2026-08-03 |
| YAML Config | `yamlconfig` | `yamlconfig-neoforge-21.1.0.jar` | `21.1.0` | PENDIENTE | 2026-08-03 |
| YetAnotherConfigLib | `yet_another_config_lib_v3` | `yet_another_config_lib_v3-3.9.5+26.2-neoforge.jar` | `3.9.5+26.2-neoforge` | SI | 2026-08-03 |
