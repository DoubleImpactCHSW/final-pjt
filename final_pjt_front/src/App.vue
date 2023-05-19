<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/signup">signup</router-link> |
      <router-link to="/login">login</router-link> |
      <b-button v-if="isLogin" @click="logout" variant="danger"
        >logout</b-button
      >
      <hr />
      <div v-if="isLogin">
        <router-link to="/product">product</router-link> |
        <router-link to="/exchange">exchange</router-link> |
        <router-link to="/mypage">mypage</router-link> |
        <router-link to="/bankmap">bankmap</router-link> |
        <router-link to="/article">community</router-link> |
        <router-link to="/recommend">recommend</router-link> |
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

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
