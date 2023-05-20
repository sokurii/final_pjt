<template>
  <div>
    <h1 class="d-flex m-4">금융상품조회</h1>
    <b-tabs content-class="mt-3">
      <b-tab title="정기예금" active>
        <div class="d-flex m-4">
          <DepositProductSearchInput @search-bank="getSearchBankD"/>
          <DepositProductList :bankD="bankD"/>
        </div>
      </b-tab>
      <b-tab title="정기적금">
        <div class="d-flex m-4">
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

</style>
