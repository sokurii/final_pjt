<template>
  <div class="profile-page">
    <!-- <h1>은행 위치 조회</h1>
    <MapSearchInput @search-banks="getSearchDatas"/>
    <KakaoMap :datas="datas"/> -->
<!-- ------------------------------------------------- -->
    <div class="profile-header d-flex align-items-center justify-content-center" data-parallax="true" >
      <h1>우리 동네 은행 찾기</h1>
    </div>
    
    <div class="main main-container mt-4">
      <div class="map-container row">
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
.profile-page .profile-header {   
    height: 100px;
    background-size:cover;
    background-position: center;
    margin: 0;
    padding: 0;
    border: 0;
    display: flex;
    align-items: center;

}

/* .main {
  
  } */

.main-container {
  margin: 50px 50px 0;
  border-radius: 6px;
  box-shadow: 0 16px 24px 2px rgba(0,0,0,.14), 0 6px 30px 5px rgba(0,0,0,.12), 0 8px 10px -5px rgba(0,0,0,.2);
  background: #FFF;
  position: relative;
  z-index: 3;
}

</style>
