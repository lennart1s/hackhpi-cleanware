export default {
  state: {
    dataCenters: [],
  },
  getters: {
    dataCenters: (state) => state.dataCenters,
  },
  mutations: {
    addDC(state, dc) {
      state.dataCenters.push(dc);
    },
  },
  actions: {
    newDC({ commit, dispatch, state }) {
      commit('addDC', {
        name: `Unnamed ${state.dataCenters.length + 1}`,
        numClusters: 1,
        lat: 0,
        long: 0,
      });
      dispatch('saveDataCenters');
    },
    saveDataCenters({ state }) {
      sessionStorage.setItem('dataCenters', JSON.stringify(state.dataCenters));
    },
    loadDataCenters({ state }) {
      const data = sessionStorage.getItem('dataCenters');
      if (data) {
        state.dataCenters = JSON.parse(data);
      }
    },
    updateDataCenter({ state, dispatch }, data) {
      state.dataCenters[data.i] = data.dc;
      dispatch('saveDataCenters');
    },
  },
};
