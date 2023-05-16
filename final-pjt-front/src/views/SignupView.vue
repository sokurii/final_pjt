<template>
  <div>
    <h2>회원가입</h2>
    <form class="signupform">
    <!-- <form @submit.prevent="signUp"> -->
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
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
      username: null,
      password1: null,
      password2: null,
    }
  },
}
</script>

<style>
.signupform {
  border: solid;
  margin: 2px 100px;
}
</style>