<template>

    <form class="signupform mx-auto" @submit.prevent="login">
      <div class="signup-container">
        <!-- login-container 왼쪽 요소 -->
          <div class="signup-left">
            <div class="sign-text">Welcome</div>
            <img src="../assets/signupp.png" alt="" class='sign-img'>
          </div>
        <!-- login-container 오른쪽 요소 -->
          <div class = 'signup-right'>
            <!-- <img src="../assets/mmop.png" alt="" class='mmop'> -->
            <div class="sign-head">회원가입</div>
            <div class="input-container">
              <div> 
                <b-form-input v-model="username" placeholder="👤 아이디를 입력하세요" id="username" style="width: 300px; height: 50px;"></b-form-input>
              </div>
              <div style="margin-top: 10px;">
                <b-form-input type="password" v-model="password1" placeholder="🔑 비밀번호를 입력하세요" id="password1" style="width: 300px; height: 50px;"></b-form-input>
              </div>
              <div style="margin-top: 10px; margin-bottom:20px;">
                <b-form-input type="password" v-model="password2" placeholder="✅ 비밀번호를 확인하세요" id="password2" style="width: 300px; height: 50px;"></b-form-input>
              </div>
              <b-button class="btn btn-warning" type="submit" style="width: 300px; height:50px;">회원가입</b-button>
              <router-link id="login" to="/login"  class="mt-3">로그인으로 돌아가기</router-link>
            </div>
          </div>
      </div>
    </form>
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
.signupform{
  width: 760px;
  height: 450px;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.signup-container{
  display: flex;
  justify-content: space-between;
  height: 100%;
  background-color: #7ab87d;
  border-radius: 20px ;
}

/* 왼쪽 */
.signup-left{
  width: 45%;
  background-color: #6da36f;
  border-top-left-radius: 20px;
  border-bottom-left-radius: 20px;
}

.sign-text {
  font-size: 60px;
  color: white;
  font-weight: bold;
  position: absolute; /* 추가 */
  top: 20%; /* 원하는 위치로 조정 */
  left: 23%; /* 원하는 위치로 조정 */
  transform: translate(-50%, -50%); /* 가운데 정렬 */
}

.sign-img {
  width: 30%;
  position: absolute; /* 추가 */
  top: 65%; /* 원하는 위치로 조정 */
  left: 36%; /* 원하는 위치로 조정 */
  transform: translate(-50%, -50%); /* 가운데 정렬 */
}

/* 오른쪽 */
.signup-right{
  width: 55%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.sign-head{
  font-size: 30px;
  font-weight: bold;
}
.align-thing{
  text-align: left;
}
.right-text{
  font-weight: bold;
}
</style>