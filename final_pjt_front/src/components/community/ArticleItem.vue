<template>
    <div class="item p-3 m-3" rounded>
        <p>{{ title }}</p>
    </div>
</template>

<script>

export default {
    name: 'ArticleItem',

    props: {
        title: String,
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
.item {
    width: 50%;
    border: solid 3px grey;
    border-radius: 10px;
}
</style>