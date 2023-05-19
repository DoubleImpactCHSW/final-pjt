<template>
    <div>
        <hr>
        <DetailContent :title="title" :content="content" :created-at="created_at" />
        <hr>
        <p>댓글 수: {{ comment_count }}</p>
        <CommentBox v-for="comment in commentsList" :key="comment.id" :content="comment.content" :created-at="comment.created_at"/>
        <div>
            <input type="text" v-model="comment_input">
            <b-button @click="addComment" class="ml-3" variant="info">등록</b-button>
        </div>
        <hr>
        <b-button @click="goList">목록</b-button>
    </div>
</template>

<script>
import DetailContent from '@/components/community/DetailContent'
import CommentBox from '@/components/community/CommentBox'
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'ArticleDetail',

    components: {
        DetailContent,
        CommentBox,
    },

    data() {
        return {
            id: this.$store.state.articleDetail.id,
            title: this.$store.state.articleDetail.title,
            content: this.$store.state.articleDetail.content,
            created_at: this.$store.state.articleDetail.created_at,
            comment_count: this.$store.state.articleDetail.comment_count,
            // comment_set: this.$store.state.articleDetail.comment_set,
            comment_input: '',
        };
    },

    computed: {
        commentsList() {
            return this.$store.state.commentsList
        }
    },

    created() {
        this.$store.dispatch('getComments')
    },

    methods: {
        goList() {
            this.$store.dispatch('changeCommunityMode', 'all')
        },
        addComment() {
            const formData = new FormData();
            formData.append('content', this.comment_input);

            axios.post(`${API_URL}/articles/${this.id}/comments/`, formData, {
                headers: {
                    Authorization: `Token ${this.$store.state.token}`,
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then((res) => {
                console.log(res)
                this.$store.dispatch('getComments')
            })
            .catch((err) => {
                console.log(err)
            })
        },
    },
};
</script>

<style scoped>

</style>