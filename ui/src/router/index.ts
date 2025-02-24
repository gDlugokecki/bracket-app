import { loadLayoutMiddleware } from '@/router/middleware/loadLayoutMiddleware'
import TournamentsDetailsView from '@/views/TournamentDetailsView.vue'
import TournamentsView from '@/views/TournamentsView.vue'
import { createRouter, createWebHistory } from 'vue-router'

import MatchView from '../views/MatchView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/tournament',
      name: 'tournament',
      component: TournamentsView,
    },
    {
      path: '/tournament/:id',
      name: 'tournamentDetails',
      component: TournamentsDetailsView,
    },
    {
      path: '/match/:id',
      name: 'match',
      component: MatchView,
    },
    {
      path: '/',
      name: 'tournament',
      component: TournamentsView,
    },
  ],
})

router.beforeEach(loadLayoutMiddleware)

export default router
