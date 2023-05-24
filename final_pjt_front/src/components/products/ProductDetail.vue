<template>
    <div class="top-container">
      <div>
        <h3>상품 상세 정보</h3>
        <div class="ele m-4 d-flex justify-content-between">
          <div class="font-weight-bold">공식 제출 월</div>
          <div class="content">{{ detailData?.dcls_month }}</div>
        </div>
        <div class="ele m-4 d-flex justify-content-between">
          <div class="font-weight-bold">금융회사명</div>
          <div class="content">{{ detailData?.kor_co_nm }}</div>
        </div>
        <div class="ele m-4 d-flex justify-content-between">
          <div class="font-weight-bold">상품명</div>
          <div class="content">{{ detailData?.fin_prdt_nm }}</div>
        </div>
        <div class="ele m-4 d-flex justify-content-between">
          <div class="font-weight-bold">가입제한</div>
          <div class="content">{{ detailData?.join_deny }}</div>
        </div>
        <div class="ele m-4 d-flex justify-content-between">
          <div class="font-weight-bold">가입 방법</div>
          <div class="content">{{ detailData?.join_way }}</div>
        </div>
        <div class="ele m-4 d-flex justify-content-between">
          <div class="font-weight-bold">부가 정보</div>
          <div class="content">{{ detailData?.etc_note }}</div>
        </div>
      </div>
      <div class="mt-auto">
        <b-button @click="registerProduct" variant="primary">가입하기</b-button>
      </div>
    </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'ProductDetail',
  props: {
    detailData: Object,
  },
  data() {
    return {};
  },
  mounted() {},
  methods: {
    registerProduct() {
      axios
        .post(
          `${API_URL}/products/add/${this.$store.state.username}/${this.detailData.fin_prdt_cd}/`,
          null,
          {
            headers: {
              Authorization: `Token ${this.$store.state.token}`,
            },
          }
        )
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>


<style scoped>
.top-container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-color: mintcream;
  padding: 30px 50px;
  width: 532px;
  height: 650px;
  border-radius: 30px;
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.3);
}

.content {
  width: 250px;
}

.ele {
  width: 400px;
}

</style>