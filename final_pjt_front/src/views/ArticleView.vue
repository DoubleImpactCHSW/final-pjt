<template>
    <div>
        <h1>상품 후기 게시판</h1>
        <p>token: {{ token }}</p>
        <hr>
        <b-button v-if="mode !== 'post'" @click="goPost" variant="primary">후기 작성하기</b-button>
        <div v-if="mode === 'all'" class="d-flex flex-column align-items-center">
            <ArticleItem v-for="article in articles" :key="article.id" :title="article.title" :content="article.content" />
        </div>
        <div v-if="mode === 'post'">
            <ArticleForm />
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import ArticleItem from '@/components/community/ArticleItem.vue'
import ArticleForm from '@/components/community/ArticleForm.vue'

export default {
    name: 'ArticleView',

    components: {
        ArticleItem,
        ArticleForm,
    },

    data() {
        return {
            articles: [],
        };
    },

    computed: {
        token() {
            return this.$store.state.token
        },
        mode() {
            return this.$store.state.communityMode
        }
    },

    created() {
        axios.get('http://127.0.0.1:8000/articles/', {
            headers: {
                Authorization: `Token ${this.$store.state.token}`
            }
        })
        .then((res) => {
            this.articles = res.data
        })
    },

    methods: {
        goPost() {
            this.$store.dispatch('changeCommunityMode', 'post')
        }
    },
};
</script>

<style scoped>

</style>