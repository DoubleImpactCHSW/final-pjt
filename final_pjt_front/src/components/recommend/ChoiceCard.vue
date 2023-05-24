<template>
  <div class="outer" :style="`background-color: ${color};`">
    <div class="content">
      <div class="centered-text">
        {{ content }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
    name: 'ChoiceCard',

    props: {
        content: String,
        color: String,
    },

    data() {
        return {
            
        };
    },

    mounted() {
        
    },

    methods: {
        
    },
};
</script>

<style scoped>
.outer {
  width: 300px;
  height: 500px;
  border-radius: 20px;
  box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.4);
  transition: transform 0.3s, box-shadow 0.3s;
  margin: 0 50px;
  cursor: pointer;
  padding: 20px;
}

.outer:hover {
  transform: scale(1.05);
  box-shadow: 0px 12px 40px rgba(0, 0, 0, 0.6);
}

.content {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.centered-text {
  font-size: 36px;
  font-weight: bold;
  text-align: center;
  color: white;
}

@keyframes pulse {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
  100% {
    transform: scale(1);
  }
}

.outer:hover {
  animation: pulse 0.6s infinite;
}
</style>