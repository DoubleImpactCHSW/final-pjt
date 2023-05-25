<template>
    <div class="top-container d-flex justify-content-around">
        <div class="left-section">
            <div class="info-section">
                <h3 class="go-center mb-4">내 정보</h3>
                <div class="oneline d-flex justify-content-between m-3">
                    <span class="key mr-5">회원번호</span>
                    <span>{{ userId }}</span>
                </div>
                <div class="oneline d-flex justify-content-between m-3">
                    <span class="key mr-5">ID</span>
                    <span>{{ username }}</span>
                </div>
                <div class="oneline d-flex justify-content-between m-3">
                    <span class="key mr-5">닉네임</span>
                    <input v-model="nickname" type="text">
                </div>
                <div class="oneline d-flex justify-content-between m-3">
                    <span class="key mr-5">Email</span>
                    <input v-model="email" type="text">
                </div>
                <div class="oneline d-flex justify-content-between m-3">
                    <span class="key mr-5">나이</span>
                    <input v-model="age" type="number">
                </div>
                <div class="oneline d-flex justify-content-between m-3">
                    <span class="key mr-5">총 자산</span>
                    <input v-model="asset" type="number">
                </div>
                <div class="oneline d-flex justify-content-between m-3">
                    <span class="key mr-5">월 평균 수익</span>
                    <input v-model="salary" type="number">
                </div>
                <div class="oneline d-flex justify-content-between m-1">
                    <span></span>
                    <span>( 단위: 원 ₩ )</span>
                </div>
            </div>
            <b-button class="go-center edit-btn" @click="editProfile" variant="info">수정하기</b-button>
        </div>

        <div class="right-section">
            <div class="inside-rs d-flex flex-column justify-content-between" v-if="finProducts.length !== 0">
                <div>
                    <h3 class="mb-4">가입한 상품 목록</h3>
                    <div v-for="product in finProducts" :key="product.productName">
                        <p><i>{{ product.bankName }} - {{ product.productName }}</i></p>
                    </div>
                </div>
                <BarChart :fin-products="finProducts" />
            </div>
            <div v-else>
                <strong>Loading...</strong>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import BarChart from '@/components/mypage/BarChart'
const API_URL = 'http://127.0.0.1:8000'

export default {
    name: 'UserInfo',

    components: {
        BarChart,
    },

    data() {
        return {
            userId: '',
            username: '',
            nickname: '',
            email: '',
            age: '',
            asset: '',
            salary: '',
            finProducts: [],

        };
    },

    mounted() {
        axios.get(`${API_URL}/accounts/profile/${this.$store.state.username}/`)
        .then((res) => {
            this.userId = res.data.id
            this.username = res.data.username
            this.nickname = res.data.nickname
            this.email = res.data.email
            this.age = res.data.age
            this.asset = res.data.money
            this.salary = res.data.salary
            const productsString = res.data.financial_products
            const listedProducts = productsString.split(',')
            const registeredProducts = listedProducts.map((cd) => {
                const searchDeposit = this.$store.state.depositProductsData.find((x) => {
                    return x.fin_prdt_cd === cd
                })
                const searchSavings = this.$store.state.savingsProductsData.find((x) => {
                    return x.fin_prdt_cd === cd
                })

                const info = searchDeposit ? {
                    bankName: searchDeposit.kor_co_nm,
                    productName: searchDeposit.fin_prdt_nm,
                    rate: searchDeposit.depositoptions_set[0].intr_rate,
                    primeRate: searchDeposit.depositoptions_set[0].intr_rate2,
                    } : {
                    bankName: searchSavings.kor_co_nm,
                    productName: searchSavings.fin_prdt_nm,
                    rate: searchSavings.savingoptions_set[0].intr_rate,
                    primeRate: searchSavings.savingoptions_set[0].intr_rate2,
                    }

                return info
            })
            this.finProducts = registeredProducts
        })
        .catch((err) => {
            console.log(err)
        })
    },

    methods: {
        editProfile() {
            const formData = new FormData();
            formData.append('id', this.userId);
            formData.append('username', this.username);
            formData.append('nickname', this.nickname);
            formData.append('email', this.email);
            formData.append('age', this.age);
            formData.append('money', this.asset);
            formData.append('salary', this.salary);
            formData.append('financial_products', this.finProducts);

      axios
        .put(`${API_URL}/accounts/profile/update/${this.$store.state.username}/`, formData, {
          headers: {
            // Authorization: `Token ${this.$store.state.token}`,
            'Content-Type': 'multipart/form-data',
          },
        })
        .then((res) => {
          console.log(res);
          alert('프로필 정보가 수정되었습니다.')
        })
        .catch((err) => {
          console.log(err);
        });
        }
    },
};
</script>

<style scoped>
.top-container {
 width: 100%;
 padding: 50px 200px;
}

.left-section {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    /* text-align: center; */
    background-color: mintcream;
    padding: 30px 50px;
    width: 532px;
    height: 700px;
    border-radius: 30px;
    box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.3);
}

.right-section {
    text-align: center;
    background-color: mintcream;
    padding: 50px;
    width: 532px;
    height: 700px;
    border-radius: 30px;
    box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.3);
}

.inside-rs {
    height: 600px;
}

.info-section {
    margin: 20px 0;
}


.key {
    font-size: 20px;
    font-weight: bold;
}
.oneline {
    height: 35px;
    width: 400px;
}

.go-center {
    margin: 0 auto;
}

.edit-btn {
    margin-bottom: 30px;
}
</style>