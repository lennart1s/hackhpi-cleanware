export default {
  state: {
    dataCenters: [],
  },
  getters: {
    dataCenters: (state) => state.dataCenters,
    dataCenter: (state) => (index) => state.dataCenters[index],
  },
  mutations: {
    setDC(state, dc, index) {
      state.dataCenters[index] = dc;
    },
    addDC(state, dc) {
      state.dataCenters.push(dc);
    },
  },
  actions: {
    newDataCenter({ commit, dispatch, state }) {
      let maxLblIndex = 0;
      for (let i = 0; i < state.dataCenters.length; i += 1) {
        if (state.dataCenters[i].name.startsWith('Unnamed ')) {
          const lblIndex = Number.parseInt(state.dataCenters[i].name.replace('Unnamed ', ''), 10);
          if (lblIndex > maxLblIndex) {
            maxLblIndex = lblIndex;
          }
        }
      }

      commit('addDC', {
        name: `Unnamed ${maxLblIndex + 1}`,
        numClusters: 1,
        lat: 0,
        long: 0,
      }, 1);
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
    clearDataCenters({ state }) {
      state.dataCenters = [];
      sessionStorage.removeItem('dataCenters');
    },
  },
};
