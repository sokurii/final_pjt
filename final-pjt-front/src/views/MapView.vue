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
          <!-- <MapSearchInput @search-banks="getSearchDatas"/>     -->
          <!-- MapSearchInput -->
          <div class="banner flex-column justify-content:center align-items:center">
            <form class="m-1" @submit.prevent="searchPlaces">
              <b-form-group label="광역시/도" label-for="province" label-cols-md="auto" class="mb-3">
                <b-form-select id="province" v-model="province" :options="provinces"></b-form-select>
              </b-form-group>
              <b-form-group label="시/군/구" label-for="city" label-cols-md="auto" class="mb-3">
                <b-form-select id="city" v-model="city" :options="cities[province]"></b-form-select>
              </b-form-group>
              <b-form-group label="은행명" label-for="bank" label-cols-md="auto" class="mb-3">
                <b-form-input id="bank" v-model="bank" class="d-inline-block" style="width: 250px; height: 35px;"></b-form-input>
              </b-form-group>
              <button type="submit" class="btn btn-primary">이동</button>
            </form>
          </div>
        </div>
        <div class="col">
          <!-- <KakaoMap :datas="datas"/> -->
          <!-- KakaoMap -->
          <div id="map">
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
              <th style="width: 100px">번호</th>
              <th style="width: 300px">이름</th>
              <th style="width: 300px">주소</th>
              <th style="width: 200px">전화번호</th>
              </thead>
            <!-- </table> -->
          </div>
          <div class="fix_body d-flex justify-content-between">
            <tbody v-if="results">

              <tr v-for="(result, index) in results" :key="index" class="body_content d-flex p-3 mt-1">
                <td style="width: 100px">{{ index + 1}} </td>
                <td style="width: 300px">{{ result.place_name }}</td>
                <td style="width: 300px">{{ result.address_name }}</td>
                <td style="width: 200px">{{ result.phone }}</td>
              </tr>

            </tbody>
   
            <!-- </table> -->
          </div>
          <div id="menu_wrap" class="bg_white" style="display: none;">
            <ul id="placesList"></ul>
            <div id="pagination"></div>
          </div>
        </div>
      </div>
    </div>


  </div>



  
</template>

<script>
// import KakaoMap from '@/components/KakaoMap'
// import MapSearchInput from '@/components/MapSearchInput'

const kakao = window.kakao

