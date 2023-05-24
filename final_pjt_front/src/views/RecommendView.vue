<template>
  <div>
    <BasicRecommendation />
    <BalanceGame />
  </div>
</template>

<script>
import BalanceGame from '@/components/recommend/BalanceGame';
import BasicRecommendation from '@/components/recommend/BasicRecommendation';

export default {
  name: 'RecommendView',

  components: {
    BalanceGame,
    BasicRecommendation,
  },

  data() {
    return {};
  },

  mounted() {},

  methods: {},
};
</script>

<style scoped>
.campfire {
  position: relative;
  width: 250px;
  height: 250px;
  background-color: black;
  border-radius: 50%;
  overflow: hidden;
}

.vs-text {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 100px;
  font-weight: bold;
  letter-spacing: 2px;
  color: gold;
  text-transform: uppercase;
  animation: burn-in-flames 2s infinite;
}

@keyframes burn-in-flames {
  0% {
    opacity: 0.8;
    text-shadow: 0 0 30px grey, 0 0 60px grey, 0 0 90px grey;
  }
  50% {
    opacity: 1;
    text-shadow: 0 0 30px #ff0000, 0 0 60px #ff3333, 0 0 90px #ff3333;
  }
  100% {
    opacity: 0.8;
    text-shadow: 0 0 30px black, 0 0 60px black, 0 0 90px black;
  }
}
</style>
