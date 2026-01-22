import type { RouteRecordRaw } from 'vue-router'

import { ROUTES, ROUTE_NAMES } from '../routes'

export const authRoutes: RouteRecordRaw[] = [
  {
    path: ROUTES.LOGIN,
    name: ROUTE_NAMES.LOGIN,
    component: () => import('@/views/auth/LoginView.vue'),
  },
  {
    path: ROUTES.SIGNUP,
    name: ROUTE_NAMES.SIGNUP,
    component: () => import('@/views/auth/SignupView.vue'),
  },
  {
    path: ROUTES.FORGOT_PASSWORD,
    name: ROUTE_NAMES.FORGOT_PASSWORD,
    component: () => import('@/views/auth/ForgotPasswordView.vue'),
  },
  {
    path: ROUTES.RESET_PASSWORD,
    name: ROUTE_NAMES.RESET_PASSWORD,
    component: () => import('@/views/auth/ResetPasswordView.vue'),
  },
]
