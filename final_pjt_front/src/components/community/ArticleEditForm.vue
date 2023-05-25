<template>
  <div>
    <form @submit.prevent="put">
      <label for="title">제목</label>
      <input type="text" id="title" v-model="title" /><br />

      <label for="content">내용</label>
      <textarea id="content" v-model="content" /><br />

      <b-button type="submit" class="b-button-custom-success">수정</b-button>
      <b-button @click="goBack" class="b-button-custom-danger">취소</b-button>
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

<style scoped>
form {
  max-width: 600px;
  margin: 0 auto;
  padding: 50px;
  border-radius: 5px;
  background-color: #81C784;
}

label {
  color: #000;
  margin-bottom: 5px;
  font-size: 32px;
}

input[type="text"] {
  width: 100%;
  padding: 15px;
  margin-bottom: 10px;
  border: 1px solid #BCAAA4;
  border-radius: 3px;
}

textarea#content {
  width: 100%;
  height: 300px;
  resize: none; /* 크기 조절 비활성화 */
  padding: 15px;
  border: 1px solid #BCAAA4;
}

.b-button-custom-success {
  background-color: #DEB887;
  border-color: #D2B48C;
  margin: 0 30px;
  padding: 5px 30px;
  font-size: 24px;
}

.b-button-custom-success:hover,
.b-button-custom-success:focus {
  background-color: #CD853F;
  border-color: #CD853F;
}

.b-button-custom-danger {
  background-color: #DEB887;
  border-color: #CDB79E;
  margin: 0 30px;
  padding: 5px 30px;
  font-size: 24px;
}

.b-button-custom-danger:hover,
.b-button-custom-danger:focus {
  background-color: #DAA520;
  border-color: #DAA520;
}
</style>
