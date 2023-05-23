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
  height: 85vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.content {
  text-align: center;
  color: #fff; /* Set font color for content */
}
</style>
