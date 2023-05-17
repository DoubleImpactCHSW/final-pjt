<template>
    <div>
        <h1>회원가입 View</h1>
        <form @submit.prevent="signUp">
        <label for="username">id : </label>
        <input type="text" id="username" v-model="username"><br>

        <label for="nickname">nickname : </label>
        <input type="text" id="nickname" v-model="nickname"><br>

        <label for="password1"> password : </label>
        <input type="password" id="password1" v-model="password1"><br>

        <label for="password2"> password confirmation : </label>
        <input type="password" id="password2" v-model="password2">
        
        <input type="submit" value="SignUp">
        </form>
    </div>
</template>

<script>
export default {
    name: 'SignUpView',

    data() {
        return {
            username: null,
            nickname: null,
            password1: null,
            password2: null,
        };
    },

    mounted() {
        
    },

    methods: {
        signUp() {
            // console.log('signup')
            const username = this.username
            const nickname = this.nickname
            const password1 = this.password1
            const password2 = this.password2

            const payload = {
                username, nickname, password1, password2
            }

            this.$store.dispatch('signUp', payload)

        }
    },
};
</script>

<style scoped>

</style>