# CurseForge — Formulario de creación del proyecto

> ✅ Proyecto ya creado: `curseforge_project_id` = `1638251`. Este documento queda como referencia de los
> valores usados / a mantener coherentes si se edita la ficha del proyecto en el futuro.

## Campos del formulario

| Campo | Valor usado |
|---|---|
| **Project Name** | `EnchantVenture Translations` |
| **Slug / URL** | `enchantventure-translations` |
| **Summary** (línea corta, ~1 frase) | `Spanish (es_ES) translations for mods in the EnchantVenture modpack that don't ship their own.` |
| **Project Type / Class** | Resource Packs |
| **Category** | Data Packs (dentro de la clase Resource Packs, el resto de categorías son de resolución: 16x, 32x, 64x... — ninguna aplica a un pack de solo traducciones, así que se usó esta) |
| **Client / Server** | Client |
| **Project License** | All Rights Reserved |
| **Description** | HTML de [`project_description.md`](project_description.md) |
| **Logo / Icon** | `resourcepack/pack.png` (libro encantado con letras "A"/"Ñ" transformándose, cinta roja/amarilla) |

## Pendiente

- Confirmar el `gameVersionId` de Minecraft `26.2` en la primera subida real (se reutiliza `16498`, el mismo
  que `EnchantVenture_fixes`; si falla, consultar `GET /v1/minecraft/version` con el Core token y corregir
  `game_versions` en [`project_vars.md`](project_vars.md)).
- Subir la primera versión (`0.0.0-beta.1`) con `powershell -File scripts/curseforge-upload.ps1`
  (requiere haber corrido antes `python build_pack.py`).
