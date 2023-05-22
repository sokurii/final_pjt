<template>

  <div class="right_wrap">
      <div class="notice">
        <h6>세율은 일반과세(15.4%)를 적용했으며, 실제와는 차이가 있을 수 있습니다.</h6>
      </div>

      <div class="fix_header d-flex justify-content-between p-3">
        <!-- <table class="main_table"> -->
          <!-- <colgroup>
            <col width="100px">
            <col width="100px">
            <col width="100px">
            <col width="200px">
            <col width="320px">      
          </colgroup> -->
          <thead>
          <th style="width: 100px">n개월</th>
          <th style="width: 100px">금리</th>
          <th style="width: 100px">지급방식</th>
          <th style="width: 100px">세전이자</th>
          <th style="width: 100px">세후이자</th>
          <th style="width: 200px">은행명</th>
          <th style="width: 320px">상품명</th>
          </thead>
        <!-- </table> -->
      </div> 

      <div class="fix_body d-flex justify-content-between">

        <!-- <table class="main_table content"> -->
            <!-- <colgroup>
              <col width="100px">
              <col width="100px">
              <col width="100px">
              <col width="100px">
              <col width="100px">
            </colgroup> -->

            <tbody >

              <tr v-for="product in filteredProducts" :key="product.id" class="body_content d-flex p-3 mt-1">
                <td>
                  <div class="row" v-for="option in product.depositoptions" :key="option.id">                
                    <div class="col" style="width: 100px">{{ option.save_trm }}</div>
                    <div class="col" style="width: 100px">{{ option.intr_rate }}</div>
                    <div class="col" style="width: 100px">{{ option.intr_rate_type_nm }}</div>
                    <div class="col" style="width: 100px">세전이자</div>
                    <div class="col" style="width: 100px">세후이자</div>
                    <!-- <td style="width: 100px">{{ option.intr_rate }} </td>
                    <td style="width: 100px">{{ option.intr_rate_type_nm }}</td>
                    <td style="width: 100px">세전이자</td>
                    <td style="width: 100px">세후이자</td> -->
                  </div>            
                </td>
                
                <td style="width: 200px">{{ product.kor_co_nm }}</td>
                <td style="width: 320px">
                  <router-link
                  :to ="{
                  name : 'depositDetail',
                  params: {fin_prdt_cd: product.fin_prdt_cd}
                  }"
                  >
                  {{ product.fin_prdt_nm }}
                  </router-link>
                </td>
              </tr>

            </tbody>
   
        <!-- </table> -->
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
    width: 1000px;
    padding-left: 80px;
    padding-top: 10px;
    /* padding-bottom: 90px; */
    min-height: -moz-calc( 100vh - 170px);
    min-height: calc( 100vh - 170px);
}
.fix_header{
  /* background-color: #F3F2E9; */
  background-color: #f3d993;
  border-radius: 10px;
}


</style>