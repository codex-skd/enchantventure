# CurseForge — Formulario de creación del proyecto

> ✅ Proyecto ya creado: `curseforge_project_id` = `1638251`. Este documento queda como referencia de los
> valores usados / a mantener coherentes si se edita la ficha del proyecto en el futuro.
>
> ⚠️ **Renombrado (v1.0.0-beta.1)**: el proyecto CurseForge se debe editar manualmente en la web para
> reflejar el rebranding — no hay endpoint API para cambiar nombre/summary/descripción. Valores nuevos abajo.

## Campos del formulario

| Campo | Valor usado (actualizado) |
|---|---|
| **Project Name** | `EnchantVenture` |
| **Slug / URL** | `enchantventure` |
| **Summary** (línea corta, ~1 frase) | `Spanish (es_ES) translations + Enchanting Table Magic Circle for the EnchantVenture modpack.` |
| **Project Type / Class** | Resource Packs |
| **Category** | Data Packs (dentro de la clase Resource Packs, el resto de categorías son de resolución: 16x, 32x, 64x... — ninguna aplica a un pack de traducciones+círculo, así que se mantiene esta) |
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
