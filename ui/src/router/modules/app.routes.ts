import type { RouteRecordRaw } from 'vue-router'

import { ROUTES, ROUTE_NAMES } from '../routes'

export const appRoutes: RouteRecordRaw[] = [
  {
    path: ROUTES.DASHBOARD,
    name: ROUTE_NAMES.DASHBOARD,
    component: () => import('@/views/DashboardView.vue'),
    meta: {
      layout: 'DashboardLayout',
      requiresAuth: true,
    },
  },
]
