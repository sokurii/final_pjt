<template>
  <div class="right_wrap">
    <div class="fix_header d-flex justify-content-between p-3">
      <thead>
        <th style="width: 100px">n개월</th>
        <th style="width: 100px">세전이자</th>
        <th style="width: 100px">세후이자</th>
        <th style="width: 200px">은행명</th>
        <th style="width: 320px">상품명</th>
      </thead>

    </div>

    <div class="fix_body d-flex justify-content-between">
      <tbody>
        <tr v-for="product in filteredProducts" :key="product.id" class="body_content d-flex p-3 mt-1">
          <td style="width: 100px">오 된당 ㅋㅋ</td>
          <td style="width: 100px">오 된당 ㅋㅋ</td>
          <td style="width: 100px">오 된당 ㅋㅋ</td>
          <td style="width: 200px">{{ product.kor_co_nm }}</td>
          <td style="width: 320px">
            <router-link :to="{
              name: 'savingDetail',
              params: { fin_prdt_cd: product.fin_prdt_cd }
            }">
              {{ product.fin_prdt_nm }}
            </router-link>
          </td>
        </tr>
      </tbody>
    </div>
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