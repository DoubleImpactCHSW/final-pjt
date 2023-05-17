<template>
    <div>
        <h1>커뮤니티(게시판)</h1>
        <p>token: {{ token }}</p>
    </div>
</template>

<script>
export default {
    name: 'ArticleView',

    data() {
        return {
        };
    },

    computed: {
        token() {
            return this.$store.state.token
        }
    },

    methods: {
        
    },
};
</script>

<style scoped>

</style>