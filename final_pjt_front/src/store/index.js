import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import router from '../router';
import createPersistedState from 'vuex-persistedstate';

const API_URL = 'http://127.0.0.1:8000';

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    token: null,
    username: null,
    signUpError: null,
    // communityMode는 community에 띄울 컴포넌트 결정
    // 'all' : 게시글 전체 조회
    // 'post' : ArticleForm
    // 'detail' : 게시글 상세 조회
    // 'edit' : 게시글 수정
    communityMode: 'all',
    articles: [],
    articleDetail: {},
    commentsList: [],
  },

  getters: {
    isLogin(state) {
      return !!state.token;
    },
  },

  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token;
      router.push({ name: 'home' });
    },
    REMOVE_TOKEN(state) {
      state.token = null;
      router.push({ name: 'login' });
    },
    SAVE_USERNAME(state, username) {
      state.username = username;
    },
    CHANGE_COMMUNITY_MODE(state, payload) {
      state.communityMode = payload;
    },
    GET_ARTICLES(state, data) {
      state.articles = data;
    },
    GET_ARTICLE_DETAIL(state, detail) {
      state.articleDetail = detail;
      state.communityMode = 'detail';
    },
    GET_COMMENTS(state, comments) {
      state.commentsList = comments;
    },
  },

  actions: {
    signUp(context, payload) {
      const username = payload.username;
      const email = payload.email;
      const password1 = payload.password1;
      const password2 = payload.password2;
      const nickname = payload.nickname;

      axios({
        method: 'post',
        url: `${API_URL}/dj_rest_auth/signup/`,
        data: {
          username,
          email,
          password1,
          password2,
          nickname,
        },
      })
        .then((res) => {
          console.log(res);
          context.state.signUpError = null;
          context.commit('SAVE_TOKEN', res.data.key);
          alert('가입을 축하합니다 ><');
        })
        .catch((err) => {
          context.state.signUpError = err.response.data;
          console.log(err);
        });
    },
    login(context, payload) {
      const username = payload.username;
      const password = payload.password;

      axios({
        method: 'post',
        url: `${API_URL}/dj_rest_auth/login/`,
        data: {
          username,
          password,
        },
      })
        .then((res) => {
          console.log(res);
          context.commit('SAVE_TOKEN', res.data.key);
          context.commit('SAVE_USERNAME', username);
        })
        .catch((err) => {
          console.log(err);
          if (err.response.status === 400) {
            alert('아이디 혹은 비밀번호가 잘못되었습니다.');
          }
        });
    },
    logout(context) {
      axios
        .post(`${API_URL}/dj_rest_auth/logout/`)
        .then((res) => {
          console.log(res);
          context.commit('REMOVE_TOKEN');
          context.commit('SAVE_USERNAME', null);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    changeCommunityMode(context, payload) {
      context.commit('CHANGE_COMMUNITY_MODE', payload);
    },
    getArticles(context) {
      axios
        .get(`${API_URL}/articles/`, {
          headers: {
            Authorization: `Token ${context.state.token}`,
          },
        })
        .then((res) => {
          context.commit('GET_ARTICLES', res.data);
        })
        .catch((err) => {
          if (err.response && err.response.status === 404) {
            // 404 에러인 경우 아무 일도 하지 않고 종료
            return;
          }
          console.log(err);
        });
    },
    getArticleDetail(context, articleId) {
      axios
        .get(`${API_URL}/articles/${articleId}/`, {
          headers: {
            Authorization: `Token ${context.state.token}`,
          },
        })
        .then((res) => {
          context.commit('GET_ARTICLE_DETAIL', res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    getComments(context, articleId) {
      axios
        .get(`${API_URL}/articles/${articleId}/comments/`, {
          headers: {
            Authorization: `Token ${context.state.token}`,
          },
        })
        .then((res) => {
          context.commit('GET_COMMENTS', res.data);
        })
        .catch((err) => {
          console.log('getCommentsErr', err)
        })
    },
  },

  modules: {},
});
