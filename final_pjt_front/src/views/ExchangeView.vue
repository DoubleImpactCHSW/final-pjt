<template>
  <div class="exchange-view">
    <div class="content">
      <RateCalculator />
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
  height: 93vh;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(to bottom, #fff, #FFFACD);
}

.content {
  text-align: center;
}
</style>
