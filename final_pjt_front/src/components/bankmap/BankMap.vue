<template>
  <div>
    <input type="text" v-model="keyword" placeholder="장소를 입력하세요">
    <b-button @click="searchPlaces">검색</b-button>
    <div id="map" style="width: 70%; height: 400px;"></div>
  </div>
</template>

<script>
export default {
  name: 'BankMap',

  data() {
    return {
      map: null,
      infowindow: null,
      keyword: '',
      placesService: null,
    };
  },

  mounted() {
    const script = document.createElement('script');
    script.onload = this.initMap;
    script.src = 'https://dapi.kakao.com/v2/maps/sdk.js?appkey=30b90730d0dd4c1fc7684e0275c21c1c&libraries=services&autoload=false';
    document.head.appendChild(script);
  },

  methods: {
    initMap() {
      const mapContainer = document.getElementById('map');
      const mapOption = {
        center: new window.kakao.maps.LatLng(37.566826, 126.9786567),
        level: 3,
      };

      this.map = new window.kakao.maps.Map(mapContainer, mapOption);
      this.infowindow = new window.kakao.maps.InfoWindow({ zIndex: 1 });
      this.placesService = new window.kakao.maps.services.Places(this.map);
    },

    searchPlaces() {
      this.placesService.keywordSearch(this.keyword, (data, status) => {
        this.placesSearchCB(data, status);
      });
    },

    placesSearchCB(data, status) {
      if (status === window.kakao.maps.services.Status.OK) {
        for (let i = 0; i < data.length; i++) {
          this.displayMarker(data[i]);
        }
      }
    },

    displayMarker(place) {
      const marker = new window.kakao.maps.Marker({
        map: this.map,
        position: new window.kakao.maps.LatLng(place.y, place.x),
      });

      window.kakao.maps.event.addListener(marker, 'click', () => {
        this.infowindow.setContent(
          '<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>'
        );
        this.infowindow.open(this.map, marker);
      });
    },
  },
};
</script>

<style scoped>

</style>
