<template>
  <div>
    <Map @dcCreated="handleMapCreation"
      @dcClicked="handleMapClick"
    >
    </Map>
    <DataCenterCard ref="dcc"></DataCenterCard>
    <!--<button @click="$refs.dcc.setup()">New</button>-->
    <!--<PieChart></PieChart>-->
  </div>
</template>

<script>
import Map from '@/components/Map.vue';
import DataCenterCard from '@/components/cards/DataCenterCard.vue';
// import PieChart from '@/components/charts/PieChart.vue';

export default {
  name: 'HomeView',
  components: {
    Map,
    DataCenterCard,
    // PieChart,
  },
  methods: {
    handleMapCreation({ long, lat, n }) {
      // console.log(long, lat, n);
      this.$refs.dcc.setup(long, lat, n);
    },
    handleMapClick(n) {
      this.$refs.dcc.show(n - 1);
    },
  },
};
</script>
