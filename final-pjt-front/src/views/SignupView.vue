<template>
  <div>
    <form class="signupform mx-auto" @submit.prevent="signup">
      <div class="signup-container">
        <!-- login-container 왼쪽 요소 -->
          <div class="signup-left">
            <div class="sign-text">Welcome</div>
            <img src="../assets/signupp.png" alt="" class='sign-img'>
          </div>
        <!-- login-container 오른쪽 요소 -->
          <div class = 'signup-right'>
            <!-- <img src="../assets/mmop.png" alt="" class='mmop'> -->
            <!-- <div class="sign-head">회원가입</div> -->
            <div class="input-container">
              <div> 
                <div class="label-text" style="width: 120px;">아이디</div>
                <input type="text"  v-model="username" required style="display: inline-block; ">
                <!-- 아이디 <b-form-input v-model="username" placeholder="👤 아이디를 입력하세요" id="username" style="width: 300px; height: 50px;"></b-form-input> -->
              </div>

              <div class="mt-2">
                <div class="label-text" style="width: 120px;">비밀번호</div>
                <input type="text" v-model="password1" required>
              </div>
              <!-- <div style="margin-top: 10px;">
                <b-form-input type="password" v-model="password1" placeholder="🔑 비밀번호를 입력하세요" id="password1" style="width: 300px; height: 50px;"></b-form-input>
              </div> -->
              <div class="mt-2">
                <div class="label-text" style="width: 120px;">비밀번호 확인</div>
                <input type="text" v-model="password2" required>
              </div>
              <!-- <div style="margin-top: 10px; margin-bottom:20px;">
                <b-form-input type="password" v-model="password2" placeholder="✅ 비밀번호를 확인하세요" id="password2" style="width: 300px; height: 50px;"></b-form-input>
              </div> -->

              <div class="mt-2">
                <div class="label-text" style="width: 120px;">성별</div>
                <div class="radio-buttons">
                  <b-form-group>
                    <b-form-radio v-model="selectedGender" name="gender" value="male">남성</b-form-radio>
                    <b-form-radio v-model="selectedGender" name="gender" value="female">여성</b-form-radio>
                  </b-form-group>
                </div>
              </div>

              <div class='mt-2'>
                <div class="label-text" style="width: 120px;">나이</div>
                <select id="age" v-model="selectedAge">
                  <option v-for="age in ages" :key='age' :value="age">{{ age }}</option>
                </select>
              </div>   

              <div class="mt-2">
                <div class="label-text" style="width: 120px;">거주지</div>
                <select id='region' v-model="selectedResidence">
                  <option v-for="region in regions" :key="region" :value="region">{{ region }}</option>
                </select>
              </div>

              <div class="mt-2 mb-2">
                <div class="label-text" style="width: 120px;">소득??(미정)</div>
              </div>
  


              <b-button class="btn btn-warning" type="submit" style="width: 300px; height:50px;">회원가입</b-button>
              <router-link id="login" to="/login"  class="mt-3">로그인으로 돌아가기</router-link>
            </div>
          </div>
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