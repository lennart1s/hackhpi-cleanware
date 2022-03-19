<template>
  <div>
    DataCenter
    {{ dataCenter.name }}
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'DataCenter',
  components: {
  },
  computed: {
    ...mapGetters(['dataCenters']),
    dataCenter() {
      return this.dataCenters[this.$route.params.dcIndex];
    },
  },
  mounted() {
    // console.log(this.$route.params);
  },
};
</script>