export default {
  name: 'MapView',
  // components: {
  //   KakaoMap,
  //   MapSearchInput
  // },
  data() {
    return {
      // SearchInput 관련
      province: '전체',
      city: '전체',
      bank: null,
      provinces: [
        '전체',
        '서울특별시',
        '인천광역시',
        '대전광역시',
        '대구광역시',
        '광주광역시',
        '부산광역시',
        '울산광역시',
        '세종특별자치시',
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
      cities: {
        '전체': ['전체'],
        '서울특별시': ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'],
        '인천광역시': ['강화군', '계양구', '동구', '미추홀구', '부평구', '서구', '연수구', '옹진군', '중구', '남동구'],
        '대전광역시': ['대덕구', '동구', '서구', '유성구', '중구'],
        '대구광역시': ['군위군', '남구', '달서구', '달성군', '동구', '북구', '서구', '수성구', '중구'],
        '광주광역시': ['광산구', '남구', '동구', '북구', '서구'],
        '부산광역시': ['강서구', '금정구', '기장군', '남구', '동구', '동래구', '부산진구', '북구', '사상구', '사하구', '서구', '수영구', '영도구', '중구', '해운대구', '연제구'],
        '울산광역시': ['남구', '동구', '북구', '울주군', '중구'],
        '세종특별자치시': ['세종시'],
        '경기도': ['가평군', '과천시', '광명시', '광주시', '구리시', '군포시', '김포시', '남양주시', '동두천시', '부천시', '성남시', '수원시', '시흥시', '안산시', '안성시', '안양시', '양주시', '양평군', '여주시', '연천군', '오산시', '용인시', '의왕시', '의정부시', '이천시', '파주시', '평택시', '포천시', '화성시'],
        '강원도': ['강릉시', '고성군', '동해시', '삼척시', '양구군', '양양군', '영월군', '원주시', '인제군', '정선군', '철원군', '춘천시', '태백시', '평창군', '화천군', '횡성군', '속초시', '홍천군'],
        '충청북도': ['괴산군', '단양군', '보은군', '영동군', '옥천군', '증평군', '진천군', '청주시', '충주시', '제천시'],
        '충청남도': ['계룡시', '공주시', '금산군', '논산시', '당진시', '보령시', '부여군', '서산시', '서천군', '아산시', '예산군', '천안시', '청양군', '태안군', '홍성군'],
        '경상북도': ['경산시', '경주시', '고령군', '구미시', '군위군', '김천시', '문경시', '봉화군', '상주시', '성주군', '안동시', '영덕군', '영양군', '영주시', '영천시', '예천군', '울릉군', '울진군', '의성군', '청도군', '청송군', '칠곡군', '포항시'],
        '경상남도': ['거제시', '거창군', '고성군', '김해시', '남해군', '밀양시', '사천시', '산청군', '양산시', '의령군', '진주시', '창녕군', '창원시', '통영시', '하동군', '함안군', '함양군', '합천군'],
        '전라북도': ['고창군', '군산시', '김제시', '남원시', '무주군', '부안군', '순창군', '익산시', '임실군', '전주시', '정읍시', '진안군', '장수군', '완주군'],
        '전라남도': ['강진군', '고흥군', '곡성군', '광양시', '구례군', '나주시', '담양군', '무안군', '목포시', '보성군', '순천시', '신안군', '여수시', '영광군', '영암군', '완도군', '장성군', '장흥군', '진도군', '함평군', '해남군', '화순군'],
        '제주특별자치도': ['제주시', '서귀포시'],
      },
      // banks: [
      //   '전체',
      //   '우리은행',
      //   '한국스탠다드차타드은행',
      //   '대구은행',
      //   '부산은행',
      //   '광주은행',
      //   '제주은행',
      //   '전북은행',
      //   '경남은행',
      //   '중소기업은행',
      //   '한국산업은행',
      //   '국민은행',
      //   '신한은행',
      //   '농협은행주식회사',
      //   '하나은행',
      //   '주식회사 케이뱅크',
      //   '수협은행',
      //   '주식회사 카카오뱅크',
      //   '토스뱅크 주식회사',
      // ],

      // 카카오맵 관련
      map: null,
      KAKAO_API_KEY: process.env.VUE_APP_KAKAO_API_KEY,
      markers: [],
      results: [],
    }
  },
  computed: {
    keyword() {
      if (!this.bank){
        this.bank = '은행'
      }

      return this.province + ' ' + this.city + ' ' + this.bank
    }
  },
  mounted() {
    if (kakao && kakao.maps) {
        this.loadMap()
    } else {
        this.loadScript()
    }
  },
  methods: {
  //   getSearchDatas(datas) {
  //     this.datas.province = datas.province
  //     this.datas.city = datas.city
  //     this.datas.bank = datas.bank
  //   }
    // api 불러오기
    loadScript() {
      const script = document.createElement("script");
      script.src =
        `//dapi.kakao.com/v2/maps/sdk.js?appkey=${this.KAKAO_API_KEY}&libraries=services&autoload=false`;
      script.onload = () => window.kakao.maps.load(() => this.loadMap());
      document.head.appendChild(script);
    },
    // 지도 출력
    loadMap() {
      const container = document.getElementById("map")
      const options = {
          center: new window.kakao.maps.LatLng(35.096378878315, 128.85365157034527), // (위도, 경도)
          level: 2
          // 초기 위치는 SSAFY 부울경 캠퍼스
      }
      this.map = new window.kakao.maps.Map(container, options)
      this.loadMarker()
    },
    // 마커 생성
    loadMarker() {
      // SSAFY 부울경 캠퍼스에 마커 생성
      const markerPosition = new window.kakao.maps.LatLng(
          35.096378878315,
          128.85365157034527
      )
      const marker = new window.kakao.maps.Marker({
          position: markerPosition,
      })
      marker.setMap(this.map)
    },
    searchPlaces() {
      const keyword = this.keyword
      if (!keyword) {
        alert("키워드를 입력해주세요!")
        return false
      }
      const ps = new window.kakao.maps.services.Places();
      ps.keywordSearch(keyword, this.placesSearchCB);
    },
    placesSearchCB(data, status, pagination) {
      if (status === window.kakao.maps.services.Status.OK) {
        this.results = data
        this.displayPlaces(data)
        this.displayPagination(pagination)
      } else if (status === window.kakao.maps.services.Status.ZERO_RESULT) {
        alert("검색 결과가 존재하지 않습니다.")
        this.results = []
      } else if (status === window.kakao.maps.services.Status.ERROR) {
        alert("검색 결과 중 오류가 발생했습니다.")
        this.results = []
      }
    },
    displayPlaces(places) {
      const listEl = document.getElementById("placesList");
      const menuEl = document.getElementById("menu_wrap");
      const fragment = document.createDocumentFragment();
      const bounds = new window.kakao.maps.LatLngBounds();
      let listStr = '';
      if (listEl) {
        this.removeAllChildNods(listEl);
        this.removeMarker();
      }
      for (let i = 0; i < places.length; i++) {
        const place = places[i];
        const placePosition = new window.kakao.maps.LatLng(place.y, place.x);
        const marker = this.addMarker(placePosition, i, place.place_name);
        const itemEl = this.getListItem(i, place);
        const infowindow = new window.kakao.maps.InfoWindow({
          zIndex: 1,
        });

        bounds.extend(placePosition);

        (function(marker, title) {
          window.kakao.maps.event.addListener(marker, "mouseover", function() {
            infowindow.setContent('<div style="padding:5px;font-size:12px;">' + title + '</div>');
            infowindow.open(this.map, marker);
          });

          window.kakao.maps.event.addListener(marker, "mouseout", function() {
            infowindow.close();
          });

          itemEl.onmouseover = function() {
            infowindow.setContent('<div style="padding:5px;font-size:12px;">' + title + '</div>');
            infowindow.open(this.map, marker);
          };

          itemEl.onmouseout = function() {
            infowindow.close();
          };
        })(marker, place.place_name);

        fragment.appendChild(itemEl);
      }

      listEl.appendChild(fragment);
      menuEl.scrollTop = 0;

      this.map.setBounds(bounds);
    },
    getListItem(index, place) {
      const el = document.createElement("li");
      let itemStr = '<span class="markerbg marker_' + (index + 1) + '"></span>' +
        '<div class="info">' +
        '   <h5>' + place.place_name + '</h5>';

      if (place.road_address_name) {
        itemStr +=
          '    <span>' + place.road_address_name + '</span>' +
          '   <span class="jibun gray">' + place.address_name + '</span>';
      } else {
        itemStr += '    <span>' + place.address_name + '</span>';
      }

      itemStr += '  <span class="tel">' + place.phone + '</span>' +
        '</div>';

      el.innerHTML = itemStr;
      el.className = "item";

      return el;
    },
    addMarker(position, idx, title) {
      const imageSrc =
        "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/marker_number_blue.png";
      const imageSize = new window.kakao.maps.Size(36, 37);
      const imgOptions = {
        spriteSize: new window.kakao.maps.Size(36, 691),
        spriteOrigin: new window.kakao.maps.Point(0, idx * 46 + 10),
        offset: new window.kakao.maps.Point(13, 37),
      };
      const markerImage = new window.kakao.maps.MarkerImage(
        imageSrc,
        imageSize,
        imgOptions
      );
      const marker = new window.kakao.maps.Marker({
        position: position,
        image: markerImage,
      });

      marker.setMap(this.map);
      this.markers.push(marker);

      return marker;
    },
    removeMarker() {
      for (let i = 0; i < this.markers.length; i++) {
        this.markers[i].setMap(null);
      }
      this.markers = [];
    },
    displayPagination(pagination) {
      if (this.listEl && this.listEl.hasChildNodes()) {
        const paginationEl = document.getElementById("pagination");
        const fragment = document.createDocumentFragment();

        while (paginationEl.hasChildNodes()) {
          paginationEl.removeChild(paginationEl.lastChild);
        }

        for (let i = 1; i <= pagination.last; i++) {
          const el = document.createElement("a");
          el.href = "#";
          el.innerHTML = i;

          if (i === pagination.current) {
            el.className = "on";
          } else {
            el.onclick = (function(i) {
              return function() {
                pagination.gotoPage(i);
              };
            })(i);
          }

          fragment.appendChild(el);
        }
        paginationEl.appendChild(fragment);
      }
    },
    displayInfowindow(marker, title) {
      const content = '<div style="padding:5px;z-index:1;">' + title + "</div>";

      infowindow.setContent(content);
      infowindow.open(this.map, marker);
    },
    removeAllChildNods(el) {
      while (el.hasChildNodes()) {
        el.removeChild(el.lastChild);
      }
    },
  },
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


/* MapSearchInput */

label{
  font-weight: bold;
}

.banner {
  /* width:20% ; */
  height: 100%;
  background-color: #7ab87d; /* 배너 배경색 */
  color: #fff; /* 배너 텍스트 색상 */
  padding: 10px 10px; /* 내부 여백 설정 */
  /* border-radius: 6px; 모서리를 둥글게 */
  border-top-left-radius: 10px;
  border-bottom-left-radius:10px;
  align-items: center;
  
  /* display: flex; */
}

.banner button {
  background-color: #fff; /* 버튼 배경색 */
  color: #7ab87d; /* 버튼 텍스트 색상 */
  padding: 8px 16px; /* 버튼 여백 설정 */
  border-radius: px; /* 모서리를 둥글게 */
  border: none; /* 테두리 제거 */
  font-weight: bold;
  cursor: pointer;
}

.banner button:hover {
  background-color: #e5e5e5; /* 마우스 오버 시 배경색 변경 */
}

/* KakaoMap */
#map {
  margin: 3px;
  display: flex;
  border: solid;
  height: 500px;
}

</style>
