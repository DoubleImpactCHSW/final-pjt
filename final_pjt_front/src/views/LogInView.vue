<template>
    <div>
        <h1>Log In</h1>
        <form @submit.prevent="login">
        <label for="username">username</label>
        <input class="ml-3 mb-2" type="text" id="username" v-model="username"><br>

        <label for="password"> password</label>
        <input class="ml-3 mb-2" type="password" id="password" v-model="password"><br>

        <b-button variant="primary">Log In</b-button>
        </form>
        <div class="m-3 p-3 border">
            <p>아직 회원이 아니신가요?</p>
            <b-button @click="goSignUp" variant="outline-primary">Sign Up</b-button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'LogInView',

    data() {
        return {
            username: null,
            password: null,
        };
    },

    mounted() {
        
    },

    methods: {
        login() {
            const username = this.username
            const password = this.password

            const payload = {
                username, password
            }

            this.$store.dispatch('login', payload)
        },
        goSignUp() {
            this.$router.push({ name: 'signup' })
        }
    },
};
</script>

<style scoped>

</style>