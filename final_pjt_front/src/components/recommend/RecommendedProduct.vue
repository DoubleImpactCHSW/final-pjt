<template>
    <div class="child-top-box">
        <div class="lefty">
            <div class="mr-4">{{ info.dcls_month }}</div>
            <div>{{ info.kor_co_nm }}</div>
        </div>
        <div class="boldy">{{ info.fin_prdt_nm }}</div>
    </div>
</template>

<script>
export default {
    name: 'RecommendedProduct',

    props: {
        info: Object,
    },

    methods: {

    }
};
</script>

<style scoped>
.child-top-box {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: wheat;
  padding: 20px;
  margin: 30px auto;
  max-width: 800px;
  border-radius: 20px;
  box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.3);
}
.lefty {
  display: flex;
  align-items: center;
  font-size: 18px;
}

.boldy {
  font-weight: 600;
  font-size: 20px;
}

</style>