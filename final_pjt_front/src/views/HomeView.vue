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
    if (!this.$store.state.token) {
      alert('로그인을 먼저 진행해야합니다!')
      this.$router.push({ name:'login' })
    }
  }
}
</script>
