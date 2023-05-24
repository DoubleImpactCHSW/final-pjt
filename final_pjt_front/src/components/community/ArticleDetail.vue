<template>
  <div>
    <DetailContent :writer="writer" :title="title" :content="content" :created-at="created_at" />
    <p>댓글 <b>{{ comment_count }}</b></p>
    <CommentBox
      v-for="comment in commentsList"
      :key="comment.id"
      :comment-id="comment.id"
      :article-id="comment.article"
      :writer="comment.username"
      :content="comment.content"
      :created-at="comment.created_at"
    />
    <div class="comment-input">
      <div class="input-group">
        <input type="text" class="form-control" v-model="comment_input" placeholder="댓글을 입력하세요" style="width: 300px;">
        <div class="input-group-append">
          <button class="btn btn-info" type="button" @click="addComment">등록</button>
        </div>
      </div>
    </div>

    <hr />
    <b-button @click="goList">목록</b-button>
  </div>
</template>

<script>
import DetailContent from '@/components/community/DetailContent';
import CommentBox from '@/components/community/CommentBox';
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000';

export default {
  name: 'ArticleDetail',

  components: {
    DetailContent,
    CommentBox,
  },

  data() {
    return {
      id: this.$store.state.articleDetail.id,
      writer: this.$store.state.articleDetail.username,
      title: this.$store.state.articleDetail.title,
      content: this.$store.state.articleDetail.content,
      created_at: this.$store.state.articleDetail.created_at,
      // comment_set: this.$store.state.articleDetail.comment_set,
      comment_input: '',
    };
  },

  computed: {
    commentsList() {
      return this.$store.state.commentsList;
    },
    comment_count() {
      return this.$store.state.articleDetail.comment_count
    },
  },

  created() {
    this.$store.dispatch('getComments', this.id);
  },

  methods: {
    goList() {
      this.$store.dispatch('changeCommunityMode', 'all');
    },
    addComment() {
      const formData = new FormData();
      formData.append('content', this.comment_input);

      axios
        .post(`${API_URL}/articles/${this.id}/comments/`, formData, {
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
            'Content-Type': 'multipart/form-data',
          },
        })
        .then((res) => {
          console.log(res);
          this.$store.dispatch('getComments', this.id);
          this.comment_input = ''
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
.comment-input {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
  max-width: 700px;
  margin: 0 auto; /* 가운데 정렬을 위해 margin 설정 */

}

.comment-input-field {
  flex: 1;
  margin-right: 10px;
}

.comment-input-field input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  transition: box-shadow 0.3s ease;
  box-sizing: border-box;
}

.comment-input-field input:hover {
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
}

.comment-input-button {
  flex-shrink: 0;
}

.comment-input-button b-button {
  transition: opacity 0.3s ease;
  animation: fade-in 0.5s;
}

@keyframes fade-in {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}


</style>
