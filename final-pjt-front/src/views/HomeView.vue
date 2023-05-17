<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png"> -->
    <div>
      <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="4000"
        controls
        indicators
        
        img-width="1024"
        img-height="480"
        style="text-shadow: 1px 1px 2px #333;"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
        :crossfade="true"
        fade
        
      >
        <!-- Text slides with image -->
        <b-carousel-slide
          caption="First slide"
          text="Nulla vitae elit libero, a pharetra augue mollis interdum."
          img-src="https://picsum.photos/1024/480/?image=52"
        ></b-carousel-slide>

        <!-- Slides with custom text -->
        <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=54">
          <h1>Hello world!</h1>
        </b-carousel-slide>

        <!-- Slides with image only -->
        <b-carousel-slide img-src="https://picsum.photos/1024/480/?image=58"></b-carousel-slide>

          <!-- Slides with img slot -->
          <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
        <b-carousel-slide>
          <template #img>
            <img
              class="d-block img-fluid w-100"
              width="1024"
              height="480"
              src="https://picsum.photos/1024/480/?image=55"
              alt="image slot"
            >
          </template>
        </b-carousel-slide>

        <!-- Slide with blank fluid image to maintain slide aspect ratio -->

      </b-carousel>

    </div>

      <div class="section-1">
        <div class="inner">
          <div class="col-md-6 d-flex justify-content-center align-items-center">
            <img src="../assets/coin.png" alt="">
          </div>
          <div class="col-md-6 d-flex justify-content-center align-items-center">
            <div class="copy-box">
              <div class="title">예/적금 금리비교</div>
              <div class="copy">전국 금융기관의 예금, 적금 정보를<br>한 눈에 알려 드려요!</div>
              <router-link to="/finance" class="btn btn-secondary">금융상품비교하기</router-link> 
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
              <router-link to="/finance" class="btn btn-secondary">환율계산하러가기</router-link> 
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
              <router-link to="/finance" class="btn btn-secondary">우리동네은행찾기</router-link> 
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
  }
}
</script>


<style>



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