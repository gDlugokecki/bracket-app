# Router Organization Guide

## Current Structure (Modular Approach)

```
router/
├── index.ts                 # Main router (combines all modules)
├── routes.ts                # Route path constants
├── middleware/              # Global middleware
│   └── loadLayoutMiddleware.ts
└── modules/                 # Route modules by feature
    ├── index.ts             # Barrel export
    ├── public.routes.ts     # Landing, 404
    ├── auth.routes.ts       # Login, signup
    ├── app.routes.ts        # Dashboard, profile, settings
    ├── tournament.routes.ts # Tournament CRUD
    └── match.routes.ts      # Match routes
```

## Benefits of This Approach

✅ **Easy to find routes** - Grouped by feature/domain
✅ **Easy to add routes** - Add to relevant module
✅ **Better code splitting** - Lazy load per feature
✅ **Clear separation** - Each module has one responsibility
✅ **Scalable** - Works for 100+ routes

## Adding a New Route

### 1. Add path constant to `routes.ts`

```typescript
export const ROUTES = {
  // ...
  LEADERBOARD: '/leaderboard',
}

export const ROUTE_NAMES = {
  // ...
  LEADERBOARD: 'leaderboard',
}
```

### 2. Add route to appropriate module

```typescript
// modules/app.routes.ts
export const appRoutes: RouteRecordRaw[] = [
  // ...
  {
    path: ROUTES.LEADERBOARD,
    name: ROUTE_NAMES.LEADERBOARD,
    component: () => import('@/views/LeaderboardView.vue'),
    meta: {
      layout: 'DashboardLayout',
      requiresAuth: true,
    },
  },
]
```

That's it! No need to touch `router/index.ts`.

## Adding a New Feature Module

Create a new file: `router/modules/player.routes.ts`

```typescript
import type { RouteRecordRaw } from 'vue-router'

import { ROUTES, ROUTE_NAMES } from '../routes'

export const playerRoutes: RouteRecordRaw[] = [
  {
    path: ROUTES.PLAYERS,
    name: ROUTE_NAMES.PLAYERS,
    component: () => import('@/views/players/PlayersView.vue'),
    meta: {
      layout: 'DashboardLayout',
      requiresAuth: true,
    },
  },
]
```

Then export from `modules/index.ts`:

```typescript
export { playerRoutes } from './player.routes'
```

And add to main router:

```typescript
import { playerRoutes } from './modules'

routes: [...playerRoutes]
```

## Alternative Approaches

### Approach 1: Flat Structure (Simple, < 15 routes)

```
router/
├── index.ts    # All routes in one file
└── routes.ts   # Path constants
```

**Pros**: Simple, easy to understand
**Cons**: Gets messy with 20+ routes

---

### Approach 2: Nested Routes (For parent-child relationships)

Use when you have logical hierarchy:

```typescript
{
  path: '/tournaments',
  component: TournamentLayout,
  children: [
    {
      path: '',
      name: 'tournaments',
      component: TournamentsListView,
    },
    {
      path: ':id',
      name: 'tournament-details',
      component: TournamentDetailsView,
    },
    {
      path: ':id/edit',
      name: 'tournament-edit',
      component: TournamentEditView,
    },
  ],
}
```

**When to use**: Parent layout wraps all children (e.g., admin section)

---

### Approach 3: Auto-Import Routes (Advanced)

Auto-discover routes from files:

```typescript
// router/index.ts
const routes = Object.values(import.meta.glob('./modules/*.routes.ts', { eager: true })).flatMap(
  (mod: any) => mod.default,
)
```

**Pros**: Zero boilerplate when adding modules
**Cons**: Hard to debug, magic behavior

---

## Route Meta Fields

Use `meta` for route-level configuration:

```typescript
{
  path: '/dashboard',
  meta: {
    layout: 'DashboardLayout',    // Which layout to use
    requiresAuth: true,            // Requires login
    requiresGuest: true,           // Only for guests (login/signup)
    title: 'Dashboard',            // Page title
    breadcrumb: 'Home > Dashboard',// Breadcrumb
    permissions: ['admin'],        // Required permissions
  },
}
```

Access in components:

```vue
<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
console.log(route.meta.requiresAuth) // true
</script>
```

## Middleware (Navigation Guards)

### Global Middleware (runs on every route)

```typescript
// router/index.ts
router.beforeEach(loadLayoutMiddleware)
router.beforeEach(authGuard)
```

### Per-Route Middleware

```typescript
{
  path: '/admin',
  beforeEnter: (to, from) => {
    if (!isAdmin()) {
      return { name: 'home' }
    }
  },
}
```

## Best Practices

1. ✅ **Always use route constants** from `routes.ts`
2. ✅ **Lazy load components** with `() => import()`
3. ✅ **Keep 404 route last** in the routes array
4. ✅ **Use descriptive route names** (kebab-case)
5. ✅ **Group related routes** in same module
6. ✅ **Add meta fields** for common route configuration

## When to Use Each Approach

| Routes  | Approach               | Reason                  |
| ------- | ---------------------- | ----------------------- |
| < 10    | Flat (all in index.ts) | Simple, no overhead     |
| 10-30   | Modular (current)      | Organized, scalable     |
| 30-100+ | Modular + Nested       | Maximum organization    |
| Any     | Auto-import            | Magic, less boilerplate |

## Current App Structure

**Our approach**: Modular (10-30 routes expected)

As the app grows:

- **Add more modules** for new features (players, teams, etc.)
- **Use nested routes** if you have parent-child layouts
- **Keep it simple** - don't over-engineer
