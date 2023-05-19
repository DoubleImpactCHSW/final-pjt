<template>
  <div class="box p-3">
    <p>{{ writer }}</p>
    <p>{{ createdAt }}</p>
    <p>{{ content }}</p>
    <b-button v-if="isMine" @click="deleteComment" variant="danger">삭제</b-button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'CommentBox',

  props: {
    commentId: Number,
    articleId: Number,
    writer: String,
    content: String,
    createdAt: String,
  },

  data() {
    return {};
  },

  computed: {
    isMine() {
      return this.writer == this.$store.state.username
    }
  },

  methods: {
    deleteComment() {
      axios
        .delete(`http://127.0.0.1:8000/articles/comments/${this.commentId}/`, {
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
        .then((res) => {
          console.log(res);
          this.$store.dispatch('getComments', this.articleId);
        })
        .catch((err) => [console.log('deleteComment', err)]);
    }
  }
};


</script>

<style scoped>
.box {
  width: 50%;
  border: solid 2px lightgreen;
  border-radius: 20px;
}
</style>
