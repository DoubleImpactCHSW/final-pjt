<template>
  <div>
    <h1>은행 지도</h1>
    <BankMap />
  </div>
</template>

<script>
import BankMap from '@/components/bankmap/BankMap'
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

<style scoped></style>
