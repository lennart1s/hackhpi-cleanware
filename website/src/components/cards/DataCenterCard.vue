<template>
  <CardOverlay ref="card"
    :ShowOnMount="true">
    <form>
      <label for="name">
        <input ref="name" type="text" v-model="name"/>
      </label>
      <label for="numClusters">
        Clusters:
        <input ref="numClusters" type="number" v-model="numClusters" />
      </label>
      <label for="solarArea">
        Solar panels:
        <input ref="solarArea" type="number" v-model="solarArea" />
        <span>m²</span>
      </label>
      <label for="numTurbines">
        Turbines:
        <input ref="numTurbines" type="number" v-model="numTurbines" />
      </label>
      <input type="button" value="Delete"
        @click="deleteDataCenter()"
      />
      <input type="button" value="Save"
        @click="saveDataCenter()"
      />
    </form>
    <button @click="$refs.tasksCard.show()">Show Tasks</button>
    <TasksCard ref="tasksCard"
      :dcIndex="dcIndex"
    />
  </CardOverlay>
</template>

<script>
import { mapGetters, mapActions, mapMutations } from 'vuex';
import CardOverlay from '@/components/cards/CardOverlay.vue';
import TasksCard from '@/components/cards/TasksCard.vue';

export default {
  name: 'DataCenterCard',
  components: {
    CardOverlay,
    TasksCard,
  },
  props: {
    lat: {
      Type: Number,
      default: 0,
    },
    lon: {
      Type: Number,
      default: 0,
    },
  },
  data: () => ({
    dcIndex: 0,
    name: '',
    numClusters: 0,
    solarArea: 0,
    numTurbines: 0,
  }),
  methods: {
    ...mapActions(['newDataCenter', 'saveDataCenters']),
    ...mapMutations(['setDataCenter']),
    async saveDataCenter() {
      if (this.dcIndex < 0) {
        return;
      }
      await this.setDataCenter({
        dataCenter: {
          name: this.name,
          numClusters: this.numClusters,
          solarArea: this.solarArea,
          numTurbines: this.numTurbines,
          lat: this.lat,
          lon: this.lon,
        },
        index: this.dcIndex,
      });

      this.saveDataCenters();

      this.$refs.card.hide();
    },
    deleteDataCenter() {
      this.$refs.card.hide();
    },
  },
  computed: {
    ...mapGetters(['dataCenters', 'dataCenter']),
    dc() {
      return this.dataCenter(this.dcIndex);
    },
  },
  async mounted() {
    this.dcIndex = await this.newDataCenter(69, 420);
    this.name = this.dc?.name || '';
    this.numClusters = this.dc?.numClusters || 1;
    this.solarArea = this.dc?.solarArea || 0;
    this.numTurbines = this.dc?.numTurbines || 0;
  },
};
</script>

<style scoped lang="stylus">
form
  display: grid
</style>
