<template>
  <div>
    <p>공시 제출월 : {{ product.dcls_month }}</p>
    <p>은행명 : {{ product.kor_co_nm }} </p>
    <p>금융상품명 : 
      <router-link
      :to="{
        name: 'depositDetail',
        params: { fin_prdt_cd: product.fin_prdt_cd }
      }"
      >
        {{ product.fin_prdt_nm }}
      </router-link>
    </p>
    <p>금리 : {{ options }}</p>
    <p>상세설명 : {{ product.etc_note }}</p>
    <p>우대사항 : {{ product.spcl_cnd }}</p>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'DepositProductListItem',
  props: {
    product: Object,
    options: Array,
  },
}
</script>

<style>

</style>