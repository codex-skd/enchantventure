# Flujo de trabajo — EnchantVenture Pack (Resource Pack)

> **Versión del workflow**: 1.17.1 (codex-docs)
> Este archivo pertenece al proyecto **EnchantVenture Pack**. Cambios aquí solo afectan a este proyecto.
> **Trabaja directamente con este archivo**: es el workflow operativo del resource pack, autocontenido. No leas `codex-docs/WORKFLOW_AGENT.md` ni `WORKFLOW_GENERIC.md` de forma rutinaria.
> On-demand (solo si la tarea lo necesita): `codex-docs/reference/CURSEFORGE.md` (formato HTML al publicar), `codex-docs/reference/REPO_SETUP.md` (setup único de repo).

## Específico del resource pack

| Dato | Valor |
|---|---|
| Nombre del proyecto (`version.txt`) | `EnchantVenture Pack` |
| Display name (Title Case) | `EnchantVenture Pack` |
| Versión de Minecraft | `26.2` |
| Pack format | `88` (`pack.mcmeta`; desde 1.21.9/26.x usa `min_format`/`max_format` en lugar de `pack_format` — corregido en v1.0.0-beta.1) |
| Rama de trabajo | `minecraft/26.2/resourcepack/production` |
| Rama pública hermana | `minecraft/26.2/resourcepack/main` (protegida, la escribe CI/CD) |
| Instancia CurseForge de referencia | `C:\Users\llagu\curseforge\minecraft\Instances\(Traducciones) EnchantVenture\mods` |
| Modpack objetivo | https://www.curseforge.com/minecraft/modpacks/enchantventure |
| Repositorio | https://gitlab.com/stalking-dragons/minecraft/enchantventure-pack.git |

## Qué es este proyecto

Resource pack **client-side** de la modpack EnchantVenture (Minecraft 26.2), solo de traducciones:

- **Traducciones** al español (`es_ES`) para los mods de la modpack que no traen su propio
  `lang/es_es.json`. No modifica ningún JAR ni mod — solo añade/complementa `assets/<modid>/lang/es_es.json`.

No es un datapack (eso es `EnchantVenture_fixes`, repo hermano).

> **Nota histórica**: entre v1.0.0-beta.1 y v1.0.0-beta.6 el pack incluyó también el "Enchanting Table
> Magic Circle" de Jacosvaldo (retexturizado animado de la mesa de encantamientos vía Respackopts).
> Se retiró en 1.0.0-beta.7 porque la animación de textura custom de OptiFine (parcheo `from/to` de
> frames) no renderizaba correctamente con EMF/ETF en 26.2 (artefactos de textura sin recortar). No
> reintroducir sin resolver antes esa incompatibilidad.

## Diferencias con un mod NeoForge o con el datapack de fixes

| Aspecto | Mod | Datapack (`EnchantVenture_fixes`) | Resource pack (este repo) |
|---|---|---|---|
| Build | `./gradlew.bat clean build` → JAR | `python build_fix_pack.py` → ZIP | `python build_pack.py` → ZIP |
| Artefacto | `build/libs/<mod_id>-...-<version>.jar` | `build/EnchantVenture_fixes-<version>.zip` | `build/EnchantVenture_Pack-<version>.zip` |
| Versión | `mod_version` en `gradle.properties` | `version.txt` | `version.txt` (única fuente de verdad) |
| Contenido versionado | `src/` | `datapack/` (generado desde JARs) | `resourcepack/` (traducciones curadas a mano) |
| pack_format | — | `107` (datapack) | `88` (resource pack — numeración distinta a la de datapacks; `min_format`/`max_format` desde 26.x) |
| gameVersions CurseForge | `["Client", "Server", "26.2", "NeoForge"]` | `["Datapack", "26.2"]` | `["26.2"]` (categoría Resource Packs) |
| Tag | `<mc>-neoforge-<version>` | `26.2-<version>` | `26.2-<version>` |
| docs/curseforge | project_description / project_vars / versions | idéntica | idéntica |

## Estructura del proyecto

`build_pack.py` (valida JSON y empaqueta `resourcepack/` → ZIP) · `version.txt` ·
`resourcepack/` (contenido real del pack, versionado: `pack.mcmeta`, `pack.png`,
`assets/<modid>/lang/es_es.json`) ·
`build/` (no versionado, solo el ZIP) · `temp/` (no versionado, zona de trabajo para analizar JARs) ·
`lib_ext/` (no versionado, packs externos de referencia — histórico, ver nota del círculo mágico arriba) ·
`docs/WORKFLOW...` + `docs/curseforge/` + `docs/TRANSLATIONS_STATUS.md` · `CHANGELOG.md` · `README.md`.

`ageforged_armor`, `armor_cosmetic`, `better_connections`, `carry_mechanics`, `data_miner`, `equivalent_legacy`,
`info_tab`, `player_activity_view`, `skd_menu`, `teleport_animation`, `tower_waystone`, `utility_core` son mods
**propios** de Stalking Dragons (carpeta hermana en `Mods_Minecraft/`): su traducción se añade directamente en
el mod (`assets/<modid>/lang/es_es.json` dentro de su propio repo), **no** en este resource pack. No reintroducir
esas traducciones aquí.

## Flujo por mod (tarea recurrente)

Trabajar `docs/TRANSLATIONS_STATUS.md` de arriba a abajo, un mod `PENDIENTE` cada vez:

1. **Extraer** el `lang/en_us.json` del JAR del mod a `temp/<modid>/en_us.json`:
   ```bash
   cd "C:\Users\llagu\curseforge\minecraft\Instances\(Traducciones) EnchantVenture\mods"
   unzip -p "<jar>" "assets/<modid>/lang/en_us.json" > "G:\Proyectos\Mods_Minecraft\EnchantVenture\temp\<modid>\en_us.json"
   ```
   Confirmar primero el `modid` real (puede no coincidir con el nombre del jar): `unzip -l "<jar>" | grep lang/`.
2. **Traducir** todas las claves a español neutro/es_ES, coherente con el resto de la modpack y con el
   glosario de Minecraft (términos ya establecidos: "yunque", "encantamiento", "poción", etc.) y con
   `resourcepack/assets/*/lang/es_es.json` ya existentes en este repo (reusar terminología entre mods).
3. **Guardar** el resultado en `resourcepack/assets/<modid>/lang/es_es.json` (JSON con las mismas claves
   que `en_us.json`, indentado a 2 espacios, `ensure_ascii=false`/UTF-8 real, sin BOM).
4. **Actualizar** `docs/TRANSLATIONS_STATUS.md`: mover la fila del mod a `SI (<fecha>)`.
5. **Build y validar**:
   ```bash
   python build_pack.py
   ```
6. **Commit**:
   ```bash
   git add -A
   git commit -m "feat(<modid>): add es_ES translation

   v<version>"
   git push
   ```
   Un commit por mod (o por lote pequeño y relacionado) — no acumular decenas de mods en un solo commit.

No usar Ollama para pre-filtrar los `en_us.json` de mods (son de referencia y pequeños — bajo el umbral de
~300 líneas/20KB de la regla general); si algún mod tiene un `en_us.json` inusualmente grande, sí aplica.

## Versionado

- Beta `0.0.0-beta.X` · Release `X.Y.Z` (SemVer)
- Versión en `version.txt`. ZIP: `EnchantVenture_Pack-<version>.zip`
- Primer versionado: `0.0.0-beta.1`
- Criterio de bump: no hay una cadencia fija por mod traducido; el usuario decide cuándo se acumula
  suficiente contenido para justificar una nueva beta/release y subida a CurseForge.

## Commits (Conventional Commits)

`<tipo>[<ámbito>]: <descripción>` · tipos `feat fix refactor docs chore style perf test` · ámbito = `modid`
cuando aplica a un mod concreto · el mensaje incluye la versión (`v<version>`).

## Tags

Cada subida a CurseForge crea tag: beta `26.2-beta.X` · release `26.2-X.Y.Z`.

## Flujo por tarea

**0. CurseForge — creación del proyecto** ✅ hecho. `project_id` `1638251`, categoría `Data Packs` (dentro
de la clase Resource Packs — el resto de categorías de esa clase son de resolución y no aplican), logo en
`resourcepack/pack.png`. Detalle en `docs/curseforge/create_project_form.md` y `docs/curseforge/project_vars.md`.
Pendiente solo confirmar el `gameVersionId` en la primera subida real.

**1. Desarrollo** (por mod, ver "Flujo por mod" arriba)

```bash
git checkout minecraft/26.2/resourcepack/production
python build_pack.py
git add -A
git commit -m "feat(<modid>): add es_ES translation

v<version>"
git push
```

**2. CurseForge** — solo si el usuario confirma:
- Bump `version.txt` → `python build_pack.py`
- Release notes `docs/curseforge/versions/<version>.md` (HTML) + actualizar `CHANGELOG.md`
- Commit `chore: bump version to <version>` → tag `26.2-<version>` → push
- Subir ZIP: `powershell -File scripts/curseforge-upload.ps1` (desde este repo)
- Formato HTML de descripciones/changelog: `codex-docs/reference/CURSEFORGE.md`

**3. Release estable** — bump `X.Y.Z` + tag.

**4. Graphify** — tras cada push a remoto. Versión 0.9.12: **`build` no existe**, usar `extract` (1ª vez) o `update . --force` (tras cambios):

```bash
GRAPHIFY="C:\Users\llagu\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\LocalCache\local-packages\Python313\Scripts\graphify.exe"
"$GRAPHIFY" update . --force
git add graphify-out/ && git commit -m "chore: update knowledge graph" && git push
```

Leer siempre `GRAPH_REPORT.md`, nunca `graph.json`/`graph.html` (pesan >1MB). Sin copias fechadas de `graphify-out/`. Backend LLM: `codex-docs/reference/GRAPHIFY.md`.

## Buenas prácticas

- Un commit por mod traducido (o lote pequeño relacionado) · commit+push tras cada cambio funcional y de docs
- `python build_pack.py` antes de subir (valida JSON y pack_format) · versionar antes de CurseForge · CHANGELOG al día
- `docs/TRANSLATIONS_STATUS.md` siempre al día — es la fuente de verdad de qué falta
- No traducir mods `PROPIO` aquí (van en su propio repo) ni mods ya marcados `SI`
- El ZIP resultante debe tener `pack.mcmeta` en la raíz (carga directa en `resourcepacks/`)
- Sin basura en repo (`nul`, `*.zip` sueltos en raíz, `temp/`) · `.gitignore` excluye `build/` y `temp/`
- README en inglés siempre actualizado

## Idioma

| Ámbito | Idioma |
|---|---|
| código, logs, commits | en-US |
| README.md | en-US |
| docs internas (docs/, CHANGELOG, este archivo) | es-ES |
| CurseForge | en-US |
| Contenido traducido (`assets/*/lang/es_es.json`) | es-ES |
