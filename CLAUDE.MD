# Bracket App - Project Guide

## Project Overview

Bracket App is a tournament management and bracket visualization application for tennis/sports tournaments. It handles tournament creation, player management, match scheduling, team formation, and real-time bracket visualization.

**Status**: Active development - migrated from Django to FastAPI backend

## Tech Stack

### Backend
- **Framework**: FastAPI (Python 3.13)
- **Database**: PostgreSQL with SQLModel ORM
- **Auth**: JWT-based authentication (PyJWT, Argon2 password hashing)
- **Server**: Uvicorn (async)
- **Migrations**: Alembic
- **Dependency Management**: Poetry

### Frontend
- **Framework**: Vue 3 with Composition API + TypeScript
- **Build Tool**: Vite 6.0
- **Styling**: Tailwind CSS v4 + Tailwind Animations
- **UI Components**: shadcn-vue (Radix Vue primitives)
- **Forms**: VeeValidate with Zod schema validation
- **State Management**: TanStack Vue Query (server state)
- **Routing**: Vue Router 4.5
- **API Client**: Auto-generated with Orval from OpenAPI spec
- **Package Manager**: pnpm

### DevOps
- **Containerization**: Docker + Docker Compose
- **Services**: FastAPI (8080), Vue dev server (5173), PostgreSQL (5432), PgAdmin (5050)

## Architecture

### Project Structure

```
bracket-app/
├── api/                          # FastAPI Backend
│   ├── app/
│   │   ├── auth/                # Authentication (users, JWT)
│   │   │   ├── models.py       # User model
│   │   │   ├── router.py       # Auth endpoints
│   │   │   └── schemas.py      # Pydantic schemas
│   │   ├── player/             # Player management
│   │   ├── tournament/         # Tournament CRUD + logic
│   │   ├── match/              # Match management
│   │   ├── team/               # Team formation
│   │   ├── config.py           # Settings (Pydantic)
│   │   └── database.py         # Async SQLAlchemy setup
│   ├── alembic/                # Database migrations
│   ├── main.py                 # FastAPI app entry
│   └── pyproject.toml          # Poetry dependencies
│
├── ui/                          # Vue 3 Frontend
│   ├── src/
│   │   ├── api/
│   │   │   ├── generated/      # Orval-generated Vue Query hooks
│   │   │   └── custom-instance.ts  # Axios configuration
│   │   ├── components/         # Reusable components
│   │   ├── views/              # Page/route components
│   │   ├── layouts/            # Layout wrappers
│   │   ├── router/             # Vue Router config
│   │   ├── types/              # TypeScript types
│   │   ├── main.ts             # Vue app entry
│   │   └── App.vue             # Root component
│   ├── orval.config.ts         # API generation config
│   ├── vite.config.ts          # Vite build config
│   └── package.json            # Dependencies
│
├── compose.yml                  # Docker services
└── makefile                     # Dev commands
```

## Vue 3 Conventions & Best Practices

### File Naming Convention
- **Vue files**: PascalCase (e.g., `TournamentForm.vue`, `MatchCard.vue`)
- **TypeScript files**: camelCase for composables (e.g., `useTournament.ts`), PascalCase for types (e.g., `Tournament.ts`)
- **Rationale**: PascalCase aligns with auto-import tooling, component naming in templates, and IDE support

### Composition API (Preferred)
Always use the Composition API with `<script setup>` syntax:

```vue
<script setup lang="ts">
import { ref, computed } from 'vue'

// Reactive state
const count = ref(0)

// Computed properties
const doubled = computed(() => count.value * 2)

// Methods
const increment = () => {
  count.value++
}
</script>
```

### Folder Structure & Naming

