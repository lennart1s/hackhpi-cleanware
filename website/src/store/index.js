import Vue from 'vue';
import Vuex from 'vuex';

import moduleDatacenters from './modules/datacenters';
import moduleSimulation from './modules/simulation';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
    moduleDatacenters,
    moduleSimulation,
  },
});
