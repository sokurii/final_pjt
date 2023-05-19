<template>

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
                <label class="label-text" style="width: 120px;">아이디</label>
                <input type="text"  v-model="username" required style="display: inline-block; ">
                <!-- 아이디 <b-form-input v-model="username" placeholder="👤 아이디를 입력하세요" id="username" style="width: 300px; height: 50px;"></b-form-input> -->
              </div>

              <div class="mt-2">
                <label class="label-text" style="width: 120px;">비밀번호</label>
                <input type="text" v-model="password1" required>
              </div>
              <!-- <div style="margin-top: 10px;">
                <b-form-input type="password" v-model="password1" placeholder="🔑 비밀번호를 입력하세요" id="password1" style="width: 300px; height: 50px;"></b-form-input>
              </div> -->
              <div class="mt-2">
                <label class="label-text" style="width: 120px;">비밀번호 확인</label>
                <input type="text" v-model="password2" required>
              </div>
              <!-- <div style="margin-top: 10px; margin-bottom:20px;">
                <b-form-input type="password" v-model="password2" placeholder="✅ 비밀번호를 확인하세요" id="password2" style="width: 300px; height: 50px;"></b-form-input>
              </div> -->

              <div class="mt-2">
                <label class="label-text" style="width: 120px;">성별</label>
                <div class="radio-buttons">
                  <b-form-group>
                    <b-form-radio v-model="selectedGender" name="gender" value="male">남성</b-form-radio>
                    <b-form-radio v-model="selectedGender" name="gender" value="female">여성</b-form-radio>
                  </b-form-group>
                </div>
              </div>

              <div class='mt-2'>
                <label class="label-text" style="width: 120px;">나이</label>
                <select id="age" v-model="selectedAge">
                  <option v-for="age in ages" :key='age' :value="age">{{ age }}</option>
                </select>
              </div>   

              <div class="mt-2">
                <label class="label-text" style="width: 120px;">거주지</label>
                <select id='region' v-model="selectedResidence">
                  <option v-for="region in regions" :key="region" :value="region">{{ region }}</option>
                </select>
              </div>

              <div class="mt-2 mb-2">
                <div class="label-text" style="width: 120px;">소득??(미정)</div>
              </div>
  


              <b-button class="btn btn-warning" type="submit" style="width: 300px; height:50px;">회원가입</b-button><br>
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
      selectedGender: null,
      selectedAge: null,
      ages:[
        '10대',
        '20대',
        '30대',
        '40대',
        '50대 이상',
      ],
      selectedResidence:'',
      regions:[
          '서울특별시',
          '인천광역시',
          '대전광역시',
          '대구광역시',
          '광주광역시',
          '부산광역시',
          '울산광역시',
          '경기도',
          '강원도',
          '충청북도',
          '충청남도',
          '경상북도',
          '경상남도',
          '전라북도',
          '전라남도',
          '제주특별자치도',
      ]
    }
  },
  methods:{
    signUp(){
      const id = this.id
      const password1 = this.password1
      const password2 = this.password2
      const selectedGender = this.selectedGender
      const selectedAge =this.selectedAge
      const selectedResidence = this.selectedResidence

      const payload = {
        id, password1, password2, selectedGender, selectedAge, selectedResidence
      }
      this.$store.dispatch('signUp',payload)
      
    }
  }
}
</script>

<style>
.signupform{
  width: 60%;
  height: 70%;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.signup-container{
  display: flex;
  justify-content: space-between;
  height: 100%;
  /* background-color: #7ab87d; */
  background-color: #fff;
  border-radius: 20px ;
}

/* 왼쪽 */
.signup-left{
  width: 40%;
  background-color: #6da36f;
  border-top-left-radius: 20px;
  border-bottom-left-radius: 20px;
}

.sign-text {
  font-size: 70px;
  color: white;
  font-weight: bold;
  position: absolute; /* 추가 */
  top: 20%; /* 원하는 위치로 조정 */
  left: 20%; /* 원하는 위치로 조정 */
  transform: translate(-50%, -50%); /* 가운데 정렬 */
}

.sign-img {
  width: 30%;
  position: absolute; /* 추가 */
  top: 65%; /* 원하는 위치로 조정 */
  right: 39.1%; /* 원하는 위치로 조정 */
  transform: translate(-50%, -50%); /* 가운데 정렬 */
}

/* 오른쪽 */
.signup-right{
  width: 60%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
/* .sign-head{
  font-size: 28px;
  font-weight: bold;
  margin-bottom:40px
} */

.label-text {
  text-align: left;
  font-weight: bold;
}

.right-text{
  font-weight: bold;

}

/* 회원가입 추가 수정  */
input[type="text"] {
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 5px;
  width: 300px; 
  height: 40px;
}

.radio-buttons .custom-control {
  display: inline-block;
  margin-right: 10px;
  
}

select#age, #region{
  width: 300px;
  height: 40px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

</style>