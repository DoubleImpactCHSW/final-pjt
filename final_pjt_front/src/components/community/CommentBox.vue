<template>
  <div class="box p-3">
    <p>{{ createdAt }}</p>
    <p>{{ content }}</p>
  </div>
</template>

<script>
export default {
  name: 'CommentBox',

  props: {
    content: String,
    createdAt: String,
  },

  data() {
    return {};
  },

  methods: {},
};
</script>

<style scoped>
.box {
  width: 50%;
  border: solid 2px lightgreen;
  border-radius: 20px;
}
</style>
