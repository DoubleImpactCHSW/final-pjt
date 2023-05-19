<template>
    <div>
        <h3>제목: {{ title }}</h3>
        <p>작성일: {{ createdAt }}</p>
        <p>내용: {{ content }}</p>
    </div>
</template>

<script>
export default {
    name: 'DetailContent',

    props: {
        title: String,
        content: String,
        createdAt: String,
    },

    data() {
        return {
            
        };
    },

    methods: {
        
    },
};
</script>

<style scoped>

</style>