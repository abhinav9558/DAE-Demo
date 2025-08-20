# ADR-database-choice.md

## Title
Use SQLite for local development

## Context
We needed a lightweight database that works offline for testing.

## Decision
We chose SQLite for local development.

## Rationale
- Simple to set up
- Doesn’t require network or credentials
- Faster for small teams

## Alternatives considered:
- PostgreSQL (more powerful, but heavier)
- Firebase (not local, requires internet)

## Consequences
- Easy onboarding for new devs
- Will need to migrate for production

## References
- https://www.sqlite.org