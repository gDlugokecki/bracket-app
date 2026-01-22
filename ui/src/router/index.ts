import { loadLayoutMiddleware } from '@/router/middleware/loadLayoutMiddleware'
import { createRouter, createWebHistory } from 'vue-router'

import { authMiddleware } from './middleware/authMiddleware'
import { publicRoutes, authRoutes, appRoutes, tournamentRoutes, matchRoutes } from './modules'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [...authRoutes, ...appRoutes, ...tournamentRoutes, ...matchRoutes, ...publicRoutes],
})

router.beforeEach(loadLayoutMiddleware)
router.beforeEach(authMiddleware)

export default router
