<template>
  <div>
    <SavingProductListItem 
      v-for="product in filteredProducts"
      :key="product.id"
      :product="product"
    />
  </div>
</template>

<script>
import SavingProductListItem from './SavingProductListItem.vue'

export default {
  name: 'SavingProductList',
  components: {
    SavingProductListItem,
  },
  props: {
    bankS: String,
  },
  computed: {
    savingProducts() {
      return this.$store.state.savingProducts
    },
    filteredProducts() {
      if (this.bankS === '전체') {
        return this.savingProducts
      }
      return this.savingProducts.filter(
        (savingProduct) => savingProduct.kor_co_nm === this.bankS
      )
    }
  },
  created() {
    this.getSavingProducts()
  },
  methods: {
    getSavingProducts() {
      this.$store.dispatch('getSavingProducts')
    }
  }
}
</script>

<style>

</style>