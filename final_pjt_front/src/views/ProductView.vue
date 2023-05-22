<template>
  <div>
    <h1>상품 조회 View</h1>
    <span @click="depositOn">정기예금</span> |
    <span @click="savingsOn">정기적금</span>
    <div class="d-flex justify-content-around">
      <div>
        <h5>은행을 선택하세요.</h5>
        <select v-model="bank" name="bank" id="">
          <option value="우리은행">우리은행</option>
          <option value="한국스탠다드차타드은행">한국스탠다드차타드은행</option>
          <option value="대구은행">대구은행</option>
          <option value="부산은행">부산은행</option>
          <option value="광주은행">광주은행</option>
          <option value="제주은행">제주은행</option>
          <option value="전북은행">전북은행</option>
          <option value="경남은행">경남은행</option>
          <option value="중소기업은행">중소기업은행</option>
          <option value="한국산업은행">한국산업은행</option>
          <option value="국민은행">국민은행</option>
          <option value="신한은행">신한은행</option>
          <option value="농협은행주식회사">농협은행주식회사</option>
          <option value="하나은행">하나은행</option>
          <option value="주식회사 케이뱅크">주식회사 케이뱅크</option>
          <option value="수협은행">수협은행</option>
          <option value="주식회사 카카오뱅크">주식회사 카카오뱅크</option>
          <option value="토스뱅크 주식회사">토스뱅크 주식회사</option>
        </select>
      </div>
      <div>
        <ProductsTable v-if="showDeposit"/>
        <ProductsTable v-else/>
      </div>
    </div>
  </div>
</template>

<script>
import ProductsTable from '@/components/products/ProductsTable'
export default {
  name: 'ProductView',

  components: {
    ProductsTable,
  },

  data() {
    return {
      showDeposit: true,
    };
  },

  mounted() {},

  methods: {
    depositOn() {
      this.showDeposit = true
    },
    savingsOn() {
      this.showDeposit = false
    } 
  },
};
</script>

<style scoped></style>
