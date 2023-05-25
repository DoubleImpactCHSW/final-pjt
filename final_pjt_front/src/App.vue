<template>
  <div id="app">
    <nav class="navbar">
      <div class="d-flex justify-content-between align-items-center" style="width: 100%;">
        <div class="d-flex align-items-center">
          <div class="navbar-logo">
            <router-link to="/">Logo</router-link>
          </div>
          <ul class="navbar-menu d-flex align-items-center" v-if="isLogin">
            <li>
              <router-link to="/product" class="nav-link">예적금 상품 조회</router-link>
            </li>
            <li>
              <router-link to="/exchange" class="nav-link">환율 조회</router-link>
            </li>
            <li>
              <router-link to="/bankmap" class="nav-link">은행 찾기</router-link>
            </li>
            <li>
              <router-link to="/article" class="nav-link">커뮤니티</router-link>
            </li>
            <li>
              <router-link to="/recommend" class="nav-link">예적금 밸런스 게임</router-link>
            </li>
          </ul>
        </div>
        <div>
          <ul class="navbar-menu d-flex align-items-center" v-if="!isLogin">
            <li>
              <router-link to="/signup" class="nav-link">Signup</router-link>
            </li>
            <li>
              <router-link to="/login" class="nav-link">Login</router-link>
            </li>
          </ul>
          <div class="navbar-logout" v-if="isLogin">
            <ul class="navbar-menu d-flex align-items-center">
              <li>
                <!-- <router-link to="/mypage" class="nav-link">My Page</router-link> -->
                <router-link to="/mypage" class="nav-link"><b-avatar variant="warning"></b-avatar></router-link>
              </li>
              <li>
                <!-- <b-button @click="logout" variant="danger">Logout</b-button> -->
                <b-button @click="logout" variant="outline-warning" class="mb-2">
                  <b-icon icon="power" aria-hidden="true"></b-icon> Logout
               </b-button>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: 'App',
  computed: {
    isLogin() {
      return this.$store.getters.isLogin;
    },
  },
  methods: {
    logout() {
      this.$store.dispatch('logout');
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.navbar {
  background-color: #f8f8f8;
  padding: 10px;
  border-bottom: 1px solid #ddd;
}


.navbar-logo {
  color: #333;
  font-size: 20px;
  font-weight: bold;
}

.navbar-menu {
  list-style: none;
  margin: 0;
  padding: 0;
}

.navbar-menu li {
  margin-left: 10px;
}

.navbar-menu li a {
  color: #333;
  text-decoration: none;
  transition: color 0.3s;
}

.navbar-menu li a:hover {
  color: #42b983;
}

.navbar-logout {
  margin-left: 10px;
}
</style>