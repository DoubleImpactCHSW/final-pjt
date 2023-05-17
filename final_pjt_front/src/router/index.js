import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProductView from '../views/ProductView.vue'
import ExchangeView from '../views/ExchangeView.vue'
import MypageView from '../views/MypageView.vue'
import BankMapView from '../views/BankMapView.vue'
import SignUpView from '../views/SignUpView.vue'
import LogInView from '../views/LogInView.vue'
import ArticleView from '../views/ArticleView.vue'
import RecommendView from '../views/RecommendView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },{
    path: '/login',
    name: 'login',
    component: LogInView
  },
  {
    path: '/product',
    name: 'product',
    component: ProductView
  },
  {
    path: '/exchange',
    name: 'exchange',
    component: ExchangeView
  },
  {
    path: '/mypage',
    name: 'mypage',
    component: MypageView
  },
  {
    path: '/bankmap',
    name: 'bankmap',
    component: BankMapView
  },
  {
    path: '/article',
    name: 'article',
    component: ArticleView
  },
  {
    path: '/recommend',
    name: 'recommend',
    component: RecommendView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
