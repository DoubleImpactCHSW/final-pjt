<template>
    <div>
        <h1>환율 페이지</h1>

        <hr>

        <RateCalculator />
    </div>
</template>

<script>
import RateCalculator from '@/components/exchange/RateCalculator'
export default {
    name: 'ExchangeView',

    components: {
        RateCalculator,
    },

    data() {
        return {
            
        };
    },

    mounted() {
        
    },

    methods: {
        
    },
};
</script>

<style scoped>

</style>