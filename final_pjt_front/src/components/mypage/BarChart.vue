<template>
  <Bar
    id="my-chart-id"
    :options="chartOptions"
    :data="chartData"
  />
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
  props: {
    finProducts: Array,
  },
  data() {
    return {
      chartData: {
        labels: this.finProducts.map((x) => x.productName),
        datasets: [
            {
            label: "저축 금리",
            backgroundColor: '#ff7f00',
            data: [...this.finProducts.map((x) => x.rate), 5.0]
            },
            {
            label: "최고 우대 금리",
            backgroundColor: '#007bff',
            data: [...this.finProducts.map((x) => x.primeRate), 5.0]
            },
          ]
      },
      chartOptions: {
        responsive: true
      }
    }
  },

}
</script>

<style scoped>
.chart-container {
  width: 400px;
  height: 400px;
}
</style>
