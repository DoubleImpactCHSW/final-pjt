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

import store from '../store'

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
    component: LogInView,
    beforeEnter: (to, from, next) => {
      /* must call `next` */
      if (store.getters.isLogin) {
        alert('이미 로그인되었습니다.')
        next(false)
      } else {
        next()
      }
    }
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


// router.beforeEach((to, from, next) => {
//   if (!store.getters.isLogin) {
//     if (to.name === 'login') {
//       next()
//     } else {
//       alert('로그인을 먼저 진행해야합니다!')
//       router.push({ name: 'login' })
//     }
//   } else {
//     next();
//   }
// })

export default router
