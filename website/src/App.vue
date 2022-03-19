<template>
  <div>
    <nav>
      <GlobalNavigation />
    </nav>
    <router-view/>
  </div>
</template>

<script>
import GlobalNavigation from '@/components/GlobalNavigation.vue';
import { mapActions } from 'vuex';

export default {
  components: {
    GlobalNavigation,
  },
  methods: {
    ...mapActions(['loadDataCenters']),
  },
  mounted() {
    this.loadDataCenters();
  },
};
</script>

<style lang="stylus">
body {
  margin: 0
}
</style>
