<template>
  <div>
    <div class="title">당신을 위한 추천 상품 TOP 5</div>
    <div>
      <RecommendedProduct v-for="prd in results" :key="prd.id" :info="prd"/>
    </div>
  </div>
</template>

<script>
import RecommendedProduct from '@/components/recommend/RecommendedProduct'

export default {
  name: 'GameResult',
  components: {
    RecommendedProduct,
  },
  computed: {
    results() {
      return this.$store.state.gameResult
    }
  },
  mounted() {
  }
};
</script>

<style scoped>

.title {
  background-color: forestgreen;
  color: #fff;
  max-width: 500px;
  margin: 0 auto;
  border-radius: 20px;
  padding: 20px 0;
  font-size: 36px;
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.3);
}


</style>
