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

    <div class="index-contents">
      <div class="section-1">
        <div class="inner">
          <div class="img"><img src="../assets/coin.png" alt=""></div>
          <div class="copy-box">
            <div class="title">예/적금금리비교</div>
            <div class="copy">전국 금융기관의 예금, 적금 정보를<br>한 눈에 알려 드려요!</div>
            <router-link to="/finance" class="btn btn-secondary">금융상품비교하기</router-link> 
          </div>
        </div>
      </div>

      <div class="section-2">
        <div class="inner">
          <div class="copy-box">
            <div class="title">환율계산기</div>
            <div class="copy">지금 환율은 얼마? </div>
            <router-link to="/finance" class="btn btn-secondary">환율계산 하러가기</router-link> 
          <!-- <div class="img"><img src="../assets/coin.png" alt=""></div>             -->
        </div>
      </div>

      <div class="section-3">
        <div class="inner">
          <div class="copy-box">
            <div class="title">우리동네은행찾기</div>
            <div class="copy">지금 가장 가까운 은행은 어디?</div>
            <router-link to="/map" class="btn btn-secondary">근처 은행 찾아보기</router-link> 
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
  height: 500px;
  background-color: #F3F2E9;
  /* background-color: #adbeae; */
  
  /* background-color: #FFAD3A; */
}

.section-2{
  
  height: 500px;
  background-color: white;
}

.section-3{
  height: 500px;
  background-color: #F3F2E9;;
  /* background-color: #ebb262; */
}

.inner{
  width: 1060px;
  height: 500px;
  /* background-color: #fff; */

}
.img{
  max-width: 50%;
  max-height: 50%;
  padding-top: 60px;
}

.copy-box{
  float: right;
  padding-right: 60px;
  


}
.title{
  font-size : 36px;
  font-weight: 800;

}

.copy{
  text-align: left;
  font-weight: 500;
}
</style>