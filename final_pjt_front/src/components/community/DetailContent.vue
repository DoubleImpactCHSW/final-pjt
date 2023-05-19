<template>
  <div>
    <h3>제목: {{ title }}</h3>
    <p>작성자: {{ writer }}</p>
    <p>작성일: {{ createdAt }}</p>
    <p>내용: {{ content }}</p>
    <b-button @click="goEdit" v-if="inMine" variant="success">수정</b-button>
  </div>
</template>

<script>
export default {
  name: 'DetailContent',

  props: {
    writer: String,
    title: String,
    content: String,
    createdAt: String,
  },

  data() {
    return {

    };
  },

  computed: {
    inMine() {
      return this.writer === this.$store.state.username
    }
  },

  methods: {
    goEdit() {
      this.$store.dispatch('changeCommunityMode', 'edit')
    }
  },
};
</script>

<style scoped></style>
