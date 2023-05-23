<template>
    <div>
      <div>
        <span>공식 제출 월</span>
        <span>{{ detailData?.dcls_month }}</span>
      </div>
      <div>
        <span>금융회사명</span>
        <span>{{ detailData?.kor_co_nm }}</span>
      </div>
      <div>
        <span>상품명</span>
        <span>{{ detailData?.fin_prdt_nm }}</span>
      </div>
      <div>
        <span>가입제한</span>
        <span>{{ detailData?.join_deny }}</span>
      </div>
      <div>
        <span>가입 방법</span>
        <span>{{ detailData?.join_way }}</span>
      </div>
      <div>
        <span>부가 정보</span>
        <span>{{ detailData?.etc_note }}</span>
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

</style>