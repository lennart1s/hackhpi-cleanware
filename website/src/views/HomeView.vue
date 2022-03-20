<template>
  <div>
    <DataCenterCard ref="dcc"></DataCenterCard>
    <button @click="$refs.dcc.setup()">New</button>
    <!--<PieChart></PieChart>-->
  </div>
</template>

<script>
import DataCenterCard from '@/components/cards/DataCenterCard.vue';
// import PieChart from '@/components/charts/PieChart.vue';

export default {
  name: 'HomeView',
  components: {
    DataCenterCard,
    // PieChart,
  },
};
</script>
