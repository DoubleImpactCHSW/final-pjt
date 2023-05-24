<template>
  <div>
    <h2>상품 후기</h2>
    <p>token: {{ token }}</p>
    <hr />
    <b-button
      class="mb-3"
      v-if="mode !== 'post'"
      @click="goPost"
      variant="primary"
      >후기 작성하러 가기</b-button
    >
    <div v-if="mode === 'all'" class="d-flex flex-column align-items-center">
      <div v-if="noArticles">
        <h3>아직 후기가 없어요.</h3>
      </div>
      <div v-else>
        <div class="article-list">
          <ArticleItem
            v-for="article in paginatedArticles"
            :key="article.id"
            :id="article.id"
            :writer="article.username"
            :title="article.title"
            :content="article.content"
          />
        </div>
        <div class="pagination-controls">
          <button @click="previousPage" :disabled="currentPage === 1">
            이전
          </button>
          <span>{{ currentPage }} / {{ totalPages }}</span>
          <button @click="nextPage" :disabled="currentPage === totalPages">
            다음
          </button>
        </div>
      </div>
    </div>
    <div v-if="mode === 'post'">
      <ArticleForm />
    </div>
    <div v-if="mode === 'detail'">
      <ArticleDetail />
    </div>
    <div v-if="mode === 'edit'">
      <ArticleEditForm />
    </div>
  </div>
</template>

<script>
import ArticleItem from '@/components/community/ArticleItem.vue';
import ArticleForm from '@/components/community/ArticleForm.vue';
import ArticleDetail from '@/components/community/ArticleDetail.vue';
import ArticleEditForm from '@/components/community/ArticleEditForm.vue';

export default {
  name: 'ArticleView',

  components: {
    ArticleItem,
    ArticleForm,
    ArticleDetail,
    ArticleEditForm,
  },

  data() {
    return {
      itemsPerPage: 4, // Number of items to display per page
      currentPage: 1, // Current page number
    };
  },

  computed: {
    token() {
      return this.$store.state.token;
    },
    mode() {
      return this.$store.state.communityMode;
    },
    articles() {
      return this.$store.state.articles;
    },
    totalPages() {
      return Math.ceil(this.articles.length / this.itemsPerPage);
    },
    paginatedArticles() {
      const startIndex = (this.currentPage - 1) * this.itemsPerPage;
      const endIndex = startIndex + this.itemsPerPage;
      return this.articles.slice(startIndex, endIndex);
    },
    noArticles() {
      return !this.paginatedArticles?.length;
    },
  },

  created() {
    this.$store.dispatch('getArticles');
  },

  methods: {
    goPost() {
      this.$store.dispatch('changeCommunityMode', 'post');
    },
    previousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
  },
};
</script>

<style scoped>
.pagination-controls {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 10px;
}

.pagination-controls button {
  margin: 0 5px;
}

.article-list {
  padding: 30px;
  border-radius: 40px;
  background-color: aliceblue;
  height: 580px;
  margin-bottom: 20px;
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.3);
}
</style>
