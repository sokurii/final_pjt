<template>
  <div v-if='!isLogin'>
    <form class="loginform mx-auto" @submit.prevent="login">
      <div class="login-container">
        <!-- login-container 왼쪽 요소 -->
        <div class="login-img">
          <div class=log-text>HELLO🍀<br>모프가 알려주는<br>금융 정보를<br>무료로 즐기세요!</div>
          <div class=log-txt>My Monitoring Planner, MMoP</div>
          <img src="../assets/loginn.png" alt="" class='log-img'>
        </div>
        <!-- login-container 오른쪽 요소 -->
        <div class = 'logininput'>
          <img src="../assets/mmop.png" alt="" class='mmop'>
          <div class="input-container">
            <b-form-input v-model="id" placeholder="👤 아이디를 입력하세요" class="mb-3" ></b-form-input>
            <b-form-input type="password" v-model="password" placeholder="🔑 비밀번호를 입력하세요" class="mb-3"></b-form-input>
            <div class="id-save">
              <b-form-checkbox v-model="rememberId" inline>아이디 저장</b-form-checkbox>
            </div>
            <b-button variant="success" type="submit" style="height:50px;">Login</b-button><br>
            <router-link id="signup" to="/signup">회원가입</router-link>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
        id: null,
        password: null,
        rememberId:false
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
/* 로그인이랑 회원가입 창에 적용해보기  */
/* .header-filter:before {
    position: absolute;
    z-index: 1;
    width: 100%;
    height: 100%;
    display: block;
    left: 0;
    top: 0;
    content: "";
    background: rgba(0,0,0,.5);
} */

.loginform{
  width: 50%;
  height: 70%;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.login-container{
  display: flex;
  justify-content: space-between;
  background-color: #fff;
  border-radius: 20px ;
}

.login-img{
  display: flex;
  width: 50%;
  background-color: #f8d57b;
  border-top-left-radius: 20px;
  border-bottom-left-radius: 20px;
}

.login-img > div{
  position:absolute;
}

.log-img{
  position:relative;
  width: 80%;
  height: 100;
  opacity : 0.7;
  margin-top: 90px;
  margin-left: 50px;
  
}

.log-text{
  font-size: 27px;
  font-weight: 800;
  z-index: 1;
  text-align: left;
  margin-top: 50px;
  margin-left: 40px;
}

.log-txt{
  font-size:16px;
  font-weight: 400;
  z-index:1;
  margin-top: 215px;
  margin-left: 45px;
}
.logininput{
  width: 50% ;
  
} 

.mmop{
  width:25%;
  margin-top: 50px;
  margin-bottom: 20px;
  margin-right: 220px;
}

.input-container{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items:center;
  height: 70%;
}

.input-container>*{
  width: 300px;
  height: 50px;
}
.id-save{
  text-align: left;
}
</style>