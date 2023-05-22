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
          <tr v-for="item in items" :key="item.id">
            <td>{{ item.column1 }}</td>
            <td>{{ item.column2 }}</td>
            <td>{{ item.column3 }}</td>
						<td></td>
						<td></td>
						<td></td>
						<td></td>
            <!-- ... -->
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProductsTable',
  data() {
    return {
      items: [
        { id: 1, column1: 'Value 1', column2: 'Value 2', column3: 'Value 3' },
        { id: 2, column1: 'Value 4', column2: 'Value 5', column3: 'Value 6' },
				{ id: 3, column1: 'Value 1', column2: 'Value 2', column3: 'Value 3' },
        { id: 4, column1: 'Value 4', column2: 'Value 5', column3: 'Value 6' },
				{ id: 5, column1: 'Value 1', column2: 'Value 2', column3: 'Value 3' },
        { id: 6, column1: 'Value 4', column2: 'Value 5', column3: 'Value 6' },
				{ id: 7, column1: 'Value 1', column2: 'Value 2', column3: 'Value 3' },
        { id: 8, column1: 'Value 4', column2: 'Value 5', column3: 'Value 6' },
				{ id: 9, column1: 'Value 1', column2: 'Value 2', column3: 'Value 3' },
        { id: 10, column1: 'Value 4', column2: 'Value 5', column3: 'Value 6' },
				{ id: 11, column1: 'Value 1', column2: 'Value 2', column3: 'Value 3' },
        { id: 12, column1: 'Value 4', column2: 'Value 5', column3: 'Value 6' },
				{ id: 13, column1: 'Value 1', column2: 'Value 2', column3: 'Value 3' },
        { id: 14, column1: 'Value 4', column2: 'Value 5', column3: 'Value 6' },
				{ id: 15, column1: 'Value 1', column2: 'Value 2', column3: 'Value 3' },
        { id: 16, column1: 'Value 4', column2: 'Value 5', column3: 'Value 6' },
        // ...
      ],
    };
  },
};
</script>

<style scoped>
.table-container {
	width: 1000px;
  height: 500px; /* 스크롤 박스의 높이 조정 */
}

.scroll-box {
  overflow-y: auto; /* 수직 스크롤 활성화 */
	height: 100%;
}

table {
  width: 1400px;
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
