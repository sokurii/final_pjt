<template>
  <div>
    <h1>은행 위치 조회</h1>
    <MapSearchInput @search-banks="getSearchDatas"/>
    <KakaoMap :datas="datas"/>
  </div>
</template>

<script>
import KakaoMap from '@/components/KakaoMap'
import MapSearchInput from '@/components/MapSearchInput'

export default {
  name: 'MapView',
  components: {
    KakaoMap,
    MapSearchInput
  },
  data() {
    return {
      datas: {
        province: null,
        city: null,
        bank: null,
      }
    }
  },
  methods: {
    getSearchDatas(datas) {
      this.datas.province = datas.province
      this.datas.city = datas.city
      this.datas.bank = datas.bank
    }
  }
}
</script>

<style>

</style>
