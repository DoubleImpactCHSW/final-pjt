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
      depositData: this.$store.state.depositProductsData,
      savingsData: this.$store.state.savingsProductsData,
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
