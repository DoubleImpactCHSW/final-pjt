<template>
  <div class="signup-container">
    <form @submit.prevent="signUp" class="signup-form">
      <label for="username">ID</label>
      <input type="text" id="username" v-model="username" /><br />

      <label for="email">Email</label>
      <input type="text" id="email" v-model="email" /><br />

      <label for="password1">Password</label>
      <input type="password" id="password1" v-model="password1" /><br />

      <label for="password2">Password Confirmation</label>
      <input type="password" id="password2" v-model="password2" /><br />

      <label for="nickname">Nickname</label>
      <input type="text" id="nickname" v-model="nickname" /><br />

      <b-button type="submit"  class="custom-success signup-button">Sign Up</b-button>
    </form>

    <div class="error-messages">
      <p v-if="inputNull" class="error-message">
        모든 항목은 필수 입력입니다.
      </p>

      <div v-for="(value, key) in errorData" :key="key" class="error-message">
        {{ value[0] }}
      </div>
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
      return !(
        this.username &&
        this.email &&
        this.password1 &&
        this.password2 &&
        this.nickname
      );
    },
    errorData() {
      return this.$store.state.signUpError ?? [];
    },
  },

  methods: {
    signUp() {
      // console.log('signup')
      const username = this.username;
      const email = this.email;
      const password1 = this.password1;
      const password2 = this.password2;
      const nickname = this.nickname;

      const payload = {
        username,
        email,
        password1,
        password2,
        nickname,
      };

      this.$store.dispatch('signUp', payload);
    },
  },
};
</script>

<style scoped>
.signup-container {
  max-width: 500px;
  margin: 50px auto;
  padding: 10px 50px;
  border-radius: 15px;
  background-color: #f1ece3;
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.3);
}

label {
  font-size: 24px;
}

.signup-form label {
  color: #8d6e63;
  margin-bottom: 5px;
}

.signup-form input[type="text"],
.signup-form input[type="password"] {
  width: 100%;
  padding: 5px;
  margin-bottom: 10px;
  border: 1px solid #8d6e63;
  border-radius: 3px;
}

.signup-form input[type="submit"] {
  margin-top: 10px;
}

.error-messages {
  margin-top: 10px;
}

.error-message {
  font-weight: bold;
  color: #b71c1c;
}

.signup-button {
  background-color: #BCAAA4;
  border-color: #BCAAA4;
  color: #FFFFFF;
  width: 100%;
  font-size: 24px;
  font-weight: bold;
  margin-top: 15px;
}

.signup-button:hover,
.signup-button:focus {
  background-color: #8D6E63;
  border-color: #8D6E63;
  color: #FFFFFF;
}
</style>
