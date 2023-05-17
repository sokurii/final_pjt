<template>
  <div>
    <div>
      <b-form-group label="광역시/도" label-for="province" label-cols-md="auto" class="mb-3">
        <b-form-select id="province" v-model="province" :options="provinces"></b-form-select>
      </b-form-group>
      <b-form-group label="시/군/구" label-for="city" label-cols-md="auto" class="mb-3">
        <b-form-select id="city" v-model="city" :options="cities"></b-form-select>
      </b-form-group>
      <b-form-group label="은행명" label-for="bank" label-cols-md="auto" class="mb-3">
        <b-form-select id="bank" v-model="bank" :options="banks"></b-form-select>
      </b-form-group>
      <button class="btn btn-primary">이동</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
      return {
        province: '---',
        city: '---',
        bank: '---',
        provinces: [
          '서울특별시',
          '인천광역시',
          '대전광역시',
          '대구광역시',
          '광주광역시',
          '부산광역시',
          '울산광역시',
          '경기도',
          '강원도',
          '충청북도',
          '충청남도',
          '경상북도',
          '경상남도',
          '전라북도',
          '전라남도',
          '제주특별자치도',
        ],
        cities: [
          'transparent',
          'white',
          'light',
          'dark',
          'primary',
          'secondary',
          'success',
          'danger',
          'warning',
          'info',
        ],
        banks: [
          'transparent',
          'white',
          'light',
          'dark',
          'primary',
          'secondary',
          'success',
          'danger',
          'warning',
          'info',
        ],
      }
    }

}
</script>

<style>

</style>