#### Components (`src/components/`)
- **Naming**: PascalCase for files and component names
- **Examples**: `MatchCard.vue`, `TournamentForm.vue`, `BracketNode.vue`
- **Purpose**: Reusable components used across multiple views
- **Organization**:
  ```
  components/
  ├── ui/                    # shadcn-vue components (auto-added via CLI)
  │   ├── button.vue         # Note: shadcn uses lowercase
  │   ├── dialog.vue
  │   └── input.vue
  ├── form/                  # Generic form helpers (cross-feature)
  │   ├── FormField.vue      # Label + input + error wrapper
  │   └── FormDatePicker.vue # Reusable date picker
  ├── tournaments/           # Tournament-specific components
  │   ├── TournamentForm.vue
  │   ├── TournamentCard.vue
  │   └── TournamentTypeSelector.vue
  ├── matches/               # Match-specific components
  │   └── MatchCard.vue
  └── common/                # Shared UI patterns (non-form)
      ├── PageHeader.vue
      └── LoadingSpinner.vue
  ```

**Component placement decision tree:**
- **Base UI primitive?** → `ui/` (shadcn-vue CLI)
- **Generic form helper used across features?** → `form/`
- **Feature-specific (tournaments, matches, etc.)?** → `{feature}/`
- **Common UI pattern (not form)?** → `common/`

#### Views (`src/views/`)
- **Naming**: PascalCase with `View` suffix
- **Examples**: `TournamentsView.vue`, `TournamentDetailsView.vue`, `MatchView.vue`
- **Purpose**: Page-level components mapped to routes
- **Rule**: Views orchestrate components, handle routing params, and fetch data
- **Organization**: Feature-based folders for multi-view features
  ```
  views/
  ├── tournaments/
  │   ├── TournamentsView.vue       # List view
  │   ├── TournamentDetailsView.vue # Detail view
  │   └── TournamentCreateView.vue  # Create view (optional)
  ├── matches/
  │   └── MatchesView.vue
  ├── players/
  │   └── PlayersView.vue
  └── HomeView.vue                  # Top-level views stay flat
  ```

#### Composables (`src/composables/` - create when needed)
- **Naming**: camelCase with `use` prefix
- **Examples**: `useTournament.ts`, `useMatchStatus.ts`, `useAuth.ts`
- **Purpose**: Reusable composition functions for shared logic
- **Pattern**:
  ```ts
  // composables/useTournament.ts
  export function useTournament(tournamentId: Ref<number>) {
    const tournament = ref<Tournament | null>(null)
    const loading = ref(false)

    const fetchTournament = async () => {
      loading.value = true
      // fetch logic
      loading.value = false
    }

    return { tournament, loading, fetchTournament }
  }
  ```

#### Types (`src/types/`)
- **Naming**: PascalCase for interfaces/types
- **Examples**: `Tournament.ts`, `Match.ts`, `ApiResponse.ts`
- **Note**: Orval generates API types in `src/api/generated/`

### Component Guidelines

#### Props Definition
```vue
<script setup lang="ts">
interface Props {
  tournamentId: number
  showDetails?: boolean  // Optional props with ?
}

const props = defineProps<Props>()

// Or with defaults
const props = withDefaults(defineProps<Props>(), {
  showDetails: true
})
</script>
```

#### Emits Definition
```vue
<script setup lang="ts">
interface Emits {
  (e: 'update:modelValue', value: string): void
  (e: 'submit', data: FormData): void
}

const emit = defineEmits<Emits>()

const handleSubmit = () => {
  emit('submit', formData)
}
</script>
```

#### Template Refs
```vue
<script setup lang="ts">
import { ref } from 'vue'

const inputRef = ref<HTMLInputElement>()

const focusInput = () => {
  inputRef.value?.focus()
}
</script>

<template>
  <input ref="inputRef" />
</template>
```

### Import Order (Auto-sorted by Prettier)
1. Vue core imports
2. External libraries
3. `@/components/` imports
4. `@/types/` imports
5. Relative imports (`./`, `../`)

