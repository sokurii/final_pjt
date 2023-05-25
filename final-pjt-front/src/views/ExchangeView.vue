<template>
  <div>
    <div class="board-title d-flex flex-column justify-content-center">
      <img class="exchange-img" src="../assets/exchange.png" alt="">
      <div><h1 class="board-title-text text-center"><strong>한 눈에 보는 환율</strong></h1></div>
      <div><h5 class="text-center pt-3">모프에서 제공하는 환율 정보를 확인하세요</h5></div>
      <div><h5 class="text-center">금융정보도 챙기고 필요한 환율도 알아보면 일석이조!</h5></div>
    </div>
    <div class="d-flex">
      <ExchangeCalculator />
      <ExchangeList />
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
.exchange-img {
  position: absolute;
  top: 45%;
  left: 50%;
  transform: translate(-50%, -50%);
  width:650px;
  object-fit: cover;
  opacity: 0.5;
  z-index: -1;
}
</style>