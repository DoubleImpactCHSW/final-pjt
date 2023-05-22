<template>
  <div class="d-flex flex-column align-items-center">
    <h1>마이페이지 View</h1>
    <UserInfo />

  </div>
</template>

<script>
import UserInfo from '@/components/mypage/UserInfo'

export default {
  name: 'MypageView',

  components: {
    UserInfo,
  },

  data() {
    return {};
  },

  mounted() {
    
  },

  methods: {},
};
</script>

<style scoped>

</style>
