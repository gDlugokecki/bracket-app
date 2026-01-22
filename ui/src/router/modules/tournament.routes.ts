import type { RouteRecordRaw } from 'vue-router'

import { ROUTES, ROUTE_NAMES } from '../routes'

export const tournamentRoutes: RouteRecordRaw[] = [
  {
    path: ROUTES.TOURNAMENTS,
    name: ROUTE_NAMES.TOURNAMENTS,
    component: () => import('@/views/TournamentsView.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/tournaments/:id',
    name: ROUTE_NAMES.TOURNAMENT_DETAILS,
    component: () => import('@/views/TournamentDetailsView.vue'),
    meta: {
      requiresAuth: true,
    },
  },
]
