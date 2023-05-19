<template>
  <div>
    <label for="country">국가 선택:</label>
    <select
      id="country"
      v-model="selectedCountry"
      @change="calculateExchangeRate"
    >
      <option
        v-for="country in rateInfo"
        :key="country.cur_unit"
        :value="country.cur_nm"
      >
        {{ country.cur_nm }}
      </option>
    </select>

    <br />

    <label for="foreign">{{ selectedCountry }}</label>
    <input
      id="foreign"
      type="number"
      v-model="foreignValue"
      @input="calculateExchangeRate"
    />

    <br />

    <label for="korea">원화 가치</label>
    <input
      id="korea"
      type="number"
      v-model="wonValue"
      @input="calculateExchangeRateReverse"
    />
  </div>
</template>

<script>
// import axios from 'axios'

// const API_URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
// const API_KEY = 'PoeFtZSihXOPw74jOsxSmWMJxQw6G9Ea'

export default {
  name: 'RateCalculator',

  data() {
    return {
      rateInfo: [
        {
          result: 1,
          cur_unit: 'AED',
          ttb: '361.1',
          tts: '368.39',
          deal_bas_r: '364.75',
          bkpr: '364',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '364',
          kftc_deal_bas_r: '364.75',
          cur_nm: '아랍에미리트 디르함',
        },
        {
          result: 1,
          cur_unit: 'AUD',
          ttb: '882.99',
          tts: '900.82',
          deal_bas_r: '891.91',
          bkpr: '891',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '891',
          kftc_deal_bas_r: '891.91',
          cur_nm: '호주 달러',
        },
        {
          result: 1,
          cur_unit: 'BHD',
          ttb: '3,516.97',
          tts: '3,588.02',
          deal_bas_r: '3,552.5',
          bkpr: '3,552',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '3,552',
          kftc_deal_bas_r: '3,552.5',
          cur_nm: '바레인 디나르',
        },
        {
          result: 1,
          cur_unit: 'BND',
          ttb: '987.86',
          tts: '1,007.81',
          deal_bas_r: '997.84',
          bkpr: '997',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '997',
          kftc_deal_bas_r: '997.84',
          cur_nm: '브루나이 달러',
        },
        {
          result: 1,
          cur_unit: 'CAD',
          ttb: '985.04',
          tts: '1,004.93',
          deal_bas_r: '994.99',
          bkpr: '994',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '994',
          kftc_deal_bas_r: '994.99',
          cur_nm: '캐나다 달러',
        },
        {
          result: 1,
          cur_unit: 'CHF',
          ttb: '1,475.71',
          tts: '1,505.52',
          deal_bas_r: '1,490.62',
          bkpr: '1,490',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '1,490',
          kftc_deal_bas_r: '1,490.62',
          cur_nm: '스위스 프랑',
        },
        {
          result: 1,
          cur_unit: 'CNH',
          ttb: '189.37',
          tts: '193.2',
          deal_bas_r: '191.29',
          bkpr: '191',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '191',
          kftc_deal_bas_r: '191.29',
          cur_nm: '위안화',
        },
        {
          result: 1,
          cur_unit: 'DKK',
          ttb: '192.95',
          tts: '196.84',
          deal_bas_r: '194.9',
          bkpr: '194',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '194',
          kftc_deal_bas_r: '194.9',
          cur_nm: '덴마아크 크로네',
        },
        {
          result: 1,
          cur_unit: 'EUR',
          ttb: '1,437.12',
          tts: '1,466.15',
          deal_bas_r: '1,451.64',
          bkpr: '1,451',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '1,451',
          kftc_deal_bas_r: '1,451.64',
          cur_nm: '유로',
        },
        {
          result: 1,
          cur_unit: 'GBP',
          ttb: '1,655.85',
          tts: '1,689.3',
          deal_bas_r: '1,672.58',
          bkpr: '1,672',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '1,672',
          kftc_deal_bas_r: '1,672.58',
          cur_nm: '영국 파운드',
        },
        {
          result: 1,
          cur_unit: 'HKD',
          ttb: '169.31',
          tts: '172.74',
          deal_bas_r: '171.03',
          bkpr: '171',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '171',
          kftc_deal_bas_r: '171.03',
          cur_nm: '홍콩 달러',
        },
        {
          result: 1,
          cur_unit: 'IDR(100)',
          ttb: '8.91',
          tts: '9.1',
          deal_bas_r: '9.01',
          bkpr: '9',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '9',
          kftc_deal_bas_r: '9.01',
          cur_nm: '인도네시아 루피아',
        },
        {
          result: 1,
          cur_unit: 'JPY(100)',
          ttb: '963.7',
          tts: '983.17',
          deal_bas_r: '973.44',
          bkpr: '973',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '973',
          kftc_deal_bas_r: '973.44',
          cur_nm: '일본 옌',
        },
        {
          result: 1,
          cur_unit: 'KRW',
          ttb: '0',
          tts: '0',
          deal_bas_r: '1',
          bkpr: '1',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '1',
          kftc_deal_bas_r: '1',
          cur_nm: '한국 원',
        },
        {
          result: 1,
          cur_unit: 'KWD',
          ttb: '4,318.25',
          tts: '4,405.48',
          deal_bas_r: '4,361.87',
          bkpr: '4,361',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '4,361',
          kftc_deal_bas_r: '4,361.87',
          cur_nm: '쿠웨이트 디나르',
        },
        {
          result: 1,
          cur_unit: 'MYR',
          ttb: '293.04',
          tts: '298.96',
          deal_bas_r: '296',
          bkpr: '296',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '296',
          kftc_deal_bas_r: '296',
          cur_nm: '말레이지아 링기트',
        },
        {
          result: 1,
          cur_unit: 'NOK',
          ttb: '123.11',
          tts: '125.6',
          deal_bas_r: '124.36',
          bkpr: '124',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '124',
          kftc_deal_bas_r: '124.36',
          cur_nm: '노르웨이 크로네',
        },
        {
          result: 1,
          cur_unit: 'NZD',
          ttb: '827.88',
          tts: '844.61',
          deal_bas_r: '836.25',
          bkpr: '836',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '836',
          kftc_deal_bas_r: '836.25',
          cur_nm: '뉴질랜드 달러',
        },
        {
          result: 1,
          cur_unit: 'SAR',
          ttb: '353.55',
          tts: '360.7',
          deal_bas_r: '357.13',
          bkpr: '357',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '357',
          kftc_deal_bas_r: '357.13',
          cur_nm: '사우디 리얄',
        },
        {
          result: 1,
          cur_unit: 'SEK',
          ttb: '126.9',
          tts: '129.47',
          deal_bas_r: '128.19',
          bkpr: '128',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '128',
          kftc_deal_bas_r: '128.19',
          cur_nm: '스웨덴 크로나',
        },
        {
          result: 1,
          cur_unit: 'SGD',
          ttb: '987.86',
          tts: '1,007.81',
          deal_bas_r: '997.84',
          bkpr: '997',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '997',
          kftc_deal_bas_r: '997.84',
          cur_nm: '싱가포르 달러',
        },
        {
          result: 1,
          cur_unit: 'THB',
          ttb: '38.7',
          tts: '39.49',
          deal_bas_r: '39.1',
          bkpr: '39',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '39',
          kftc_deal_bas_r: '39.1',
          cur_nm: '태국 바트',
        },
        {
          result: 1,
          cur_unit: 'USD',
          ttb: '1,326',
          tts: '1,352.79',
          deal_bas_r: '1,339.4',
          bkpr: '1,339',
          yy_efee_r: '0',
          ten_dd_efee_r: '0',
          kftc_bkpr: '1,339',
          kftc_deal_bas_r: '1,339.4',
          cur_nm: '미국 달러',
        },
      ],
      selectedCountry: '미국 달러',
      foreignValue: 0,
      wonValue: 0,
    };
  },

  created() {
    // axios.get(API_URL, {
    //     params: {
    //         authkey: API_KEY,
    //         data: 'AP01',
    //         searchdate: '20230518'
    //     }
    // })
    // .then((res) => {
    //     console.log(res)
    // })
    // .catch((err) => {
    //     console.log(err)
    // })
  },

  methods: {
    calculateExchangeRate() {
      const bkpr = this.rateInfo.filter(
        (c) => c.cur_nm === this.selectedCountry
      )[0].bkpr;

      const rate = Number(bkpr.split(',').join(''));
      const foreignValue = Number(this.foreignValue);
      this.wonValue = foreignValue * rate;
    },
    calculateExchangeRateReverse() {
      const bkpr = this.rateInfo.filter(
        (c) => c.cur_nm === this.selectedCountry
      )[0].bkpr;

      const rate = Number(bkpr.split(',').join(''));
      const wonValue = Number(this.wonValue);
      this.foreignValue = wonValue / rate;
    },
  },
};
</script>

<style scoped></style>
