<template>
  <div>
    <h1>추천 게임 view</h1>

    <hr>
    <p>당신의 선택은?</p>
    <span class="vs-text">VS</span>
    <div class="d-flex justify-content-around">
      <ChoiceCard />
      <ChoiceCard />
    </div>
  </div>
</template>

<script>
import ChoiceCard from '@/components/recommend/ChoiceCard'
export default {
  name: 'RecommendView',

  components: {
    ChoiceCard,
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
    text-shadow: 0 0 30px #FF0000, 0 0 60px #FF3333, 0 0 90px #FF3333;
  }
  100% {
    opacity: 0.8;
    text-shadow: 0 0 30px black, 0 0 60px black, 0 0 90px black;
  }
}
</style>
