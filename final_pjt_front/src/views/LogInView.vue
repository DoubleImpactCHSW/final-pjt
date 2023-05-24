<template>
  <div class="login-container">
    <h1 class="login-title">Log In</h1>
    <form @submit.prevent="login" class="login-form">
      <div class="form-group">
        <label for="username" class="form-label">Username</label>
        <input
          class="form-input"
          type="text"
          id="username"
          v-model="username"
        />
      </div>

      <div class="form-group">
        <label for="password" class="form-label">Password</label>
        <input
          class="form-input"
          type="password"
          id="password"
          v-model="password"
        />
      </div>

      <button type="submit" class="login-button">Log In</button>
    </form>

    <div class="signup-section">
      <p>Not a member yet?</p>
      <button @click="goSignUp" class="signup-button">Sign Up</button>
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

  mounted() {},

  methods: {
    login() {
      const username = this.username;
      const password = this.password;

      const payload = {
        username,
        password,
      };

      this.$store.dispatch('login', payload);
    },
    goSignUp() {
      this.$router.push({ name: 'signup' });
    },
  },
  beforeRouteUpdate(to, from, next) {
    if (to.path === from.path) {
      next(false);
    } else {
      next();
    }
  },
};
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f6f6f6;
  border: 2px solid #ccc;
  border-radius: 8px;
  animation: backgroundAnimation 10s infinite alternate ease-in-out;
}

.login-title {
  text-align: center;
  font-size: 24px;
  margin-bottom: 20px;
}

.login-form .form-group {
  margin-bottom: 20px;
}

.form-label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.login-button {
  display: block;
  width: 100%;
  padding: 10px;
  background-color: #4caf50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.signup-section {
  margin-top: 20px;
  text-align: center;
}

.signup-button {
  padding: 10px 20px;
  background-color: #fff;
  border: 1px solid #4caf50;
  border-radius: 4px;
  color: #4caf50;
  cursor: pointer;
}

@keyframes backgroundAnimation {
  0% {
    background-color: #f6f6f6;
  }
  50% {
    background-color: #ebebeb;
  }
  100% {
    background-color: #f6f6f6;
  }
}
</style>
