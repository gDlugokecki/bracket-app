import { createRouter, createWebHistory } from 'vue-router'
import MatchView from '../views/MatchView.vue'
import HomeView from '@/views/HomeView.vue'
import TournamentsView from '@/views/TournamentsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/tournament',
      name: 'tournament',
      component: TournamentsView,
    },
    {
      path: '/match/:id',
      name: 'match',
      component: MatchView,
    },
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
  ],
})

export default router
