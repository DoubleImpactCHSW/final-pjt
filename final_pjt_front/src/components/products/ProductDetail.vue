<template>
    <div>
      <div class="m-4 d-flex justify-content-between">
        <div>공식 제출 월</div>
        <div class="content">{{ detailData?.dcls_month }}</div>
      </div>
      <div class="m-4 d-flex justify-content-between">
        <div>금융회사명</div>
        <div class="content">{{ detailData?.kor_co_nm }}</div>
      </div>
      <div class="m-4 d-flex justify-content-between">
        <div>상품명</div>
        <div class="content">{{ detailData?.fin_prdt_nm }}</div>
      </div>
      <div class="m-4 d-flex justify-content-between">
        <div>가입제한</div>
        <div class="content">{{ detailData?.join_deny }}</div>
      </div>
      <div class="m-4 d-flex justify-content-between">
        <div>가입 방법</div>
        <div class="content">{{ detailData?.join_way }}</div>
      </div>
      <div class="m-4 d-flex justify-content-between">
        <div>부가 정보</div>
        <div class="content">{{ detailData?.etc_note }}</div>
      </div>

      <b-button @click="registerProduct" variant="primary">가입하기</b-button>
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
.content {
  width: 200px;
  background-color: chocolate;
}
</style>