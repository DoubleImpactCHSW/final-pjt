<template>
  <div class="container">
    <h2>은행 찾기</h2>
    <input type="text" v-model="searchQuery" placeholder="장소 검색" />
    <button @click="searchPlaces">검색</button>
    <div id="map"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      searchQuery: '',
      map: null,
      infowindow: null,
      ps: null,
      markers: [], // 마커를 관리하기 위한 배열 추가
    };
  },

  computed: {
    bankSearchQuery() {
      return this.searchQuery + ' ' + '은행';
    },
  },

  mounted() {
    // 지도를 생성합니다
    const mapContainer = document.getElementById('map');
    const mapOption = {
      center: new window.kakao.maps.LatLng(37.566826, 126.9786567),
      level: 3,
    };
    this.map = new window.kakao.maps.Map(mapContainer, mapOption);

    // 인포윈도우를 생성합니다
    this.infowindow = new window.kakao.maps.InfoWindow({ zIndex: 1 });

    // 장소 검색 객체를 생성합니다
    this.ps = new window.kakao.maps.services.Places(this.map);
  },
  methods: {
    searchPlaces() {
      // 이전에 표시된 마커들을 제거합니다
      this.clearMarkers();

      // 키워드로 장소를 검색합니다
      this.ps.keywordSearch(this.bankSearchQuery, this.placesSearchCB);
    },
    placesSearchCB(data, status) {
      if (status === window.kakao.maps.services.Status.OK) {
        for (let i = 0; i < data.length; i++) {
          this.displayMarker(data[i]);
        }
        // 검색된 위치로 지도 이동
        const bounds = new window.kakao.maps.LatLngBounds();
        for (let i = 0; i < data.length; i++) {
          bounds.extend(new window.kakao.maps.LatLng(data[i].y, data[i].x));
        }
        this.map.setBounds(bounds);
      }
    },
    displayMarker(place) {
      // 마커를 생성하고 지도에 표시합니다
      const marker = new window.kakao.maps.Marker({
        map: this.map,
        position: new window.kakao.maps.LatLng(place.y, place.x),
      });

      // 마커에 클릭 이벤트를 등록합니다
      window.kakao.maps.event.addListener(marker, 'click', () => {
        // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
        this.infowindow.setContent(
          '<div style="padding:5px;font-size:12px;">' +
            place.place_name +
            '</div>'
        );
        this.infowindow.open(this.map, marker);
      });

      // 마커를 배열에 추가합니다
      this.markers.push(marker);
    },
    clearMarkers() {
      this.infowindow.close();

      // 배열에 있는 모든 마커를 제거하고 배열도 초기화합니다
      for (let i = 0; i < this.markers.length; i++) {
        this.markers[i].setMap(null);
      }
      this.markers = [];
    },
  },
};
</script>

<style scoped>
.container {
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 30px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
  margin-bottom: 25px;
}

input {
  border: none;
  border-radius: 4px;
  padding: 10px;
  margin-right: 20px;
  margin-left: 20px;
  font-size: 16px;
  margin-bottom: 50px;
}

button {
  border: none;
  border-radius: 4px;
  padding-top: 10px;
  padding-bottom: 10px;
  padding-right: 30px;
  padding-left: 30px;
  margin-right: 20px;
  margin-left: 20px;
  font-size: 16px;
  margin-bottom: 50px;
}

#map {
  width: 100%;
  height: 500px;
  border: 1px solid #ccc;
  border-radius: 8px;
  margin: 0 auto;
}
</style>
