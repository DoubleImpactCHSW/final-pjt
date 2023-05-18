<template>
  <div class="home">
    <h1>HomeView</h1>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {
  },
  created() {
    if (!this.$store.getters.isLogin) {
      alert('로그인 해주세요!')
      this.$router.push({ name: 'login' })
    }
  }
}
</script>
