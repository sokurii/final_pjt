<template>
  <div>
    <div id="map">
      
    </div>
  </div>
</template>

<script>
export default {
  name: 'KakaoMap',
  data() {
    return {
        map: null,
        KAKAO_API_KEY: process.env.VUE_APP_KAKAO_API_KEY
    }
  },
  mounted() {
    if (window.kakao && window.kakao.maps) {
        this.loadMap()
    } else {
        this.loadScript()
    }
  },
  methods: {
    // api 불러오기
    loadScript() {
        const script = document.createElement("script")
        script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${this.KAKAO_API_KEY}&autoload=false`
        script.onload = () => window.kakao.maps.load(this.loadMap)

        document.head.appendChild(script)
    },
    // 지도 출력
    loadMap () {
        const container = document.getElementById("map")
        const options = {
            center: new window.kakao.maps.LatLng(35.096378878315, 128.85365157034527), // (위도, 경도)
            level: 2
        }

        this.map = new window.kakao.maps.Map(container, options)
        this.loadMarker()
    },
    loadMarker() {
        const markerPosition = new window.kakao.maps.LatLng(
            35.096378878315,
            128.85365157034527
        )
        const marker = new window.kakao.maps.Marker({
            position: markerPosition,
        })
        marker.setMap(this.map)
    }
  }
}
</script>

<style scoped>
#map {
  margin: 3px;
  display: flex;
  border: solid;
  height: 500px;
}
</style>