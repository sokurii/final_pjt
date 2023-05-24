<template>
  <div class="right_wrap">
    <div class="notice">
      <li>세율은 일반과세(15.4%)를 적용했으며, 실제와는 차이가 있을 수 있습니다.</li>
      <li>자유적립식도 정액적립식과 같은 월납입금액으로 가정하고 계산했습니다.</li>
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
          <th style="width: 100px">예치기간(개월)</th>
          <th style="width: 100px">금리(%)</th>
          <th style="width: 100px">적립방식</th>
          <th style="width: 100px">지급방식</th>
          <th style="width: 100px">예상세전이자(원)</th>
          <th style="width: 100px">예상세후이자(원)</th>
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
                  <div class="row" v-for="option in product.savingoptions" :key="option.id">                
                    <div class="col" style="width: 100px">{{ option.save_trm }}</div>
                    <div class="col" style="width: 100px">{{ option.intr_rate }}</div>
                    <div class="col" style="width: 100px">{{ option.rsrv_type_nm }}</div>
                    <div class="col" style="width: 100px">{{ option.intr_rate_type_nm }}</div>

                    <div v-if="option.intr_rate_type_nm === '단리'" class="col" style="width: 100px">{{ ((payloadS.depositAmount * ( 0.01 * option.intr_rate ) * ( option.save_trm + 1 ) * ( option.save_trm ) / 2) / 12).toFixed(0) }}</div>
                    <div v-else class="col" style="width: 100px">{{ (payloadS.depositAmount * option.save_trm * 0.01 * option.intr_rate * 0.55).toFixed(0) }}</div>
                    
                    <div v-if="option.intr_rate_type_nm === '단리'" class="col" style="width: 100px">{{ (((payloadS.depositAmount * ( 0.01 * option.intr_rate ) * ( option.save_trm + 1 ) * ( option.save_trm ) / 2) / 12) * (1 - 0.154)).toFixed(0) }}</div>
                    <div v-else class="col" style="width: 100px">{{ ((payloadS.depositAmount * option.save_trm * 0.01 * option.intr_rate * 0.55) * (1 - 0.154)).toFixed(0) }}</div>
                    <!-- <td style="width: 100px">{{ option.intr_rate }} </td>
                    <td style="width: 100px">{{ option.intr_rate_type_nm }}</td>
                    <td style="width: 100px">세전이자</td>
                    <td style="width: 100px">세후이자</td> -->
                  </div>            
                </td>
                <td style="width: 200px">{{ product.kor_co_nm }}</td>
                <td style="width: 320px">
                  <b-button v-b-modal="product.fin_prdt_cd">{{ product.fin_prdt_nm }}</b-button>

                  <b-modal :id="product.fin_prdt_cd" title="상품 상세 정보">
                    <SavingtProductDetail :fin_prdt_cd="product.fin_prdt_cd"/>
                  </b-modal>
                </td>
              </tr>

            </tbody>
   
        <!-- </table> -->
      </div>
  </div>
</template>

<script>
import SavingtProductDetail from './SavingProductDetail.vue'

export default {
  name: 'SavingProductList',
  components: {
    SavingtProductDetail,
  },
  props: {
    payloadS: Object,
  },
  computed: {
    savingProducts() {
      return this.$store.state.savingProducts
    },
    filteredProducts() {
      if (this.payloadS.selectBank === '전체') {
        return this.savingProducts
      }
      return this.savingProducts.filter(
        (savingProduct) => savingProduct.kor_co_nm === this.payloadS.selectBank
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