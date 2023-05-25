<template>
  <div>
    <div class="board-title d-flex flex-column justify-content-center">
      <img class="board-img" src="../assets/zoom.png" alt="">
      <div><h1 class="board-title-text text-center"><strong>금융상품비교</strong></h1></div>
      <div><h5 class="text-center pt-3">모프에서 전국 금융기관이 제공하는 예적금 상품을 확인하세요!</h5></div>
      <div><h5 class="text-center">예치금액, 기간, 이자율, 이자지급방식까지 원하는 상품을 찾아드려요 :D</h5></div>
    </div>

    <b-tabs content-class="bg-white">
      <b-tab title="정기예금" active class="tab">
        <div id="container">
          <DepositProductSearchInput @search-bank="getSearchD"/>
          <DepositProductList :payloadD="payloadD"/>
        </div>
      </b-tab>
      <b-tab title="정기적금">
        <div id="container">
          <SavingProductSearchInput @search-bank="getSearchS"/>
          <SavingProductList :payloadS="payloadS"/>
        </div>
      </b-tab>
    </b-tabs>
  </div>
</template>

<script>
import DepositProductSearchInput from '@/components/DepositProductSearchInput'
import DepositProductList from '@/components/DepositProductList'
import SavingProductSearchInput from '@/components/SavingProductSearchInput'
import SavingProductList from '@/components/SavingProductList'

export default {
  name: 'FinanceView',
  components: {
    DepositProductSearchInput,
    DepositProductList,
    SavingProductSearchInput,
    SavingProductList,
  },
  data() {
    return {
      payloadD: {},
      payloadS: {},
    }
  },
  methods: {
    getSearchD(payloadD) {
      this.payloadD = payloadD
    },
    getSearchS(payloadS) {
      this.payloadS = payloadS
    },
  }

}
</script>

<style scoped>
.finance{
  background-color: white;
}
#container {
  padding-top: 50px;
  padding-bottom: 90px;
  width: 1200px;
  margin: 0 auto;
  display: flex;
  height: 100vh;
  flex-grow:1;
}


.board-title {
  position: relative;
  z-index: -2;
  overflow: hidden;
}

.board-img {
  position: absolute;
  top: 50%;
  left: 53%;
  transform: translate(-50%, -50%);
  width:650px;
  object-fit: cover;
  opacity: 0.5;
  z-index: -1;
}
.board-title > h5{
  font-weight: 800;
}


</style>