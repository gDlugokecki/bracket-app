import type { RouteRecordRaw } from 'vue-router'

import { ROUTE_NAMES } from '../routes'

export const matchRoutes: RouteRecordRaw[] = [
  {
    path: '/matches/:id',
    name: ROUTE_NAMES.MATCH_DETAILS,
    component: () => import('@/views/MatchView.vue'),
    meta: {
      requiresAuth: true,
    },
  },
]
