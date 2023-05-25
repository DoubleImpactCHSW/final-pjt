<template>
  <div class="d-flex flex-column align-items-center">
    <BasicRecommendation :rec-list="recPrdsList" v-if="isOnRecommend"/>
    <UserInfo @go-recommend="handleRecommend" v-else/>
  </div>
</template>

<script>
import UserInfo from '@/components/mypage/UserInfo'
import BasicRecommendation from '@/components/mypage/BasicRecommendation'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'MypageView',

  components: {
    UserInfo,
    BasicRecommendation,
  },

  data() {
    return {
      onRecommend: false,
      recPrds: null,
    };
  },

  computed: {
    isOnRecommend() {
      return this.onRecommend
    },
    recPrdsList() {
      return this.recPrds
    }
  },

  mounted() {
    
  },

  methods: {
    handleRecommend() {
      this.onRecommend = true
      axios
        .get(`${API_URL}/recommendation/`, {
            headers: {
                Authorization: `Token ${this.$store.state.token}`,
            },
        })
        .then((res) => {
            console.log(res)
            const resList = res.data.recommend_prd

            const extract = resList.map((cd) => {
                const searchDeposit = this.$store.state.depositProductsData.find((x) => {
                    return x.fin_prdt_cd === cd
                })
                const searchSavings = this.$store.state.savingsProductsData.find((x) => {
                    return x.fin_prdt_cd === cd
                })

                const info = searchDeposit ? {
                    id: searchDeposit.fin_prdt_cd,
                    bankName: searchDeposit.kor_co_nm,
                    productName: searchDeposit.fin_prdt_nm,
                    } : {
                    id: searchSavings.fin_prdt_cd,
                    bankName: searchSavings.kor_co_nm,
                    productName: searchSavings.fin_prdt_nm,
                    }

                return info
            })
            this.recPrds = extract
        })
        .catch((err) => {
            console.log(err)
        })
    }
  },
};
</script>

<style scoped>

</style>
