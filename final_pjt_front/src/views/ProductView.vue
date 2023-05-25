<template>
  <div class="top-box">
    <div class="body d-flex justify-content-center">
      <div
        class="left-section d-flex flex-column justify-content-center align-items-center"
      >
        <div class="header">
          <div class="header-box my-3">
            <span></span>
            <span class="bank-choice">상품 발행사를 선택하세요.</span>
            <select v-model="bank" name="bank">
              <option value="전체">전체</option>
              <option
                v-for="bankname in depositBankList"
                :key="bankname"
                :value="bankname"
              >
                {{ bankname }}
              </option>
            </select>
          </div>
          <div class="my-3">
            <b-button
              @click="depositOn"
              variant="warning"
              class="btn-custom-deposit"
              >정기예금</b-button
            >
            <b-button
              @click="savingsOn"
              variant="warning"
              class="btn-custom-savings"
              >정기적금</b-button
            >
          </div>
        </div>
        <div class="my-3">
          <ProductsTable
            @onProductSelected="handleSelected"
            :is-deposit="true"
            :bank-filter="selectedBank"
            :product-data="depositData"
            v-if="showDeposit"
          />
          <ProductsTable
            @onProductSelected="handleSelected"
            :is-deposit="false"
            :bank-filter="selectedBank"
            :product-data="savingsData"
            v-else
          />
        </div>
      </div>
      <div
        class="right-section d-flex flex-column justify-content-center align-items-center"
      >
        <ProductDetail :detail-data="selectedDetailData" />
      </div>
    </div>
  </div>
</template>

<script>
import ProductsTable from '@/components/products/ProductsTable';
import ProductDetail from '@/components/products/ProductDetail';

export default {
  name: 'ProductView',

  components: {
    ProductsTable,
    ProductDetail,
  },

  data() {
    return {
      showDeposit: true,
      bank: '전체',
      depositData: this.$store.state.depositProductsData,
      savingsData: this.$store.state.savingsProductsData,
      selectedDetail: null,
    };
  },

  computed: {
    selectedBank() {
      return this.bank;
    },
    depositBankList() {
      const li = this.depositData.map((dep) => {
        return dep.kor_co_nm;
      });
      return [...new Set(li)];
    },
    savingsBankList() {
      const li = this.savingsData.map((dep) => {
        return dep.kor_co_nm;
      });
      return [...new Set(li)];
    },
    selectedDetailData() {
      if (this.showDeposit) {
        return this.depositData.find((dep) => {
          return dep.fin_prdt_cd === this.selectedDetail;
        });
      } else {
        return this.savingsData.find((dep) => {
          return dep.fin_prdt_cd === this.selectedDetail;
        });
      }
    },
  },

  methods: {
    depositOn() {
      this.showDeposit = true;
    },
    savingsOn() {
      this.showDeposit = false;
    },
    handleSelected(payload) {
      this.selectedDetail = payload;
    },
  },
};
</script>

<style scoped>
.top-box {
  padding-top: 80px;
  height: 93vh;
  background: linear-gradient(to bottom, #fff, #fffacd);
}

.left-section {
  margin-right: 70px;
}

.right-section {
  margin-left: 70px;
}

.header {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100px;
  background-color: #aed581;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
  border-radius: 10px;
}

.header-box {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 575px;
  margin-left: 10px;
  padding: 10px;
  border-radius: 5px;
  background-color: #fff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  animation: header-animation 0.3s;
}

@keyframes header-animation {
  0% {
    opacity: 0;
    transform: translateY(-10px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

.btn-custom-deposit {
  margin-left: 20px;
  font-size: 28px;
  background-color: #8d6e63;
  color: #fff;
  border: none;
}

.btn-custom-savings {
  margin: 0 20px;
  font-size: 28px;
  background-color: #8d6e63;
  color: #fff;
  border: none;
}

.btn-custom:hover {
  background-color: #0056b3;
}

.btn-custom:focus {
  box-shadow: none;
  outline: none;
}

.bank-choice {
  font-size: 28px;
  font-weight: 600;
}
</style>
