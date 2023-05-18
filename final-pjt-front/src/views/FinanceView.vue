<template>
  <div>
    <h1 class="d-flex m-4">금융상품조회</h1>
    <div class="d-flex m-4">
      <ProductSearchInput @search-bank="getSearchBank"/>
      <ProductList :bank="bank"/>
    </div>
  </div>
</template>

<script>
import ProductSearchInput from '@/components/ProductSearchInput'
import ProductList from '@/components/ProductList'

export default {
  name: 'FinanceView',
  components: {
    ProductSearchInput,
    ProductList,
  },
  data() {
    return {
      bank: null,
    }
  },
  methods: {
    getSearchBank(bank) {
      this.bank = bank
    }
  }

}
</script>

<style scoped>

</style>
