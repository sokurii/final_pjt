import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import FinanceView from '../views/FinanceView.vue'
import MapView from '../views/MapView.vue'
import CommunityView from '../views/CommunityView.vue'
import WriteView from '../views/WriteView.vue'
import ProfileView from '../views/ProfileView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/finance',
    name: 'finance',
    component: FinanceView
  },
  {
    path: '/map',
    name: 'map',
    component: MapView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/write',
    name: 'write',
    component: WriteView
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
