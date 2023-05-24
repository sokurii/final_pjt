<template>
  <div>
    <div class="board-title d-flex flex-column align-items-center justify-content-center">
      <div><h1 class="board-title-text"><strong>한 눈에 보는 환율</strong></h1></div>
      <div>Lorem, ipsum dolor sit amet consectetur adipisicing elit.<br>Illum recusandae maxime temporibus blanditiis reprehenderit quos cumque nulla unde sunt</div>
      <!-- <img src="@/assets/document.png"  style="width : 10% ; transform:rotate(20deg);" > -->
    </div>
    <div class= "exchange-view d-flex">  
      <ExchangeList />
      <ExchangeCalculator />
    </div>
  </div>
</template>

<script>
import ExchangeList from '@/components/ExchangeList'
import ExchangeCalculator from '@/components/ExchangeCalculator'

export default {
  name: 'ExchangeView',
  components: {
    ExchangeList,
    ExchangeCalculator,
  }
}
</script>

<style>
.exchange-view{
  background-color: #fff;
  height: calc(100% - 200px);
}
</style>