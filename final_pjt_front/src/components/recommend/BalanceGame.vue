<template>
  <div>
    <div v-if="isGameOn">
      <div v-if="!showRoundText">
        <div class="question-box">
          <span class="question-text">{{ question[currentRound] }}</span>
        </div>
        <span class="vs-text">VS</span>
        <div class="d-flex justify-content-around">
          <div @click="selectLeft">
            <ChoiceCard color="#FF3333" :content="leftOption[currentRound]" />
          </div>
          <div @click="selectRight">
            <ChoiceCard color="#0047AB" :content="rightOption[currentRound]" />
          </div>
        </div>
      </div>
      <div v-if="showRoundText" class="round-text-container">
        <div class="round-text">{{ roundText }}</div>
      </div>
    </div>
    <div v-else>
      <GameResult :final-game-result="finalGameResult" />
    </div>
  </div>
</template>

<script>
import ChoiceCard from '@/components/recommend/ChoiceCard';
import GameResult from '@/components/recommend/GameResult';

export default {
  name: 'BalanceGame',

  components: {
    ChoiceCard,
    GameResult,
  },

  data() {
    return {
      question: ['나는 목돈이', '상품 가입 방법은?', '2년 이상 가입을'],
      leftOption: ['있다.', '직접 방문', '할거야!'],
      rightOption: ['없다.', '귀찮아~\n온라인으로!', '2년은 너무 길어~'],
      round: 0,
      showRoundText: true,
      choice: [1, 1, 1],
      gameOn: true,
      gameResult: null,
    };
  },

  computed: {
    currentRound() {
      return this.round;
    },
    roundText() {
      return 'Round ' + (this.round + 1);
    },
    isGameOn() {
      return this.gameOn;
    },
    finalGameResult() {
      return this.gameResult;
    },
  },

  mounted() {
    setTimeout(() => {
      this.showRoundText = false;
    }, 3000);
  },

  methods: {
    async selectLeft() {
      this.round = this.round + 1;
      if (this.round === 3) {
        this.gameOn = false;
        const result = await this.$store.dispatch('getGameResult', this.choice);
        this.gameResult = result;
      }
      this.showRoundText = true;
      setTimeout(() => {
        this.showRoundText = false;
      }, 3000);
    },
    async selectRight() {
      this.choice[this.round] = 0;
      this.round = this.round + 1;
      if (this.round === 3) {
        this.gameOn = false;
        const result = await this.$store.dispatch('getGameResult', this.choice);
        this.gameResult = result;
      }
      this.showRoundText = true;
      setTimeout(() => {
        this.showRoundText = false;
      }, 3000);
    },
  },
};
</script>

<style scoped>
.question-box {
  text-align: center;
  padding: 10px;
  background-color: #f8f8f8;
  border-radius: 5px;
  max-width: 500px;
  margin: 50px auto;
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.3);
}

.question-text {
  font-size: 32px;
  font-weight: bold;
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

.round-text-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 75vh;
}

.round-text {
  font-size: 64px;
  font-weight: bold;
  animation: fade-in-out 3s;
}

@keyframes fade-in-out {
  0% {
    opacity: 0;
  }
  20% {
    opacity: 1;
  }
  80% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
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
    text-shadow: 0 0 30px #0047ab, 0 0 60px #0047ab, 0 0 90px #0047ab;
  }
}
</style>
