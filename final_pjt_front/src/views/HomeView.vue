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
              <b-card
                overlay
                :img-src="getImagePath('1.jpg')"
                img-alt="Card Image"
                text-variant="white"
                sub-title=""
              >
                <div
                  class="d-flex flex-column justify-content-center align-items-end h-100"
                >
                  <b-card-title class="text-right"
                    ><strong style="font-size: 80px; margin-right: 30px"
                      >국가별 환율을 한눈에</strong
                    ></b-card-title
                  >
                  <b-card-text
                    class="text-right"
                    style="font-size: 40px; margin-right: 30px"
                  >
                    지금 환율이 가장 좋은 곳은? 환율 조회해보자~
                  </b-card-text>
                </div>
              </b-card>
            </div>
          </template>
        </b-carousel-slide>
        <b-carousel-slide img-blank>
          <template #img>
            <div @click="goToProductView">
              <b-card
                overlay
                :img-src="getImagePath('2.jpg')"
                img-alt="Card Image"
                text-variant="white"
                sub-title=""
              >
                <div
                  class="d-flex flex-column justify-content-center align-items-start h-100"
                >
                  <b-card-title
                    class="text-left"
                    style="font-size: 80px; margin-right: 40px"
                    ><strong>예금금리비교</strong></b-card-title
                  >
                  <b-card-text
                    class="text-left"
                    style="font-size: 40px; margin-right: 40px"
                    >전국 1만여개 금융기관을 한번에~</b-card-text
                  >
                </div>
              </b-card>
            </div>
          </template>
        </b-carousel-slide>
        <b-carousel-slide img-blank>
          <template #img>
            <div @click="goToBankMapView">
              <b-card
                overlay
                :img-src="getImagePath('3.jpg')"
                img-alt="Card Image"
                text-variant="white"
                sub-title=""
              >
                <div
                  class="d-flex flex-column justify-content-center align-items-end h-100"
                >
                  <b-card-title class="text-right"
                    ><strong style="font-size: 80px; margin-right: 30px"
                      >은행 찾기</strong
                    ></b-card-title
                  >
                  <b-card-text
                    class="text-right"
                    style="font-size: 40px; margin-right: 30px"
                    >이 근처에 은행이 어디 있을까? 확인하고
                    싶다면?!</b-card-text
                  >
                </div>
              </b-card>
            </div>
          </template>
        </b-carousel-slide>
        <b-carousel-slide img-blank>
          <template #img>
            <div @click="goToRecommendView">
              <b-card
                overlay
                :img-src="getImagePath('4.jpg')"
                img-alt="Card Image"
                text-variant="white"
              >
                <div
                  class="d-flex flex-column justify-content-center align-items-end h-100"
                >
                  <b-card-title class="text-right"
                    ><strong style="font-size: 80px; margin-right: 30px"
                      >내게 맞는 예적금 상품</strong
                    ></b-card-title
                  >
                  <b-card-text
                    class="text-right"
                    style="font-size: 40px; margin-right: 30px"
                    >EZ는 쉽고 정확하게 추천해드립니다.</b-card-text
                  >
                </div>
              </b-card>
            </div>
          </template>
        </b-carousel-slide>
      </b-carousel>
    </div>

    <footer
      bg="primary"
      :text="['white', 'center', 'lg-start']"
      class="fixed-bottom"
    >
      <div
        class="text-center p-3"
        style="background-color: rgba(255, 255, 0, 0.2)"
      >
        © 2023 Copyright: DoubleImpact
        <img
          src="@/assets/background/doubleimpact.jpg"
          alt="img"
          style="max-width: 50px; max-height: 50px"
        />
      </div>
    </footer>
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
      this.$router.push('/exchange');
    },
    goToProductView() {
      this.$router.push('/product');
    },
    goToBankMapView() {
      this.$router.push('/bankmap');
    },
    goToRecommendView() {
      this.$router.push('/recommend');
    },
    getImagePath(img) {
      return require(`@/assets/homeimages/${img}`);
    },
  },
};
</script>

<style></style>
