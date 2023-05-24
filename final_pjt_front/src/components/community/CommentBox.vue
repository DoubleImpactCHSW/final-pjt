<template>
  <div class="comment-container">
    <div class="comment-info">
      <span class="comment-writer">{{ writer }}</span>
      <span class="comment-date">{{ newCreatedAt }}</span>
    </div>
    <div class="comment-content">{{ content }}</div>
    <div class="comment-actions">
      <b-button v-if="isMine" @click="deleteComment" variant="danger" class="delete-button">삭제</b-button>
    </div>
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
    },
    newCreatedAt() {
      const date = new Date(this.createdAt);
      const year = date.getFullYear();
      const month = String(date.getMonth() + 1).padStart(2, '0');
      const day = String(date.getDate()).padStart(2, '0');
  
      return `${year}.${month}.${day}`;
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
.comment-container {
  display: flex;
  align-items: center;
  max-width: 800px; /* 원하는 최대 너비로 설정 */
  margin: 0 auto;
  padding: 10px 20px;
  background-color: #f8f8f8;
  border: 1px solid #ddd;
  border-radius: 5px;
  margin-bottom: 10px;
}

.comment-info {
  display: flex;
  align-items: center;
  margin-right: 10px;
}

.comment-writer {
  font-weight: bold;
  margin-right: 10px;
}

.comment-date {
  color: #666;
}

.comment-content {
  margin-right: 30px;
  margin-left: 30px;
  width: 450px;
  text-align: start;
}

.comment-actions {
  display: flex;
  margin-left: auto;
}

.delete-button {
}
</style>