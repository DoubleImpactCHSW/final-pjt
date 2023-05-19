<template>
  <div>
    <form @submit.prevent="put">
      <label for="title">제목</label>
      <input type="text" id="title" v-model="title" /><br />

      <label for="content">내용</label>
      <input type="text" id="content" v-model="content" /><br />

      <b-button type="submit" variant="success">수정</b-button>
      <b-button @click="goBack" variant="danger">취소</b-button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/articles'

export default {
  name: 'ArticleEditForm',

  data() {
    return {
      title: this.$store.state.articleDetail.title,
      content: this.$store.state.articleDetail.content,
    };
  },

  mounted() {},

  methods: {
    put() {
      const formData = new FormData();
      formData.append('title', this.title);
      formData.append('content', this.content);

      axios
        .put(`${API_URL}/${this.$store.state.articleDetail.id}/`, formData, {
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
            'Content-Type': 'multipart/form-data',
          },
        })
        .then((res) => {
          console.log(res);
          this.$store.dispatch('getArticleDetail', this.$store.state.articleDetail.id);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    goBack() {
        this.$store.dispatch('changeCommunityMode', 'detail')
    }
  },
};
</script>

<style scoped></style>
