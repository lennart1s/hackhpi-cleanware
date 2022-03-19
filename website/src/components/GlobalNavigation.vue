<template>
  <div id="nav">
    <router-link
      v-for="dc, i of dataCenters" :key="i"
      :to="{ name: 'DataCenter', params: { dcIndex: i } }"
      class="nav-tab"
    >
      <div>
        {{ dc.name }}
      </div>
    </router-link>
    <button class="add-dc-btn" @click="addNewDC()">+</button>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'GlobalNavigation',
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

.nav-tab
  width: 14ch
  background-color: rgba(0, 0, 0, 0.2)
  height: 100%
  text-align: center
  &:hover
    background-color: rgba(0, 0, 0, 0.4)
    cursor: pointer
</style>
