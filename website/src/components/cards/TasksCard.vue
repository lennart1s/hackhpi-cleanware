<template>
  <CardOverlay ref="card" :X="0.7"
    :ShowOnMount="false"
    :Width="'270px'"
    :Height="'500px'"
    :scrollable="true"
  >
    <div class="wrapper">
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
          Num tasks:
          <input ref="numRand" type="number" value="1" min="1" max="99" />
        </label>
        <input @click="addRandomTasks()" type="button" value="Add" />
      </form>
      <div class="list">
        <div v-for="t, i of tasks" :key="i" class="task">
          {{ i + 1 }}. &nbsp; {{ t }} <span><button @click="removeTask(i)">x</button></span>
        </div>
      </div>
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
    ...mapActions(['saveDataCenters', 'addTask']),
    show() {
      this.tasks = this.dc.tasks;
      if (!this.dc.tasks) {
        this.dc.tasks = [];
      }
      this.$refs.card.show();
    },
    async addNewTask() {
      // let name = Math.random().toString(36).substr(2, 5);

      const cpup = this.$refs.cpup.value;
      this.dc.tasks.push(cpup);
      await this.setDataCenter({
        dataCenter: this.dc,
        index: this.dcIndex,
      });
      this.saveDataCenters();
      this.tasks = this.dc.tasks;
      this.addTask({ dc: this.dcIndex, cpup });
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
    async removeTask(i) {
      this.dc.tasks.splice(i, 1);
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
    this.tasks = this.dc.tasks;
  },
};
</script>

<style scoped lang="stylus">
.wrapper
  padding: 0.25rem 0.75rem !important
h2
  font-size: 1.3rem
  font-weight: 400

h3
  font-size: 1.15rem
  font-weight: 400
  margin: 5px
  grid-column: 1 / 4

form
  width: 100%
  display: grid
  grid-template-columns: 40% 20% 20%
  grid-gap: 5px

form label
  font-size: 1rem
  font-weight: 400
  grid-column: 1 / 3
  display: grid
  grid-template-columns: 66% 33%

form input
  width: 40px
  grid-column: 2 / 3

form input[type=button]
  margin-left: auto
  grid-column: 3 / 4
  width: 60px !important
  background-color: transparent
  font-size: 0.95rem
  border: 1px solid black
  border-radius: 2px
  padding-block: 3px
  cursor: pointer
  &:hover
    background-color: rgba(0, 0, 0, 0.05)

.list
  margin-block: 0.75rem
  margin-left: 10px

.task
  width: 100%

.task span
  margin-left: auto
</style>
