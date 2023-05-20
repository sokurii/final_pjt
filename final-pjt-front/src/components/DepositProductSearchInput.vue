<template>
  <div>
    <form class="m-1" @submit.prevent="searchProducts">
      <b-form-group label="은행명" label-for="bank" label-cols-md="auto" class="mb-3">
        <b-form-select id="bank" v-model="bank" :options="banks"></b-form-select>
      </b-form-group>
      <button type="submit" class="btn btn-primary">조회</button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'SavingProductSearchInput',
  data() {
    return {
      bank: '전체',
      banks: [
          '전체',
          '우리은행',
          '한국스탠다드차타드은행',
          '대구은행',
          '부산은행',
          '광주은행',
          '제주은행',
          '전북은행',
          '경남은행',
          '중소기업은행',
          '한국산업은행',
          '국민은행',
          '신한은행',
          '농협은행주식회사',
          '하나은행',
          '주식회사 케이뱅크',
          '수협은행',
          '주식회사 카카오뱅크',
          '토스뱅크 주식회사',
        ],
    }
  },
  methods: {
    searchProducts() {
      this.$emit('search-bank', this.bank)
    }
  }
}
</script>

<style>

</style>