Example:
```ts
import { ref, computed } from 'vue'

import { useQuery } from '@tanstack/vue-query'

import MatchCard from '@/components/matches/MatchCard.vue'

import type { Tournament } from '@/types/Tournament'

import { formatDate } from './utils'
```

### API Integration with Vue Query

Use Orval-generated hooks from `src/api/generated/`:

```vue
<script setup lang="ts">
import { getTournamentsQueryOptions } from '@/api/generated/tournaments'

import { useQuery } from '@tanstack/vue-query'

// Fetch tournaments with automatic caching, refetching, and error handling
const { data: tournaments, isLoading, error } = useQuery(getTournamentsQueryOptions())
</script>

<template>
  <div v-if="isLoading">Loading...</div>
  <div v-else-if="error">Error: {{ error.message }}</div>
  <div v-else>
    <div v-for="tournament in tournaments" :key="tournament.id">
      {{ tournament.name }}
    </div>
  </div>
</template>
```

### Reactivity Rules
- Use `.value` to access/modify refs in `<script>`
- NO `.value` needed in templates
- `reactive()` for objects, `ref()` for primitives
- Destructuring loses reactivity - use `toRefs()` or access properties directly

```ts
// Good
const count = ref(0)
const increment = () => count.value++

// Good - object with reactive
const state = reactive({ count: 0, name: 'Tournament' })
const increment = () => state.count++

// Bad - loses reactivity
const { count } = reactive({ count: 0 })

// Good - preserves reactivity
const { count } = toRefs(reactive({ count: 0 }))
```

## Code Style

### Enforced by Prettier & ESLint
- **No semicolons** (`semi: false`)
- **Single quotes** for strings
- **2 spaces** indentation
- **100 character** line length
- **LF** line endings
- **Trailing commas** where valid
- Unused variables prefixed with `_` are allowed

### TypeScript
- Use strict typing - avoid `any`
- Leverage Orval-generated types from OpenAPI spec
- Use `interface` for object shapes, `type` for unions/intersections

### Tailwind CSS
- Use Tailwind utility classes
- shadcn-vue components are unstyled by default, styled with Tailwind
- Organize classes with Prettier's Tailwind plugin (auto-sorted)

## Development Workflow

### Setup
```bash
# Build and start all services
make build
make run

# Or manually
docker compose build
docker compose up
```

### API Development Workflow
1. Modify FastAPI endpoints in `api/app/*/router.py`
2. Update models in `api/app/*/models.py`
3. Create migration: `make api-migrations`
4. Apply migration: `make api-migrate`
5. **Regenerate UI API client**: `cd ui && pnpm generate`
6. Use new types/hooks in Vue components

### UI Development
```bash
cd ui
pnpm dev           # Start dev server
pnpm lint          # Run ESLint with auto-fix
pnpm build         # Production build
pnpm test:unit     # Run Vitest tests
pnpm generate      # Generate API client from OpenAPI
```

### Database Migrations
```bash
# Backend must be running (docker compose up)
make api-migrations   # Auto-generate migration from model changes
make api-migrate      # Apply pending migrations

# Or inside api container
docker compose exec api alembic revision --autogenerate -m "description"
docker compose exec api alembic upgrade head
```

### API Client Regeneration
**CRITICAL**: After any backend API changes, regenerate the frontend client:
```bash
cd ui
pnpm generate
```

This fetches OpenAPI spec from `http://localhost:8080/openapi.json` and generates:
- TypeScript types in `src/api/generated/model/`
- Vue Query hooks in `src/api/generated/`

## Testing Strategy

### Frontend (Vitest)
- Unit tests for components and composables
- Test files: `*.spec.ts` or `*.test.ts`
- Run: `pnpm test:unit`

### Backend
- pytest tests (to be implemented)
- Focus on router endpoints and business logic

## Git Workflow

### Branching
- `main` - production-ready code
- Feature branches: `feature/tournament-brackets`, `fix/match-score-update`

