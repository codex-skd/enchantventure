# Graph Report - EnchantVenture_translations  (2026-08-04)

## Corpus Check
- 111 files · ~172,480 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 95 nodes · 74 edges · 37 communities (23 shown, 14 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d4a252b2`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- build_translation_pack.py
- Screenshot of the EnchantVenture resource pack
- Flujo de trabajo — EnchantVenture_translations (Resource Pack)
- CurseForge — Variables del proyecto
- EnchantVenture Translations
- create_project_form.md
- Changelog
- [0.0.0-beta.14] - 2026-08-04
- [0.0.0-beta.10] - 2026-08-03
- [0.0.0-beta.11] - 2026-08-03
- [0.0.0-beta.12] - 2026-08-03
- [0.0.0-beta.13] - 2026-08-03
- [0.0.0-beta.1] - 2026-08-03
- [0.0.0-beta.2] - 2026-08-03
- [0.0.0-beta.4] - 2026-08-03
- [0.0.0-beta.5] - 2026-08-03
- [0.0.0-beta.6] - 2026-08-03
- [0.0.0-beta.7] - 2026-08-03
- [0.0.0-beta.8] - 2026-08-03
- [0.0.0-beta.9] - 2026-08-03
- [0.0.0-beta.3] - 2026-08-03

## God Nodes (most connected - your core abstractions)
1. `Changelog` - 16 edges
2. `Flujo de trabajo — EnchantVenture_translations (Resource Pack)` - 12 edges
3. `CurseForge — Variables del proyecto` - 12 edges
4. `EnchantVenture Translations` - 6 edges
5. `[0.0.0-beta.15] - 2026-08-04` - 3 edges
6. `[0.0.0-beta.14] - 2026-08-04` - 3 edges
7. `CurseForge — Formulario de creación del proyecto` - 3 edges
8. `validate_json_files()` - 2 edges
9. `main()` - 2 edges
10. `[0.0.0-beta.13] - 2026-08-03` - 2 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (37 total, 14 thin omitted)

### Community 3 - "Flujo de trabajo — EnchantVenture_translations (Resource Pack)"
Cohesion: 0.15
Nodes (12): Buenas prácticas, Commits (Conventional Commits), Diferencias con un mod NeoForge o con el datapack de fixes, Específico del resource pack, Estructura del proyecto, Flujo de trabajo — EnchantVenture_translations (Resource Pack), Flujo por mod (tarea recurrente), Flujo por tarea (+4 more)

### Community 4 - "CurseForge — Variables del proyecto"
Cohesion: 0.17
Nodes (12): CurseForge — Variables del proyecto, Descripción del proyecto, Estructura del changelog (HTML), Flujo completo, Parámetros del upload, Proyecto, Rama, Tag (+4 more)

### Community 5 - "EnchantVenture Translations"
Cohesion: 0.22
Nodes (7): Estado de traducciones — EnchantVenture Translations, Build, Coverage, EnchantVenture Translations, Installation, License, Requirements

### Community 6 - "create_project_form.md"
Cohesion: 0.33
Nodes (3): Campos del formulario, CurseForge — Formulario de creación del proyecto, Pendiente

### Community 7 - "Changelog"
Cohesion: 0.50
Nodes (3): [0.0.0-beta.6] - 2026-08-03, Añadido, Changelog

### Community 8 - "[0.0.0-beta.14] - 2026-08-04"
Cohesion: 0.67
Nodes (3): [0.0.0-beta.15] - 2026-08-04, Añadido, Cambiado

### Community 17 - "[0.0.0-beta.6] - 2026-08-03"
Cohesion: 0.67
Nodes (3): [0.0.0-beta.14] - 2026-08-04, Añadido, Cambiado

## Knowledge Gaps
- **48 isolated node(s):** `Añadido`, `Cambiado`, `Cambiado`, `Añadido`, `Añadido` (+43 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **14 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Changelog` connect `Changelog` to `[0.0.0-beta.3] - 2026-08-03`, `[0.0.0-beta.14] - 2026-08-04`, `[0.0.0-beta.10] - 2026-08-03`, `[0.0.0-beta.11] - 2026-08-03`, `[0.0.0-beta.12] - 2026-08-03`, `[0.0.0-beta.13] - 2026-08-03`, `[0.0.0-beta.1] - 2026-08-03`, `[0.0.0-beta.2] - 2026-08-03`, `[0.0.0-beta.4] - 2026-08-03`, `[0.0.0-beta.5] - 2026-08-03`, `[0.0.0-beta.6] - 2026-08-03`, `[0.0.0-beta.7] - 2026-08-03`, `[0.0.0-beta.8] - 2026-08-03`, `[0.0.0-beta.9] - 2026-08-03`?**
  _High betweenness centrality (0.116) - this node is a cross-community bridge._
- **Why does `CurseForge — Variables del proyecto` connect `CurseForge — Variables del proyecto` to `create_project_form.md`?**
  _High betweenness centrality (0.028) - this node is a cross-community bridge._
- **What connects `Añadido`, `Cambiado`, `Cambiado` to the rest of the system?**
  _48 weakly-connected nodes found - possible documentation gaps or missing edges._