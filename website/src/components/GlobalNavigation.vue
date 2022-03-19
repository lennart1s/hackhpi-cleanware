<template>
  <div id="nav">
    <NavigationTab :to="{ name: 'home' }">Home</NavigationTab>
    <NavigationTab
      v-for="dc, idx of dataCenters" :key="idx"
      :to="{ name: 'DataCenter', params: { dcIndex: idx } }"
    >
      {{ dc.name }}
    </NavigationTab>
    <button class="add-dc-btn" @click="addNewDC()">+</button>
  </div>
</template>

<script>
import NavigationTab from '@/components/NavigationTab.vue';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'GlobalNavigation',
  components: {
    NavigationTab,
  },
  methods: {
    ...mapActions(['newDC']),
    addNewDC() {
      this.newDC();
    },
  },
  computed: {
    ...mapGetters(['dataCenters']),
  },
};
</script>

<style scoped lang="stylus">
#nav
  background-color: rgba(0, 0, 0, 0.2)
  width: 100%
  height: 2rem

  display: flex
  flex-direction: row
  justify-content: left

.add-dc-btn
  color: white
  background-color: rgb(44, 62, 143)
  border: none
  margin-left: auto
  height: 100%
  padding-inline: 1rem
  size: 3rem
  font-weight: bold
  cursor: pointer
</style>
