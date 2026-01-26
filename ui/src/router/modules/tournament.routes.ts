import type { RouteRecordRaw } from 'vue-router'

import { ROUTES, ROUTE_NAMES } from '../routes'

export const tournamentRoutes: RouteRecordRaw[] = [
  {
    path: ROUTES.TOURNAMENT_CREATE,
    name: ROUTE_NAMES.TOURNAMENT_CREATE,
    component: () => import('@/views/tournaments/form/TournamentForm.vue'),
    meta: {
      requiresAuth: true,
      layout: 'DashboardLayout',
    },
  },
]
