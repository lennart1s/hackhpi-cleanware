<template>
  <div>
    <div class="banner">
      <img src="@/assets/cleanware-logo-768x461.png" alt="logo">
    </div>
    <Map @dcCreated="handleMapCreation"
      @dcClicked="handleMapClick"
      @run="handleRun"
    >
    </Map>
    <p class="time-shift">+{{time}}h</p>
    <DataCenterCard ref="dcc"></DataCenterCard>
    <!--<button @click="$refs.dcc.setup()">New</button>-->
    <!--<PieChart></PieChart>-->
    <modal name="chart" width="500px" height="500px">
      <LineChart class="consumption-chart"></LineChart>
    </modal>
    <button @click="$modal.show('chart')">Open Chart</button>
  </div>
</template>

<script>
import Map from '@/components/Map.vue';
import DataCenterCard from '@/components/cards/DataCenterCard.vue';
import LineChart from '@/components/charts/LineChart.vue';
// import PieChart from '@/components/charts/PieChart.vue';
import { mapGetters, mapMutations, mapActions } from 'vuex';

export default {
  name: 'HomeView',
  components: {
    Map,
    DataCenterCard,
    LineChart,
    // PieChart,
  },
  methods: {
    ...mapMutations(['setTime']),
    ...mapActions(['getWeatherForDataCenter']),
    handleRun() {
      console.log('run');
      this.setTime(this.time + 1);
    },
    async handleMapCreation({ long, lat, n }) {
      // console.log(long, lat, n);
      await this.getWeatherForDataCenter(n - 1);
      this.$refs.dcc.setup(long, lat, n);
    },
    handleMapClick(n) {
      this.$refs.dcc.show(n - 1);
    },
  },
  computed: {
    ...mapGetters(['time']),
  },
};
</script>

<style lang="stylus">
.banner
  pointer-events: none
  z-index: 1000
  width: 100%
  position: absolute
  height: 100px

.banner img
  margin-right: 2rem
  float: right
  height: 100px
  -webkit-filter: drop-shadow(5px 5px 5px rgba(0, 0, 0, 0.22));
  filter: drop-shadow(5px 5px 5px rgba(0, 0, 0, 0.22));

.consumption-chart
  display: absolute
  z-index: 1000
  background-color: rgba(0,0,0,0);
  width: 1400px
  height: 800px

.time-shift
  z-index: 1000
  position: absolute
  top: 3.5%
  left: 55%
  text-shadow: 1px 1px 5px rgba(0,0,0,0.4)
  font-weight: 400
  font-size: 1.5rem

</style>
