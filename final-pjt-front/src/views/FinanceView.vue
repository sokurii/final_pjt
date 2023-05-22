<template>
  <div>
    <b-tabs content-class="bg-white">
      <h3>금융상품비교, 설명 div 만들기</h3>
      <b-tab title="정기예금" active class="tab">
        <div id="container">
          <DepositProductSearchInput @search-bank="getSearchBankD"/>
          <DepositProductList :bankD="bankD"/>
        </div>
      </b-tab>
      <b-tab title="정기적금">
        <div id="container">
          <SavingProductSearchInput @search-bank="getSearchBankS"/>
          <SavingProductList :bankS="bankS"/>
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
      bankD: null,
      bankS: null,
    }
  },
  methods: {
    getSearchBankD(bankD) {
      this.bankD = bankD
    },
    getSearchBankS(bankS) {
      this.bankS = bankS
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
}


</style>
