<template>
  <div>
    <h1>
      DataCenter
    </h1>
    <h2>
      {{ dataCenter.name }}
    </h2>

    <form class="form">
      <label for="dcName">
        Name:
        <input ref="dcName" :value="dataCenter.name" type="text" />
      </label>
      <br />
      <label for="dcLat">
        Breitengrad:
        <input ref="dcLat" :value="dataCenter.lat" type="number" />
      </label>
      <br />
      <label for="dcLong">
        Längengrad:
        <input ref="dcLong" :value="dataCenter.long" type="number" />
      </label>
      <br />
      <label for="dcClusterNum">
        Cluster-Anzahl:
        <input ref="dcClusterNum" :value="dataCenter.numClusters" type="number"
        />
      </label>
      <br />
      <input ref="submit" type="button"
        value="Änderungen Speichern"
        @click="saveChanges()"
      />
    </form>
    <Map
      @dcCreated="dcCreated"
      @dcClicked="dcClicked"
    />
  </div>
</template>

<script>
import Map from '@/components/Map.vue';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'DataCenter',
  data: () => ({
    dataCenter: undefined,
  }),
  components: {
    Map,
  },
  computed: {
    ...mapGetters(['dataCenters']),
  },
  created() {
    this.loadDataCenters();
  },
  mounted() {
    this.init();
  },
  methods: {
    ...mapActions(['saveDataCenters', 'updateDataCenter', 'loadDataCenters']),
    dcCreated(dc) {
      console.log('dcCreated', dc);
    },
    dcClicked(n) {
      console.log('dcClicked', n);
    },
    saveChanges() {
      this.dataCenter = {
        name: this.$refs.dcName.value,
        lat: this.$refs.dcLat.value,
        long: this.$refs.dcLong.value,
        numClusters: this.$refs.dcClusterNum.value,
      };

      this.updateDataCenter({ i: this.$route.params.dcIndex, dc: this.dataCenter });
      this.$router.go(this.$router.currentRoute);
    },
    init() {
      this.dataCenter = this.dataCenters[this.$route.params.dcIndex];
    },
  },
  watch: {
    '$route.params.dcIndex': function () {
      this.init();
    },
  },
};
</script>
