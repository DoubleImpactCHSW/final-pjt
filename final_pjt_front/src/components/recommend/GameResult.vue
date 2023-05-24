<template>
  <div>
    <p>게임 결과</p>
    <div>
      {{ finalGameResult }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'GameResult',
  props: {
    finalGameResult: Array,
  },
};
</script>

<style scoped></style>
