<template>
  <modal class="card">
    <slot></slot>
  </modal>
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
@import '../assets/theme.styl';

#nav
  background-color: $secondary
  width: 100%
  height: 2rem

  display: flex
  flex-direction: row
  justify-content: left

.add-dc-btn
  color: white
  background-color: $accent
  border: none
  margin-left: auto
  height: 100%
  padding-inline: 1rem
  size: 3rem
  font-weight: bold
  cursor: pointer
  &:hover
    background-color: $accent-light
</style>
