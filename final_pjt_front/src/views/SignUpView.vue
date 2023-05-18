<template>
    <div>
        <h1>회원가입 View</h1>
        <form @submit.prevent="signUp">
        <label for="username">id</label>
        <input type="text" id="username" v-model="username"><br>

        <label for="email">email</label>
        <input type="text" id="email" v-model="email"><br>

        <label for="password1"> password</label>
        <input type="password" id="password1" v-model="password1"><br>

        <label for="password2"> password confirmation</label>
        <input type="password" id="password2" v-model="password2"><br>
        
        <label for="nickname">nickname</label>
        <input type="text" id="nickname" v-model="nickname"><br>

        <b-button type="submit" variant="success"> Sign Up </b-button>
        </form>
        <div>
            <p v-if="inputNull" class="font-weight-bold text-danger">모든 항목은 필수 입력입니다.</p>
        </div>
        <div>
                <p v-for="(value, key) in errorData" :key="key" class="font-weight-bold text-danger">
                    {{ value[0] }}
                </p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SignUpView',

    data() {
        return {
            username: '',
            email: '',
            password1: '',
            password2: '',
            nickname: '',
        };
    },

    computed: {
        inputNull() {
            return !(this.username && this.email && this.password1 && this.password2 && this.nickname)
        },
        errorData() {
            return this.$store.state.signUpError
        }
    },

    methods: {
        signUp() {
            // console.log('signup')
            const username = this.username
            const email = this.email
            const password1 = this.password1
            const password2 = this.password2
            const nickname = this.nickname

            const payload = {
                username, email, password1, password2, nickname
            }

            this.$store.dispatch('signUp', payload)

        }
    },
};
</script>

<style scoped>

</style>