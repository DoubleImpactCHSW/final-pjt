<template>
  <div class="bankmap-view">
    <BankMap />
  </div>
</template>

<script>
import BankMap from '@/components/bankmap/BankMap';
export default {
  name: 'BankMapView',

  components: {
    BankMap,
  },

  data() {
    return {};
  },

  mounted() {},

  methods: {},
};
</script>

<style scoped>
.bankmap-view {
  padding-top: 50px;
  height: 93vh;
  background: linear-gradient(to bottom, #fff, #FFFACD);
}
</style>
