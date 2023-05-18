<template>
  <div>
    <h2>로그인</h2>
    <form class="loginform" @submit.prevent="login">
      <div>
        <label for="id">ID:</label>
        <input type="text" id="id" v-model="id">
      </div>
      <div>
        <label for="password">Password:</label>
          <input type="password" id="password" v-model="password">
      </div>
      <button class="btn btn-success" type="submit">Login</button>
    </form>
    <router-link id="signup" to="/signup">
      <button class="btn btn-primary">
        회원가입
      </button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
        id: null,
        password: null
    };
  },
  methods: {
    login() {
      const id = this.id
      const password = this.password

      const payload = {
        id, password
      }
      this.$store.dispatch('logIn', payload)
    }
  }
};
</script>

<style scoped>
.loginform {
  border: solid;
  /* border-radius: ; */
}
</style>