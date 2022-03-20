<template>
  <CardOverlay ref="card" :X="0.7">
    <h2>Tasks</h2>
    <form>
      <h3>Add manually:</h3>
      <label for="cpup">
        CPU usage:
        <input ref="cpup" type="number" value="0.3" min="0.05" max="1.0" step="0.05"/>
      </label>
      <input @click="addNewTask()" type="button" value="Add" />
    </form>
    <form>
      <h3>Add random tasks:</h3>
      <label for="numRand">
        Number of tasks:
        <input ref="numRand" type="number" />
      </label>
      <input @click="addRandomTasks()" type="button" value="Add" />
    </form>
    <div v-for="t, i of tasks" :key="i">
      {{ i + 1 }}. {{ t }}
    </div>
  </CardOverlay>
</template>

<script>
import CardOverlay from '@/components/cards/CardOverlay.vue';
import { mapGetters, mapMutations, mapActions } from 'vuex';

export default {
  name: 'TasksCard',
  components: {
    CardOverlay,
  },
  props: {
    dcIndex: {
      Type: Number,
    },
  },
  data: () => ({
    tasks: [],
  }),
  methods: {
    ...mapMutations(['setDataCenter']),
    ...mapActions(['saveDataCenters']),
    show() {
      this.$refs.card.show();
    },
    async addNewTask() {
      const cpup = this.$refs.cpup.value;
      this.dc.tasks.push(cpup);
      await this.setDataCenter({
        dataCenter: this.dc,
        index: this.dcIndex,
      });
      this.saveDataCenters();
      this.tasks = this.dc.tasks;
    },
    async addRandomTasks() {
      const n = this.$refs.numRand.value;
      for (let i = 0; i < n; i += 1) {
        this.dc.tasks.push(Math.floor((Math.random() * 0.95 + 0.05) * 20) / 20);
      }
      await this.setDataCenter({
        dataCenter: this.dc,
        index: this.dcIndex,
      });
      this.saveDataCenters();
      this.tasks = this.dc.tasks;
    },
  },
  computed: {
    ...mapGetters(['dataCenters', 'dataCenter']),
    dc() {
      return this.dataCenter(this.dcIndex);
    },
  },
  created() {
    if (!this.dc.tasks) {
      this.dc.tasks = [];
    }
  },
};
</script>

<style scoped lang="stylus">
form
  display: grid
</style>
