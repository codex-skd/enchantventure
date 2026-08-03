# CurseForge — Formulario de creación del proyecto

> Checklist para crear manualmente el proyecto "EnchantVenture Translations" en CurseForge
> (https://www.curseforge.com/project/create). No existe endpoint de API para crear proyectos,
> solo para subir archivos a uno ya existente — este paso es manual.

## Campos del formulario

| Campo | Valor a usar |
|---|---|
| **Project Name** | `EnchantVenture Translations` |
| **Slug / URL** | `enchantventure-translations` (o el que sugiera CurseForge si está ocupado) |
| **Summary** (línea corta, ~1 frase) | `Spanish (es_ES) translations for mods in the EnchantVenture modpack that don't ship their own.` |
| **Project Type** | Resource Packs |
| **Category** | Miscellaneous (no es Data Packs ni Font Packs — este pack solo trae `lang/es_es.json`; si el desplegable ofrece algo más específico tipo "Language"/"Localization", usar esa en su lugar) |
| **Client / Server** | Client |
| **Project License** | All Rights Reserved |
| **Description** | Pegar el HTML completo de [`project_description.md`](project_description.md) en el editor (modo HTML/source, no el WYSIWYG en markdown) |
| **Logo / Icon** | ⚠️ Pendiente — falta un `pack.png` (icono cuadrado, se ve también en el selector de resource packs in-game). Aún no se ha proporcionado ninguno; avisa cuando lo tengas y lo integro en `resourcepack/pack.png` y lo subo aquí. |

## Tras crear el proyecto

1. Anotar el `curseforge_project_id` (URL del proyecto, ej. `curseforge.com/minecraft/texture-packs/enchantventure-translations`
   → el ID numérico está en la página de administración o en la URL de la API) en
   [`project_vars.md`](project_vars.md) (`curseforge_project_id`).
2. Confirmar el `gameVersionId` de Minecraft `26.2` (reutilizar el ya validado en `EnchantVenture_fixes`
   si sigue vigente, o consultar `GET /v1/minecraft/version` con el Core token) y anotarlo en
   `game_versions` de la sección "Variables parseables" de `project_vars.md`.
3. Rellenar la sección "Variables parseables" completa para que `scripts/curseforge-upload.ps1` funcione.
4. Subir la primera versión (`0.0.0-beta.1`) con `powershell -File scripts/curseforge-upload.ps1`
   (requiere haber corrido antes `python build_translation_pack.py`).
