import type { RouteRecordRaw } from 'vue-router'

import { ROUTES, ROUTE_NAMES } from '../routes'

export const publicRoutes: RouteRecordRaw[] = [
  {
    path: ROUTES.HOME,
    name: ROUTE_NAMES.HOME,
    component: () => import('@/views/LandingView.vue'),
  },
  {
    path: ROUTES.NOT_FOUND,
    name: ROUTE_NAMES.NOT_FOUND,
    component: () => import('@/views/NotFound.vue'),
  },
]
