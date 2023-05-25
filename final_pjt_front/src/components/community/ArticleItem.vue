<template>
  <div class="item p-2 m-3 rounded">
    <div class="d-flex justify-content-between align-items-center">
      <p class="mb-0">{{ writer }}</p>
      <b-button v-if="isMine" @click="deleteArticle" variant="danger" size="sm"
        >삭제</b-button
      >
    </div>
    <h4 class="mt-2 title" @click="goDetail">{{ title }}</h4>
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
      return this.writer == this.$store.state.username;
    },
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
        .catch((err) => console.log(err));
    },
    goDetail() {
      this.$store.dispatch('getArticleDetail', this.articleId);
    },
  },
};
</script>

<style scoped>
.item {
  width: 700px;
  border-radius: 10px;
  transition: background-color 0.3s;
  background-color: #fff8e1;
}

.item:hover {
  background-color: #deb887;
}

.item p {
  color: #666;
}

.item h4.title {
  color: #333;
  font-size: 32px;
  font-weight: bold;
  transition: color 0.3s;
  cursor: pointer;
}

.item h4.title:hover {
  color: #fff8e1;
}
</style>
