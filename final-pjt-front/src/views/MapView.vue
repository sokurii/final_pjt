<template>
  <div class="profile-page">
    <div class="profile-header">
      <h1>우리 동네 은행 찾기</h1>
    </div>
    
    <div class="main-container mt-4">
      <div class="row">
        <div class="col-3">
          <MapSearchInput @search-banks="getSearchDatas"/>    
        </div>
        <div class="col">
          <KakaoMap :datas="datas"/>
        </div>
      </div>
    </div>
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
.profile-header {
  height: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.main-container {
  margin: 50px;
}

.map-container .row {
  margin: 0;
}

.map-container .col-3,
.map-container .col {
  min-height: 400px;
}
</style>
