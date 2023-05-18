<template>
    <div>
        <form @submit.prevent="post">
            <label for="title">제목</label>
            <input type="text" id="title" v-model="title"><br>

            <label for="content">내용</label>
            <input type="text" id="content" v-model="content"><br>
            
            <b-button type="submit" variant="success">등록</b-button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name: 'ArticleForm',

    data() {
        return {
            title: '',
            content: '',
        };
    },

    mounted() {
        
    },

    methods: {
        post() {
            const formData = new FormData();
            formData.append('title', this.title);
            formData.append('content', this.content);


            axios.post('http://127.0.0.1:8000/articles/', formData, {
                headers: {
                    Authorization: `Token ${this.$store.state.token}`,
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then(res => {
                console.log(res)
                this.$store.dispatch('getArticles') // 리렌더링용
                this.$store.dispatch('changeCommunityMode', 'all')
            })
            .catch(err => {
                console.log(err)
            })

        }
    },
};
</script>

<style scoped>

</style>