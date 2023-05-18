<template>
  <div>
    <h2>회원가입</h2>
    <form class="signupform" @submit.prevent="signUp">
      <label for="id">ID : </label>
      <input type="text" id="id" v-model="id"><br>

      <label for="password1"> 비밀번호 : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> 비밀번호 확인 : </label>
      <input type="password" id="password2" v-model="password2">
      
      <div>
        <button class="btn btn-primary">회원가입</button>    
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      id: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const id = this.id
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        id, password1, password2
      }
      this.$store.dispatch('signUp', payload)
    }
  }
}
</script>

<style>
.signupform {
  border: solid;
  margin: 2px 100px;
}
</style>