<template>

  <div class='loginview'>
    <form class="loginform" @submit.prevent="login">
      <div class="login-container">
          <div class="login-img">
            <div class=log-text>Welcome🎉<br>모프가 알려주는<br>금융 정보를<br>무료로 즐기세요!</div>
            <div class=log-txt>My Monitoring Planner, MMoP</div>
            <img src="../assets/loginn.png" alt="" class='log-img'>
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
.content {
  /* position: absolute; */
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  /* background-color: rgba(0, 0, 0, 0.5); */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items:center;
}
/* .loginview{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items:center;
  height: 100vh;

} */

.loginform{

  
  width: 760px;
  height: 450px;
  /* margin-bottom: 200px; */
  background-color: #fff;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
  border-radius: 20px;
}

.login-container{
  display: flex;
  justify-content: space-between;
  height: 100%;
  
  

}

.login-img{
  width: 50%;
  background-color: #f8d57b;
  border-top-left-radius: 20px;
  border-bottom-left-radius: 20px;
}

.login-img > div{
  position:absolute;
}

.log-img{
  width: 80%;
  opacity : 0.7;
  margin-top: 100px;
  margin-left: 10px;
  
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

.id-save{
  text-align: left;
}
</style>