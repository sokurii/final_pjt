<template>
  <div>
    <form class="loginform mx-auto" @submit.prevent="login">
      <div class="login-container">
        <!-- login-container 왼쪽 요소 -->
        <div class="login-img">
          <div class="log-text">HELLO🍀<br>모프가 알려주는<br>금융 정보를<br>무료로 즐기세요!</div>
          <div class="log-txt">My Monitoring Planner, MMoP</div>
          <img src="../assets/loginn.png" alt="" class="log-img">
        </div>
        <!-- login-container 오른쪽 요소 -->
        <div class="logininput">
          <img src="../assets/mmop.png" alt="" class="mmop">
          <div class="input-container">
            <div>
              <b-form-input v-model="form.id" placeholder="👤 아이디를 입력하세요" class="responsive-input"></b-form-input>
            </div>
            <div>
              <b-form-input type="password" v-model="form.password" placeholder="🔑 비밀번호를 입력하세요" class="responsive-input"></b-form-input>
            </div>

            <div class="id-save">
              <b-form-checkbox v-model="rememberId">
                <span style="margin-left: 5px;">아이디 저장</span>
              </b-form-checkbox>
            </div>              
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
        id: null,
        password: null
      },
      rememberId: false
    };
  },
  methods: {
    login() {
      const id = this.form.id;
      const password = this.form.password;

      const payload = {
        id,
        password
      };
      this.$store.dispatch('logIn', payload);
    }
  }
};
</script>

<style scoped>
.loginform {
  width: 50%;
  height: 70%;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.login-container {
  display: flex;
  justify-content: space-between;
  height: 100%;
  background-color: #fff;
  border-radius: 20px ;
}

.login-img {
  width: 50%;
  background-color: #f8d57b;
  border-top-left-radius: 20px;
  border-bottom-left-radius: 20px;
}

.login-img > div {
  position:absolute;
}

.log-img {
  width: 80%;
  opacity : 0.7;
  margin-top: 100px;
  margin-left: 10px;
}

.log-text {
  font-size: 27px;
  font-weight: 800;
  z-index: 1;
  text-align: left;
  margin-top: 50px;
  margin-left: 40px;
}

.log-txt {
  font-size: 16px;
  font-weight: 400;
  z-index: 1;
  margin-top: 215px;
  margin-left: 45px;
}

.logininput {
  width: 50% ;
}

.mmop {
  width: 25%;
  margin-top: 50px;
  margin-bottom: 20px;
  margin-right: 220px;
}

.input-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 70%;
}

.id-save {
  text-align: left;
}

.responsive-input {
  width: 300px;
  height: 50px;
}

@media screen and (max-width: 768px) {
  .loginform {
    width: 90%;
  }
  
  .login-container {
    flex-direction: column;
  }
  
  .login-img {
    border-radius: 20px 20px 0 0;
    width: 100%;
    height: 250px;
  }
  
  .log-img {
    margin-top: 40px;
    margin-left: 10px;
    width: 70%;
  }
  
  .log-text {
    font-size: 22px;
    margin-top: 30px;
    margin-left: 30px;
  }
  
  .log-txt {
    font-size: 14px;
    margin-top: 140px;
    margin-left: 35px;
  }
  
  .logininput {
    width: 100%;
    margin-top: 20px;
  }
  
  .mmop {
    margin-top: 30px;
    margin-bottom: 10px;
    margin-right: 0;
    width: 40%;
  }
  
  .responsive-input {
    width: 100%;
  }
  
  .id-save {
    margin-top: 10px;
    margin-bottom: 10px;
  }
}
</style>
