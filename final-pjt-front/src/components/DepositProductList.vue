<template>
  <div>
    <DepositProductListItem 
      v-for="product in filteredProducts"
      :key="product.id"
      :product="product"
    />
  </div>
</template>

<script>
import DepositProductListItem from './DepositProductListItem.vue'

export default {
  name: 'DepositProductList',
  components: {
    DepositProductListItem,
  },
  props: {
    bankD: String,
  },
  computed: {
    depositProducts() {
      return this.$store.state.depositProducts
    },
    filteredProducts() {
      if (this.bankD === '전체') {
        return this.depositProducts
      }
      return this.depositProducts.filter(
        (depositProduct) => depositProduct.kor_co_nm === this.bankD
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