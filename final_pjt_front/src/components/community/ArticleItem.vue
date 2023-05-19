<template>
  <div class="item p-3 m-3" rounded>
    <p>작성자 {{ writer }}</p>
    <p @click="goDetail">{{ title }}</p>
    <b-button v-if="isMine" @click="deleteArticle" variant="danger">삭제</b-button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ArticleItem',

  props: {
    id: Number,
    writer: String,
    title: String,
  },

  data() {
    return {
      articleId: this.id,
    };
  },

  computed: {
    isMine() {
      return this.writer == this.$store.state.username
    }
  },

  methods: {
    deleteArticle() {
      axios
        .delete(`http://127.0.0.1:8000/articles/${this.articleId}`, {
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
        .then((res) => {
          console.log(res);
          this.$store.dispatch('getArticles');
        })
        .catch((err) => [console.log(err)]);
    },
    goDetail() {
      this.$store.dispatch('getArticleDetail', this.articleId);
    },
  },
};
</script>

<style scoped>
.item {
  width: 50%;
  border: solid 3px grey;
  border-radius: 10px;
}
</style>
