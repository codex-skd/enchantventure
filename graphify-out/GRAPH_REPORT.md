# Graph Report - enchantventure-pack  (2026-08-11)

## Corpus Check
- 141 files · ~1,190,337 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 129 nodes · 100 edges · 40 communities (34 shown, 6 thin omitted)
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `f8a1194e`
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
- [0.0.0-beta.9] - 2026-08-03
- [1.0.0-beta.3] - 2026-08-10

## God Nodes (most connected - your core abstractions)
1. `Changelog` - 24 edges
2. `Flujo de trabajo — EnchantVenture Pack (Resource Pack)` - 12 edges
3. `CurseForge — Variables del proyecto` - 12 edges
4. `EnchantVenture Pack` - 8 edges
5. `[1.0.0-beta.1] - 2026-08-10` - 5 edges
6. `[0.0.0-beta.16] - 2026-08-08` - 4 edges
7. `[0.0.0-beta.18] - 2026-08-10` - 3 edges
8. `[0.0.0-beta.17] - 2026-08-09` - 3 edges
9. `[0.0.0-beta.15] - 2026-08-04` - 3 edges
10. `[0.0.0-beta.14] - 2026-08-04` - 3 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (40 total, 6 thin omitted)

### Community 0 - "build_translation_pack.py"
Cohesion: 0.14
Nodes (13): Buenas prácticas, Commits (Conventional Commits), Círculo mágico (Enchanting Table Magic Circle, integrado desde v1.0.0-beta.1), Diferencias con un mod NeoForge o con el datapack de fixes, Específico del resource pack, Estructura del proyecto, Flujo de trabajo — EnchantVenture Pack (Resource Pack), Flujo por mod (tarea recurrente) (+5 more)

### Community 3 - "Flujo de trabajo — EnchantVenture_translations (Resource Pack)"
Cohesion: 0.50
Nodes (4): [0.0.0-beta.16] - 2026-08-08, Añadido, Corregido, Eliminado

### Community 4 - "CurseForge — Variables del proyecto"
Cohesion: 0.17
Nodes (12): CurseForge — Variables del proyecto, Descripción del proyecto, Estructura del changelog (HTML), Flujo completo, Parámetros del upload, Proyecto, Rama, Tag (+4 more)

### Community 5 - "EnchantVenture Translations"
Cohesion: 0.18
Nodes (9): Estado de traducciones — EnchantVenture Pack, Build, Coverage, Credits, EnchantVenture Pack, Features, Installation, License (+1 more)

### Community 6 - "create_project_form.md"
Cohesion: 0.33
Nodes (3): Campos del formulario, CurseForge — Formulario de creación del proyecto, Pendiente

### Community 7 - "Changelog"
Cohesion: 0.06
Nodes (30): [0.0.0-beta.10] - 2026-08-03, [0.0.0-beta.11] - 2026-08-03, [0.0.0-beta.12] - 2026-08-03, [0.0.0-beta.13] - 2026-08-03, [0.0.0-beta.14] - 2026-08-04, [0.0.0-beta.1] - 2026-08-03, [0.0.0-beta.2] - 2026-08-03, [0.0.0-beta.3] - 2026-08-03 (+22 more)

### Community 8 - "[0.0.0-beta.14] - 2026-08-04"
Cohesion: 0.40
Nodes (5): [1.0.0-beta.1] - 2026-08-10, Añadido, Cambiado, Corregido, Nota

### Community 10 - "[0.0.0-beta.11] - 2026-08-03"
Cohesion: 0.67
Nodes (3): [0.0.0-beta.15] - 2026-08-04, Añadido, Cambiado

### Community 11 - "[0.0.0-beta.12] - 2026-08-03"
Cohesion: 0.67
Nodes (3): [0.0.0-beta.17] - 2026-08-09, Corregido, Nota

### Community 12 - "[0.0.0-beta.13] - 2026-08-03"
Cohesion: 0.67
Nodes (3): [0.0.0-beta.18] - 2026-08-10, Corregido, Nota

## Knowledge Gaps
- **65 isolated node(s):** `Documentado`, `Corregido`, `Cambiado`, `Documentado`, `Cambiado` (+60 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **6 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Changelog` connect `Changelog` to `Flujo de trabajo — EnchantVenture_translations (Resource Pack)`, `[1.0.0-beta.3] - 2026-08-10`, `[0.0.0-beta.14] - 2026-08-04`, `[0.0.0-beta.11] - 2026-08-03`, `[0.0.0-beta.12] - 2026-08-03`, `[0.0.0-beta.13] - 2026-08-03`, `[0.0.0-beta.1] - 2026-08-03`, `[0.0.0-beta.2] - 2026-08-03`, `[0.0.0-beta.9] - 2026-08-03`?**
  _High betweenness centrality (0.184) - this node is a cross-community bridge._
- **Why does `[1.0.0-beta.1] - 2026-08-10` connect `[0.0.0-beta.14] - 2026-08-04` to `Changelog`?**
  _High betweenness centrality (0.026) - this node is a cross-community bridge._
- **Why does `[0.0.0-beta.16] - 2026-08-08` connect `Flujo de trabajo — EnchantVenture_translations (Resource Pack)` to `Changelog`?**
  _High betweenness centrality (0.020) - this node is a cross-community bridge._
- **What connects `Documentado`, `Corregido`, `Cambiado` to the rest of the system?**
  _65 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `build_translation_pack.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._
- **Should `Changelog` be split into smaller, more focused modules?**
  _Cohesion score 0.06451612903225806 - nodes in this community are weakly interconnected._