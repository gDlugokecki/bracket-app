import { useAuth } from '@/composables/useAuth'
import { ROUTES } from '@/router/routes'
import type { RouteLocationNormalized } from 'vue-router'

export async function authMiddleware(to: RouteLocationNormalized) {
  const { checkAuth, isAuthenticated } = useAuth()

  const requiresAuth = to.meta.requiresAuth === true

  if (requiresAuth) {
    const authenticated = await checkAuth()

    if (!authenticated) {
      return { path: ROUTES.LOGIN, query: { redirect: to.fullPath } }
    }
  } else {
    if (isAuthenticated.value && !requiresAuth) {
      return { path: ROUTES.DASHBOARD }
    }
  }

  return true
}
