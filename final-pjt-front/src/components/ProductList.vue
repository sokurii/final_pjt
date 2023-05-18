<template>
  <div>
    <ProductListItem 
      v-for="product in filteredProducts"
      :key="product.id"
      :product="product"
    />
  </div>
</template>

<script>
import ProductListItem from './ProductListItem.vue'

export default {
  name: 'ProductList',
  components: {
    ProductListItem,
  },
  props: {
    bank: String,
  },
  computed: {
    products() {
      return this.$store.state.products
    },
    filteredProducts() {
      if (this.bank === '전체') {
        return this.products
      }
      return this.products.filter(
        (product) => product.kor_co_nm === this.bank
      )
    }
  },
  created() {
    this.getDepositProducts()
  },
  methods: {
    getDepositProducts() {
      this.$store.dispatch('getDepositProducts')
    }
  }
}
</script>

<style>

</style>