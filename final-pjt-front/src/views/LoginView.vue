<template>

  <div class='loginview'>
    <h2>배경이 있었으면 좋겠음, 사이즈도 고민</h2>
    <form class="loginform" @submit.prevent="login">
      <div class="login-container">
          <div class="login-img">
            <span class=log-text>지금 로그인하고<br>ㅇㅇ한 환경을<br>경험하세요</span>
            <img src="../assets/login.png" alt="" class='log-img'>
          </div>

          <div class = 'logininput'>
            <img src="../assets/mmop.png" alt="" class='mmop'>
            <div class="input-container">
              <div> 
                <!-- <b-form-input v-model="text" placeholder="👤 아이디를 입력하세요" style="width: 300px; height:50px;" ></b-form-input> -->
                <b-form-input v-model="form.id" placeholder="👤 아이디를 입력하세요" style="width: 300px; height:50px;" ></b-form-input>
              </div>
              <div style="margin-top: 10px; margin-bottom:20px;">
                <!-- <b-form-input v-model="text" placeholder="🔑 비밀번호를 입력하세요" style="width: 300px; height:50px;"></b-form-input> -->
                <b-form-input type="password" v-model="form.password" placeholder="🔑 비밀번호를 입력하세요" style="width: 300px; height: 50px;"></b-form-input>
              </div>

              <div class="id-save" style="margin-top: -10px; margin-bottom:20px; width:300px ">
                <b-form-checkbox v-model="rememberId">
                  <span style="margin-left: 5px;">아이디 저장</span>
                </b-form-checkbox>
                <!-- <input type="checkbox" v-model="rememberId">
                <label for="remember">아이디 저장</label> -->
              </div>              
              <!-- <b-form-checkbox v-model="saveId">아이디 저장</b-form-checkbox> -->
              <b-button class="btn btn-success" type="submit" style="width: 300px; height:50px;">Login</b-button><br>
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
      form: {
        id: '',
        password: ''
      },
      remmerberId:false
    };
  },
  methods: {
    login() {
      // 로그인 로직을 처리하는 함수
      // Vue.js에서는 이 부분에서 Django에서 사용하는 csrf 토큰이 필요하지 않습니다.
    }
  }
};
</script>

<style>
.loginview{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items:center;
  height: 100vh;

}

.loginform{
  width: 760px;
  height: 450px;
  margin-bottom: 200px;
  background-color: #fff;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);

}

.login-container{
  display: flex;
  justify-content: space-between;
  height: 100%;
  

}

.login-img{
  width: 50%;
  background-color: #F8D479;
}

.login-img > span{
  position:absolute;
}

.log-img{
  width: 100%;
  opacity : 0.4;
  margin-top: 50px;
  margin-right: 30px;
  
}

.log-text{
  font-size: 36px;
  font-weight: bold;
  z-index: 1;
  text-align: left;
  margin-top: 40px;
  margin-left: 30px;
}
.logininput{
  width: 50% ;
} 

.mmop{
  width:30%;
  margin-top: 60px;
  margin-bottom: 20px;
  margin-right: 200px;
}

.input-container{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items:center;
  height: 60%;
}

.id-save{
  text-align: left;
}
</style>