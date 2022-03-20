<template>
  <CardOverlay ref="card"
    :ShowOnMount="false">
    <p class="coords">{{lon}}° N, {{lat}}° E</p>
    <form>
      <label for="name">
        <input ref="name" type="text" class="editable" v-model="name"
          style="grid-column: 1 / 4"
        />
      </label>
      <label for="numClusters">
        Racks:
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
      <input class="del-btn" type="button" value="Delete"
        @click="deleteDataCenter()"
      />
      <input class="save-btn" type="button" value="Save"
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
  },
  data: () => ({
    dcIndex: 0,
    name: '',
    numClusters: 0,
    solarArea: 0,
    numTurbines: 0,
    lat: 0,
    lon: 0,
  }),
  methods: {
    ...mapActions(['newDataCenter', 'saveDataCenters']),
    ...mapMutations(['setDataCenter', 'removeDataCenter']),
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
          tasks: this.dc.tasks,
          weather: this.dc.weather,
        },
        index: this.dcIndex,
      });

      this.saveDataCenters();

      this.$refs.card.hide();
    },
    deleteDataCenter() {
      this.removeDataCenter(this.dcIndex);
      this.saveDataCenters();
      this.$refs.card.hide();
    },
    async setup(lat, lon) {
      this.$refs.card.show();
      this.dcIndex = await this.newDataCenter(lat, lon);
      this.lat = Math.round(lat * 1000) / 1000;
      this.lon = Math.round(lon * 1000) / 1000;
      this.name = this.dc?.name || '';
      this.numClusters = this.dc?.numClusters || 1;
      this.solarArea = this.dc?.solarArea || 0;
      this.numTurbines = this.dc?.numTurbines || 0;
    },
    show(i) {
      this.dcIndex = -1;
      this.dcIndex = i;
      this.name = this.dc?.name || '';
      this.numClusters = this.dc?.numClusters || 1;
      this.solarArea = this.dc?.solarArea || 0;
      this.numTurbines = this.dc?.numTurbines || 0;
      this.$refs.card.show();
    },
  },
  computed: {
    ...mapGetters(['dataCenters', 'dataCenter']),
    dc() {
      return this.dataCenter(this.dcIndex);
    },
  },
  mounted() {
    // this.setup();
  },
};
</script>

<style scoped lang="stylus">
form
  padding: 1rem
  padding-top: 0
  display: grid
  grid-gap: 5px
  grid-template-columns: 50% 50%

input.editable
  padding: 5px
  font-size: 1.2rem
  border: 1px solid rgba(0, 0, 0, 0.0)
  &:hover
    padding: 5px
    border: 1px solid rgba(0, 0, 0, 0.2)

form label
  grid-column: 1 / 3
  width: 100%
  display: grid
  grid-template-columns: 50% 40% 10%

form input:not(.editable)
  grid-column: 2 / 3
  margin-left: auto
  width: 40%

.del-btn,.save-btn
  width: 80px !important
  margin-inline: auto
  margin-top: 12px
  background-color: transparent
  font-size: 0.95rem
  border: 1px solid black
  border-radius: 2px
  padding-block: 3px
  cursor: pointer
  &:hover
    background-color: rgba(0, 0, 0, 0.05)

.del-btn
  grid-column: 1 / 2 !important

.save-btn
  grid-column: 2 / 3 !important

.coords
  margin-bottom: 5px
  margin-left: 15px
  color: rgba(0,0,0, 0.3)
  font-size: 0.7rem

</style>
