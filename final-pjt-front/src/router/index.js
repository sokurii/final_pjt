import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import SignupView from '../views/SignupView.vue'
import FinanceView from '../views/FinanceView.vue'
import MapView from '../views/MapView.vue'
import ExchangeView from '../views/ExchangeView.vue'
import CommunityView from '../views/CommunityView.vue'
import ProfileView from '../views/ProfileView.vue'
import DepositProductDetailView from '../views/DepositProductDetailView.vue'
import SavingProductDetailView from '../views/SavingProductDetailView.vue'
import CreateArticleView from '../views/CreateArticleView.vue'
import DetailArticleView from '../views/DetailArticleView.vue'

Vue.use(VueRouter)

const routes = [
  { // 메인 페이지
    path: '/',
    name: 'home',
    component: HomeView
  },
  { // 로그인 페이지
    path: '/login',
    name: 'login',
    component: LoginView,
  },
  { // 회원가입 페이지
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  { // 금융상품조회 페이지
    path: '/finance',
    name: 'finance',
    component: FinanceView
  },
  { // 정기예금 상품 상세 조회 페이지
    path: '/finance/deposit/:fin_prdt_cd',
    name: 'depositDetail',
    component: DepositProductDetailView
  },
  { // 금융상품 상세 조회 페이지
    path: '/finance/saving/:fin_prdt_cd',
    name: 'savingDetail',
    component: SavingProductDetailView
  },
  { // 지도 페이지
    path: '/map',
    name: 'map',
    component: MapView
  },
  { // 환율 페이지
    path: '/exchange',
    name: 'exchange',
    component: ExchangeView
  },
  { // 게시판 페이지
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  { // 게시글 작성 페이지
    path: '/community/create',
    name: 'CreateArticle',
    component: CreateArticleView
  },
  { // 게시글 상세 페이지
    path: '/community/:id',
    name: 'DetailArticle',
    component: DetailArticleView
  },
  { // 프로필 페이지
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
