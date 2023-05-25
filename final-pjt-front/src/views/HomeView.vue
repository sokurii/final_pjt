<template>
  <div>
    <div class="home d-flex flex-column justify-content-center">
      <img class="main-img" src="../assets/main.png" alt="">
      <div><p class="board-title-text text-center"><strong>마이 모니터링 플래너, 모프</strong></p></div>
      <div><h4 class="text-center">개인 맞춤형 예적금 상품 서비스부터</h4></div>
      <div><h4 class="text-center">사람들과 공유하는 금융 커뮤니티까지</h4></div>
      <div><h4 class="text-center">모프와 함께 나만의 금융 플랜을 계획하세요!</h4></div>
    </div>

    <div>
      <div class="section-1">
        <div class="inner d-flex justify-content-around align-items-center">
          <div>
            <img src="../assets/coin.png" alt="" style="width:350px">
          </div>
          <div class="d-flex justify-content-center align-items-center">
            <div class="copy-box">
              <div class="title">예/적금 금리비교</div>
              <div class="copy">전국 금융기관의 예금, 적금 정보를<br>한 눈에 알려 드려요!</div><br>
              <button @click="goToFinance" to="/finance" class="btn btn-secondary">금융상품비교하기</button> 
            </div>
          </div>
        </div>
      </div>




      <div class="section-2">
        <div class="inner d-flex justify-content-around align-items-center">
          <div class="d-flex justify-content-center align-items-center">
            <div class="copy-box">
              <div class="title">우리동네은행</div>
              <div class="copy">마음에 드는 상품을 어디서 가입할까?<br>주변 은행을 찾아보세요!</div><br>
              <button @click="goToMap" to="/map" class="btn btn-secondary">우리동네은행찾기</button> 
            </div>
          </div>
          <div>
            <img src="../assets/map.png" alt="" style="width:400px">
          </div>
        </div>
      </div>

      <div class="section-3">
        <div class="inner d-flex justify-content-around align-items-center">
          <div>
            <img src="../assets/talk.png" alt="" style="width:300px">
          </div>
          <div class="d-flex justify-content-center align-items-center">
            <div class="copy-box">
              <div class="title">플래너 보드</div>
              <div class="copy">나의 금융 플래너를 짜보고,<br>사람들과 자유롭게 소통하세요!</div><br>
              <button @click="goToCommunity" to="/community" class="btn btn-secondary">게시판 구경하기</button> 
            </div>
          </div>
        </div>
      </div>


    </div>
  </div>
</template>

<script>
import { BCarousel, BCarouselSlide } from 'bootstrap-vue'

// @ is an alias to /src
export default {
  name: 'HomeView',
  components: {
    BCarousel,
    BCarouselSlide
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  methods: {
    goToFinance() {
      console.log(this.isLogin)
      if (this.isLogin) {
        this.$router.push({ name: 'finance' })
      } else {         
        alert('로그인이 필요한 서비스입니다.')
        this.$router.push({ name: 'login' })
      }
    },
    goToMap() {
      if (this.isLogin) {
        this.$router.push({ name: 'map' })
      } else {         
        alert('로그인이 필요한 서비스입니다.')
        this.$router.push({ name: 'login' })
      }
    },
    goToCommunity() {
      if (this.isLogin) {
        this.$router.push({ name: 'community' })
      } else {         
        alert('로그인이 필요한 서비스입니다.')
        this.$router.push({ name: 'login' })
      }
    },
  },
}
</script>


<style scoped>

.home{
  width: 100%;
  height: 700px;
  background-color: #F3F2E9;
  position: relative;
  z-index: -2;
  overflow: hidden;
}
.board-title-text{
  font-size: 60px
}
.text-center{
  padding-bottom: 10px;
  font-weight: 700;
}

.main-img {
  position: absolute;
  top: 45%;
  left: 50%;
  transform: translate(-50%, -50%);
  width:80%;
  object-fit: cover;
  opacity: 0.5;
  z-index: -1;
}
.section-1{
  display:flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 500px;
  background-color: white;
  /* background-color: #adbeae; */
  
  /* background-color: #FFAD3A; */
}

.section-2{
  display:flex;
  justify-content: center;
  align-items: center;  
  height: 500px;
  background-color: #F3F2E9;
}

.section-3{
  display:flex;
  justify-content: center;
  align-items: center;
  height: 500px;
  background-color: white;
  /* background-color: #ebb262; */
}

.inner{
  width: 1000px;
  height: 500px;
  display: flex;

}
.img{

  padding-top: 60px;
}

.copy-box{
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;

}


.copy-box .title{
  font-size : 48px;
  font-weight: 800;
  text-align: left;
}

.copy-box .copy{
  font-size : 20px;
  text-align: left;
  font-weight: 500;
  text-align: left;
}

.copy-box .btn {
  align-self: flex-start;
  font-size: 20px;
  width: 250px;
  height: 50px;
  background-color: #6da36f;
  color: white;
}

</style>
