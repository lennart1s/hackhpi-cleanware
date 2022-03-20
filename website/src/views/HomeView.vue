<template>
  <div>
    <DataCenterCard></DataCenterCard>
    <PieChart></PieChart>
  </div>
</template>

<script>
import DataCenterCard from '@/components/cards/DataCenterCard.vue';
import PieChart from '@/components/charts/PieChart.vue';

export default {
  name: 'HomeView',
  components: {
    DataCenterCard,
    PieChart,
  },
};
</script>
