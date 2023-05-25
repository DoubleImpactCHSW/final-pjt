<template>
  <div class="home">

    <div>
    <b-carousel
      id="carousel-no-animation"
      style="text-shadow: 0px 0px 2px #000"
      no-animation
      indicators
      img-width="1024"
      img-height="480"
    >
    <b-carousel-slide img-blank>
      <template #img>
        <div @click="goToExchangeView">
          <b-card overlay img-src="https://picsum.photos/900/250/?image=3" img-alt="Card Image" text-variant="white" sub-title="">
            <div class="d-flex flex-column justify-content-center align-items-start h-100">
              <b-card-title class="text-left"><strong>국가별 환율을 한눈에</strong></b-card-title>
              <b-card-text class="text-left">
                지금 환율이 가장 좋은 곳은?
                환율 조회해보자~
              </b-card-text>
            </div>
          </b-card>
        </div>
      </template>
    </b-carousel-slide>
    <b-carousel-slide img-blank>
      <template #img>
        <div @click="goToProductView">
          <b-card overlay img-src="https://picsum.photos/900/250/?image=3" img-alt="Card Image" text-variant="white" >
          <div class="text-right">
              <b-card-title class="text-right "><strong>예금금리비교</strong></b-card-title>
              <b-card-sub-title class="text-right">은행/저축은행은 물론! 3000여 모든 새마을금고, 신협까지!</b-card-sub-title>
              <b-card-text class="text-right">전국 1만여개 금융기관을 한번에~</b-card-text>
        </div>
          </b-card>
        </div>
      </template>
    </b-carousel-slide>
    <b-carousel-slide img-blank>
      <template #img>
        <div @click="goToBankMapView">
          <b-card overlay img-src="https://picsum.photos/900/250/?image=3" img-alt="Card Image" text-variant="white" >
          <div class="text-right">
              <b-card-title class="text-right "><strong>은행 찾기</strong></b-card-title>
              <b-card-text class="text-right">이 근처에 은행이 어디 있을까? 확인하고 싶다면?!</b-card-text>
          </div>
          </b-card>
        </div>
      </template>
    </b-carousel-slide>
    <b-carousel-slide img-blank>
      <template #img>
        <div @click="goToRecommendView">
          <b-card overlay img-src="https://picsum.photos/900/250/?image=3" img-alt="Card Image" text-variant="white" >
          <div class = "d-flex flex-column justify-content-center align-items-start h-100">
              <b-card-title class="text-left"><strong>내게 맞는 예적금 상품</strong></b-card-title>
              <b-card-text class="text-left">...은 쉽고 정확하게 비교합니다.</b-card-text>
          </div>
          </b-card>
        </div>
      </template>
    </b-carousel-slide>


    
  </b-carousel>
</div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'HomeView',
  components: {},
  created() {
    if (!this.$store.getters.isLogin) {
      alert('로그인 해주세요!');
      this.$router.push({ name: 'login' });
    }
  },
  methods: {
  goToExchangeView() {
    this.$router.push('/exchange')
  },
  goToProductView() {
    this.$router.push('/product')
  },
  goToBankMapView() {
    this.$router.push('/bankmap')
  },
  goToRecommendView() {
    this.$router.push('/recommend')
  },
  }
}
</script>
