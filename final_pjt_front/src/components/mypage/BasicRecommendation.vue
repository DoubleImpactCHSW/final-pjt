<template>
  <div class="cont">
    <div class="top-title">
      <div class="title-line"></div>
      <div class="title-text">당신만을 위해 엄선한 TOP 10 상품</div>
      <div class="title-line"></div>
    </div>
    <div v-if="recList" class="recommendation-list">
      <div class="product-item" v-for="product in recList" :key="product.id">
        <div class="bank-name">{{ product.bankName }}</div>
        <div class="product-name">{{ product.productName }}</div>
      </div>
    </div>
    <div v-else class="loading-message">
      당신의 데이터를 기반으로 최적의 상품들을 추출하는 중입니다...
    </div>
  </div>
</template>

<script>
export default {
  name: 'BasicRecommendation',
  props: {
    recList: Array,
  },
};
</script>

<style scoped>
.cont {
  margin-top: 100px;
}


.top-title {
  text-align: center;
  margin-bottom: 50px;
}

.title-line {
  width: 100px;
  height: 2px;
  background-color: #FFD700;
  display: inline-block;
  vertical-align: middle;
}

.title-text {
  font-size: 32px;
  font-weight: bold;
  color: #FFD700;
  display: inline-block;
  margin: 0 20px;
}

.recommendation-list {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-gap: 15px;
}

.product-item {
  background-color: #f2f2f2;
  padding: 10px;
  border-radius: 5px;
}

.bank-name {
  font-weight: bold;
}

.product-name {
  margin-top: 5px;
}

.loading-message {
  text-align: center;
  font-style: italic;
  color: #888;
  margin-top: 80px;
  font-size: 24px;
}
</style>
