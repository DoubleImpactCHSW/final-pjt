import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'
import createPersistedState from 'vuex-persistedstate';

const API_URL = 'http://127.0.0.1:8000'


Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    token: null,
    signUpError: null,
    // communityMode는 community에 띄울 컴포넌트 결정
    // 'all' : 게시글 전체 조회
    // 'post' : ArticleForm
    // 'detail' : 게시글 상세 조회
    communityMode: 'all',
    articles: [],
  },
  getters: {
    isLogin(state) {
      return !!state.token
    }
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'home' })
    },
    REMOVE_TOKEN(state) {
      state.token = null
      router.push({ name: 'login' })
    },
    CHANGE_COMMUNITY_MODE(state, payload) {
      state.communityMode = payload
    },
    GET_ARTICLES(state, data) {
      state.articles = [...data]
    },
  },
  actions: {
    signUp(context, payload) {
      const username = payload.username
      const email = payload.email
      const password1 = payload.password1
      const password2 = payload.password2
      const nickname = payload.nickname

      axios({
        method: 'post',
        url: `${API_URL}/dj_rest_auth/signup/`,
        data: {
          username, email, password1, password2, nickname
        }
      }).then((res) => {
        console.log(res)
        context.state.signUpError = null
        context.commit('SAVE_TOKEN', res.data.key)
        alert('가입을 축하합니다 ><')
      }).catch((err) => {
        context.state.signUpError = err.response.data
        console.log(err)
      })
    },
    login(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/dj_rest_auth/login/`,
        data: {
          username, password
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          console.log(err)
          if (err.response.status === 400) {
            alert('아이디 혹은 비밀번호가 잘못되었습니다.')
          }
        })
    },
    logout(context) {
      axios.post(`${API_URL}/dj_rest_auth/logout/`)
      .then((res) => {
        console.log(res)
        context.commit('REMOVE_TOKEN')
      })
      .catch((err) => {
        console.log(err)
      })
    },
    changeCommunityMode(context, payload) {
      context.commit('CHANGE_COMMUNITY_MODE', payload)
    },
    getArticles(context) {
      axios.get('http://127.0.0.1:8000/articles/', {
            headers: {
                Authorization: `Token ${context.state.token}`
            }
        })
        .then((res) => {
            context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  modules: {
  }
})
