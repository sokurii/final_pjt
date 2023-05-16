<template>
  <div>
    <h2>로그인</h2>
    <form class="loginform">
    <!-- <form @submit.prevent="login"> -->
      <div>
        <label>
          ID:
          <input type="text" v-model="form.id" required>
        </label>
      </div>
      <div>
        <label>
          Password:
          <input type="password" v-model="form.password" required>
        </label>
      </div>
      <button class="btn btn-success" type="submit">Login</button>
    </form>
    <router-link id="signup" to="/signup">회원가입</router-link>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      form: {
        id: '',
        password: ''
      }
    };
  },
  // methods: {
  //   login() {
  //     // 로그인 로직을 처리하는 함수
  //     // Vue.js에서는 이 부분에서 Django에서 사용하는 csrf 토큰이 필요하지 않습니다.
  //   }
  // }
};
</script>

<style scoped>
.loginform {
  border: solid;
  /* border-radius: ; */
}
</style>