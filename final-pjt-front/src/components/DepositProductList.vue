<template>
  <div class="right_wrap">
    <!-- <DepositProductListItem 
      v-for="product in filteredProducts"
      :key="product.id"
      :product="product"
    /> -->
    <div v-for="product in filteredProducts" :key="product.id" class="right_wrap">
      <p>은행명 : {{ product.kor_co_nm }}</p>
      <p>
        금융상품명:
        <router-link
            :to ="{
            name : 'depositDetail',
            params: {fin_prdt_cd: product.fin_prdt_cd}
          }"
        >
          {{ product.fin_prdt_nm }}
        </router-link>
      </p>
    </div>
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
.right_wrap{
    width: 986px;
    padding-left: 38px;
    /* border-left: 1px solid #ddd; */
    padding-top: 50px;
    padding-bottom: 90px;
    min-height: -moz-calc( 100vh - 170px);
    min-height: calc( 100vh - 170px);
}
</style>