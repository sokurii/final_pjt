<template>
  <div>
    <p>FinanceView</p>
    <div>
      <ProductSearchInput />
      <ProductList />
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
  }

}
</script>

<style>

</style>
