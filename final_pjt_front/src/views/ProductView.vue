<template>
  <div>
    <h1>상품 조회 View</h1>
    <b-button @click="depositOn">정기예금</b-button> |
    <b-button @click="savingsOn">정기적금</b-button>
    <div class="d-flex">
      <div>
        <div>
          <h5>은행을 선택하세요.</h5>
          <select v-model="bank" name="bank" id="">
            <option value="전체">전체</option>
            <option v-for="bankname in depositBankList" :key="bankname" :value="bankname">{{ bankname }}</option>
          </select>
        </div>
        <div>
          <ProductsTable @onProductSelected="handleSelected" :is-deposit="true" :bank-filter="selectedBank" :product-data="depositData" v-if="showDeposit"/>
          <ProductsTable @onProductSelected="handleSelected" :is-deposit="false" :bank-filter="selectedBank" :product-data="savingsData" v-else/>
        </div>
      </div>
      <div class="m-5">
        <h3>상품 상세 정보</h3>
        <ProductDetail :detail-data="selectedDetailData"/>
      </div>
    </div>
  </div>
</template>

<script>
import ProductsTable from '@/components/products/ProductsTable'
import ProductDetail from '@/components/products/ProductDetail'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'ProductView',

  components: {
    ProductsTable,
    ProductDetail,
  },

  data() {
    return {
      showDeposit: true,
      bank: '',
      depositData: [],
      savingsData: [],
      selectedDetail: null,
    };
  },

  computed: {
    selectedBank() {
      return this.bank
    },
    depositBankList() {
      const li = this.depositData.map((dep) => {
        return dep.kor_co_nm
      })
      return [...new Set(li)];
    },
    savingsBankList() {
      const li = this.savingsData.map((dep) => {
        return dep.kor_co_nm
      })
      return [...new Set(li)];
    },
    selectedDetailData() {
      if (this.showDeposit) {
        return this.depositData.find((dep) => {
          return dep.fin_prdt_cd === this.selectedDetail
          })
      } else {
        return this.savingsData.find((dep) => {
          return dep.fin_prdt_cd === this.selectedDetail
          })
      }
    }
  },

  async beforeMount() {
    try {
      const res1 = await axios.get(`${API_URL}/products/save-deposit-products/`);
      console.log('예금 상품 목록 저장 완료', res1);
    } catch (err) {
      console.log('예금 상품 목록 저장 실패:', err);
    }

    try {
      const res2 = await axios.get(`${API_URL}/products/save-deposit-options/`);
      console.log('예금 옵션 저장 완료', res2);
    } catch (err) {
      console.log('예금 상품 옵션 저장 실패:', err);
    }

    try {
      const res3 = await axios.get(`${API_URL}/products/save-saving-products/`);
      console.log('적금 상품 목록 저장 완료', res3);
    } catch (err) {
      console.log('적금 상품 목록 저장 실패:', err);
    }

    try {
      const res4 = await axios.get(`${API_URL}/products/save-saving-options/`);
      console.log('적금 옵션 저장 완료', res4);
    } catch (err) {
      console.log('적금 상품 옵션 저장 실패:', err);
    }

    try {
      const res5 = await axios.get(`${API_URL}/products/deposit-products/`);
      this.depositData = res5.data
      console.log('예금 목록 호출 성공', res5);
    } catch (err) {
      console.log('예금 목록 호출 실패:', err);
    }

    try {
      const res6 = await axios.get(`${API_URL}/products/saving-products/`);
      this.savingsData = res6.data
      console.log('적금 목록 호출 완료', res6);
    } catch (err) {
      console.log('적금 목록 호출 실패:', err);
    }
  },

  methods: {
    depositOn() {
      this.showDeposit = true
    },
    savingsOn() {
      this.showDeposit = false
    },
    handleSelected(payload) {
      this.selectedDetail = payload
    } 
  },
};
</script>

<style scoped></style>
