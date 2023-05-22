<template>
  <div class="home">
    <div>
      <b-carousel
        id="carousel-fade"
        style="text-shadow: 0px 0px 2px #000"
        fade
        indicators
        img-width="1024"
        img-height="480"
      >
        <b-carousel-slide
          caption="First Slide"
          img-src="https://picsum.photos/1024/480/?image=10"
        ></b-carousel-slide>
        <b-carousel-slide
          caption="Second Slide"
          img-src="https://picsum.photos/1024/480/?image=12"
        ></b-carousel-slide>
        <b-carousel-slide
          caption="Third Slide"
          img-src="https://picsum.photos/1024/480/?image=22"
        ></b-carousel-slide>
      </b-carousel>
    </div>
    <div>
      <div class="section-1">
        <div class="inner">
          <div class="col-md-6 d-flex justify-content-center align-items-center">
            <img src="../assets/coin.png" alt="">
          </div>
          <div class="col-md-6 d-flex justify-content-center align-items-center">
            <div class="copy-box">
              <div class="title">예/적금 금리비교</div>
              <div class="copy">전국 금융기관의 예금, 적금 정보를<br>한 눈에 알려 드려요!</div>
              <button @click="goToFinance" to="/finance" class="btn btn-secondary">금융상품비교하기</button> 
            </div>
          </div>
        </div>
      </div>


      <div class="section-2">
        <div class="inner">
          <div class="col-md-6 d-flex justify-content-center align-items-center">
            <div class="copy-box">
              <div class="title">환율계산기</div>
              <div class="copy">내게 꼭 필요했던 환율,<br>ㅇㅇ에게 맡겨 보세요!</div>
              <button @click="goToExchange" to="/exchange" class="btn btn-secondary">환율계산하러가기</button> 
            </div>
          </div>
          <div class="col-md-6 d-flex justify-content-center align-items-center">
            <img src="../assets/cal.png" alt="" class="img-fluid mx-auto d-block" style="max-width: 50%; max-height: 50%;">
          </div>
        </div>
      </div>



      <div class="section-3">
        <div class="inner">
          <div class="col-md-6 d-flex justify-content-center align-items-center">
            <img src="../assets/bank.png" alt="" class="img-fluid mx-auto d-block" style="max-width: 50%; max-height: 50%;">
          </div>
          <div class="col-md-6 d-flex justify-content-center align-items-center">
            <div class="copy-box">
              <div class="title">우리동네은행</div>
              <div class="copy">마음에 드는 상품을 어디서 가입할까?<br>주변 은행을 찾아보세요!</div>
              <button @click="goToMap" to="/map" class="btn btn-secondary">우리동네은행찾기</button> 
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
    goToExchange() {
      if (this.isLogin) {
        this.$router.push({ name: 'exchange' })
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
  },
}
</script>


<style>

.home{
  width: 100%;
}

.section-1{
  display:flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 500px;
  background-color: #F3F2E9;
  /* background-color: #adbeae; */
  
  /* background-color: #FFAD3A; */
}

.section-2{
  display:flex;
  justify-content: center;
  align-items: center;  
  height: 500px;
  background-color: white;
}

.section-3{
  display:flex;
  justify-content: center;
  align-items: center;
  height: 500px;
  background-color: #F3F2E9;;
  /* background-color: #ebb262; */
}

.inner{
  width: 1060px;
  height: 500px;
  display: flex;
  /* flex-direction: column;
  justify-content: center;
  align-items: center; */
  /* background-color: #fff; */

}
.img{
  max-width: 50%;
  max-height: 50%;
  padding-top: 60px;
}

.copy-box{
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;

}


.copy-box .title{
  font-size : 36px;
  font-weight: 800;
  text-align: left;
}

.copy-box .copy{
  text-align: left;
  font-weight: 500;
  text-align: left;
}

.copy-box .btn{
  align-self:flex-start;
}
</style>
