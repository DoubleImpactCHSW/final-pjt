<template>
  <div class="table-container">
    <div class="scroll-box">
      <table>
        <thead>
          <tr>
            <th>공시 제출 월</th>
            <th>금융 회사 명</th>
            <th>상품 명</th>
            <th>6개월</th>
            <th>12개월</th>
            <th>24개월</th>
            <th>36개월</th>
            <!-- ... -->
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in filteredData" :key="product.id">
            <td>{{ product?.dcls_month }}</td>
            <td>{{ product?.kor_co_nm }}</td>
            <td>
              <b-button @click="viewDetail(product.fin_prdt_cd)" variant='info'>{{ product?.fin_prdt_nm }}</b-button>
            </td>
						<td>{{ isDeposit ? product?.depositoptions_set[0]?.intr_rate : product?.savingoptions_set[0]?.intr_rate }}</td>
						<td>{{ isDeposit ? product?.depositoptions_set[1]?.intr_rate : product?.savingoptions_set[1]?.intr_rate }}</td>
						<td>{{ isDeposit ? product?.depositoptions_set[2]?.intr_rate : product?.savingoptions_set[2]?.intr_rate }}</td>
						<td>{{ isDeposit ? product?.depositoptions_set[3]?.intr_rate : product?.savingoptions_set[3]?.intr_rate }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProductsTable',

  props: {
    isDeposit: Boolean,
    productData: Array,
    bankFilter: String,
  },

  computed: {
    filteredData() {
      if (this.bankFilter.length < 3) {
        return this.productData
      } else {
        return this.productData.filter((prod) => {
          return prod.kor_co_nm === this.bankFilter
        })
      }

    }
  },

  methods: {
    viewDetail(fin_prdt_cd) {
      this.$emit('onProductSelected', fin_prdt_cd);
    }
  }
};
</script>

<style scoped>
.table-container {
	width: 800px;
  height: 500px; /* 스크롤 박스의 높이 조정 */
}

.scroll-box {
  overflow-y: auto; /* 수직 스크롤 활성화 */
	height: 100%;
}

table {
  width: 1200px;
	height: 500px;
  border-collapse: collapse;
}

th, td {
  padding: 8px;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f2f2f2;
}

tr:nth-child(even) {
  background-color: #f9f9f9;
}
</style>
