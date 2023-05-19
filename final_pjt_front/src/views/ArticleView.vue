<template>
  <div>
    <h1>상품 후기 게시판</h1>
    <p>token: {{ token }}</p>
    <hr />
    <b-button v-if="mode !== 'post'" @click="goPost" variant="primary"
      >후기 작성하기</b-button
    >
    <div v-if="mode === 'all'" class="d-flex flex-column align-items-center">
      <ArticleItem
        v-for="article in articles"
        :key="article.id"
        :id="article.id"
        :title="article.title"
        :content="article.content"
      />
    </div>
    <div v-if="mode === 'post'">
      <ArticleForm />
    </div>
    <div v-if="mode === 'detail'">
      <ArticleDetail />
    </div>
  </div>
</template>

<script>
import ArticleItem from '@/components/community/ArticleItem.vue';
import ArticleForm from '@/components/community/ArticleForm.vue';
import ArticleDetail from '@/components/community/ArticleDetail.vue';

export default {
  name: 'ArticleView',

  components: {
    ArticleItem,
    ArticleForm,
    ArticleDetail,
  },

  data() {
    return {};
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
  },

  created() {
    this.$store.dispatch('getArticles');
  },

  methods: {
    goPost() {
      this.$store.dispatch('changeCommunityMode', 'post');
    },
  },
};
</script>

<style scoped></style>
