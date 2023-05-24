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
  height: 94vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background-image: url('@/assets/background/ship.gif');
  background-size: cover;
  background-position: center;
}

.content {
  text-align: center;
  color: #fff; /* Set font color for content */
}
</style>
