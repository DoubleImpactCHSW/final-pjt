<template>
    <div class="outer">
        
    </div>
</template>

<script>
export default {
    name: 'ChoiceCard',

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
.outer {
    background-color: lightsalmon;
    width: 300px;
    height: 500px;
    border-radius: 20px;
    box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.4);
    transition: transform 0.3s, box-shadow 0.3s;
    margin: 50px;
}

.outer:hover {
    transform: scale(1.05);
    box-shadow: 0px 12px 40px rgba(0, 0, 0, 0.6);
}

@keyframes pulse {
    0% {
        transform: scale(1);
    }
    50% {
        transform: scale(1.1);
    }
    100% {
        transform: scale(1);
    }
}

.outer:hover {
    animation: pulse 0.6s infinite;
}

</style>