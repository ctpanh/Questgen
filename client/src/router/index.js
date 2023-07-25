import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView
    },
    {
      path: '/app',
      name: 'AppCreate',
      component: () => import('../views/AppCreate.vue')
    },
    {
      path: '/app/view',
      name: 'AppView',
      component: () => import('../views/AppView.vue')
    }
  ]
})

export default router
