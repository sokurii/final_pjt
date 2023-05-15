<template>
  <div>
    <h1>은행 위치 조회</h1>
    <MapSearchInput />
    <KakaoMap />
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
  }
}
</script>

<style>

</style>