### Commit Messages
Use conventional commits:
- `feat: add tournament bracket visualization`
- `fix: correct match score update logic`
- `refactor: simplify team formation logic`
- `docs: update API documentation`
- `test: add unit tests for MatchCard component`

## Database Schema (Key Models)

### Relationships
- **User** ↔ **Player** (1:1)
- **Tournament** ↔ **Player** (M:M via `tournament_players`)
- **Tournament** ↔ **Match** (1:M)
- **Team** ↔ **Player** (M:M via `team_players`)
- **Match** → **Team** (team1, team2, winner_team)

### Match Status Enum
- `SCHEDULED` - Match created but not started
- `IN_PROGRESS` - Match currently being played
- `COMPLETED` - Match finished
- `CANCELED` - Match canceled

## Environment Variables

### `.env` (root - database)
```
DB_NAME=bracket_app
DB_USER=bracket_user
DB_PASSWORD=bracket_password
DB_HOST=db
DB_PORT=5432
```

### `api/.env` (backend)
```
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql+asyncpg://bracket_user:bracket_password@db:5432/bracket_app
```

## Common Tasks

### Add a new API endpoint
1. Create route in `api/app/*/router.py`
2. Define request/response schemas
3. Implement business logic
4. Test endpoint manually or with tests
5. Run `pnpm generate` in `ui/` directory
6. Use generated hook in Vue component

### Create a new Vue component
1. Create `ComponentName.vue` in appropriate `src/components/` folder
2. Use `<script setup lang="ts">` with Composition API
3. Define props with TypeScript interfaces
4. Import and use in views or other components
5. Follow import order convention

### Add a new database field
1. Update model in `api/app/*/models.py`
2. Create migration: `make api-migrations`
3. Review generated migration in `api/alembic/versions/`
4. Apply: `make api-migrate`
5. Update schemas if needed
6. Regenerate UI client: `cd ui && pnpm generate`

## Learning Resources

- [Vue 3 Composition API](https://vuejs.org/guide/extras/composition-api-faq.html)
- [TanStack Vue Query](https://tanstack.com/query/latest/docs/framework/vue/overview)
- [VeeValidate](https://vee-validate.logaretm.com/v4/) + [Zod](https://zod.dev/)
- [shadcn-vue Components](https://www.shadcn-vue.com/)
- [Radix Vue Primitives](https://www.radix-vue.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

## Code Review Principles (For Claude)

### Communication Style
- Concise over verbose
- Critical over agreeable
- Honest over polite
- Practical over theoretical
- Question decisions

### Code Quality Standards
- No `any` types - Use proper TypeScript
- No duplicated code - Extract if used 3+ times
- No magic numbers - Use constants
- No premature abstraction - Wait until you feel the pain
- No unnecessary comments - Explain why, not what

### Comments
Only add when crucial:
- Why decisions were made (non-obvious)
- Warnings about breaking changes
- TODOs for temporary workarounds
- External constraints (API requirements)

Never explain what code does - use better variable names.

### Decision Framework
1. Direct answer (2-3 sentences)
2. Why (1 sentence)
3. Code example (only if needed)
4. Alternatives (only if clearly relevant)

### Enforce
- Semantic HTML
- Accessibility (keyboard nav, ARIA when needed)
- Performance (lazy loading, code splitting)
- Consistency (follow existing patterns)

## Tips for Claude Code

- Always regenerate API client after backend changes
- Use TypeScript strictly - leverage generated types
- Prefer Vue Query hooks over manual axios calls
- Use VeeValidate + Zod for form validation (type-safe schemas)
- Follow existing component patterns in the codebase
- Use shadcn-vue components (add with CLI: `pnpm dlx shadcn-vue@latest add <component>`)
- Components are added to `src/components/ui/` and can be customized
- Test in browser after UI changes (http://localhost:5173)
- Check API docs at http://localhost:8080/docs
