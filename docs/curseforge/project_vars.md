# CurseForge — Variables del proyecto

> **Pendiente de creación.** El proyecto de CurseForge para "EnchantVenture Translations" todavía no existe.
> Hay que crearlo manualmente en la web (logo, summary, descripción general del resource pack) antes de
> poder subir la primera versión. Ver tarea "0. CurseForge — creación del proyecto" en
> `docs/WORKFLOW_ENCHANTVENTURE_TRANSLATIONS_26-2.md`.

## Proyecto

| Variable | Valor |
|----------|-------|
| `curseforge_project_id` | `PENDIENTE` |
| `mod_id` | `enchantventure_translations` |
| `display_name` | `EnchantVenture Translations` |

## Tokens

| API | Token | Uso |
|-----|-------|-----|
| Upload | `ee776b0a-ee95-4850-b554-06be02a8657f` (token de cuenta, mismo que el resto de proyectos) | Subir archivos ZIP |
| Core (GET) | `$2a$10$yGwryAfmRkS9ZJsJUDf5YOKZpOIsmHB8Fji2D8JVCKBSZEKYlwmaO` | Consultar datos del proyecto |

Autenticación Upload: cabecera `X-Api-Token`
Autenticación Core: cabecera `x-api-key`

> El API token de CurseForge es el mismo para todos los proyectos (token de cuenta, no de proyecto).

## Versión actual

| Variable | Valor |
|----------|-------|
| `minecraft_version` | `26.2` |
| `pack_format` | `64` |
| `environment` | `Client` (traducciones, se aplican en el cliente) |

## Rama

```
minecraft/26.2/resourcepack/production
```

## Tag

Formato: `<mc-version>-<version>`
Ejemplo: `26.2-0.0.0-beta.1`

## Parámetros del upload

| Campo | Valor | Notas |
|-------|-------|-------|
| `displayName` | `EnchantVenture Translations (0.0.0-beta.1)` | Nombre visible: `display_name (version)` |
| `changelog` | HTML (no Markdown) | Ver estructura abajo |
| `changelogType` | `html` | Obligatorio para que se vea bien |
| `releaseType` | `beta` | Según el tipo de versión |
| `gameVersions` | `[<gameVersionId de 26.2>]` | CurseForge usa el `gameVersionId` de Minecraft, no el pack format (ver nota abajo) |

## Estructura del changelog (HTML)

```html
<h2>v0.0.0-beta.1 - Initial release</h2>

<h3>Added</h3>
<ul>
<li><strong>EnchantVenture Translations</strong>: first versioned release of the resource pack.</li>
</ul>

<hr>

<p><strong>ZIP</strong>: <code>EnchantVenture_translations-0.0.0-beta.1.zip</code></p>
```

> Nota: `gameVersions` usa el `gameVersionId` de Minecraft (de `GET /v1/minecraft/version`), no el pack format.
> Para `26.2` reutilizar el mismo id ya validado en `EnchantVenture_fixes/docs/curseforge/project_vars.md`
> (`16498` a fecha de este documento) — confirmar contra el endpoint si ha pasado tiempo.

## Verificar con GET

```bash
curl -s "https://api.curseforge.com/v1/mods/<PROJECT_ID>/files/<FILE_ID>" \
  -H "x-api-key: <API_TOKEN>"
```

## Descripción del proyecto

No hay endpoint API para actualizar la descripción. Se edita manualmente desde la web de CurseForge
pegando el HTML de `docs/curseforge/project_description.md`.

## Variables parseables (para scripts)

El script `scripts/curseforge-upload.ps1` lee estas líneas (`key = value`). Rellenar tras crear el proyecto:

```
project_id = PENDIENTE
api_token = ee776b0a-ee95-4850-b554-06be02a8657f
game_versions = PENDIENTE
release_type = beta
```

## Flujo completo

0. **Crear el proyecto en CurseForge** (una vez): logo (`pack.png`), summary, descripción (pegar HTML de
   `project_description.md`), categoría "Resource Packs". Anotar `project_id` y `gameVersionId` aquí.
1. `python build_translation_pack.py`
2. Actualizar `docs/curseforge/versions/<version>.md` con HTML
3. Actualizar `CHANGELOG.md`
4. `git commit -m "chore: bump version to <version>"` + `git push`
5. `git tag -a 26.2-<version> -m "v<version>: descripcion"` + `git push origin <tag>`
6. Subir ZIP a CurseForge con `scripts/curseforge-upload.ps1`
7. Verificar con GET que el changelog se vea bien
8. Liberar manualmente desde la web si es necesario
