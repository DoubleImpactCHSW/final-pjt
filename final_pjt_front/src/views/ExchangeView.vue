<template>
  <div class="exchange-view">
    <div class="content">
      <hr />
      <RateCalculator />
      <hr />
    </div>
  </div>
</template>

<script>
import RateCalculator from '@/components/exchange/RateCalculator';
export default {
  name: 'ExchangeView',

  components: {
    RateCalculator,
  },
};
</script>

<style scoped>
.exchange-view {
  height: 90vh;
  display: flex;
  justify-content: center;
  align-items: center;
  /* background-color: #795548; */
  /* background-image: url('@/assets/background/orbis.jpg');
  background-size: cover;
  background-position: center; */
}

.content {
  text-align: center;
}
</style>
