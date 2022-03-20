export default {
  state: {
    dataCenters: [],
  },
  getters: {
    dataCenters: (state) => state.dataCenters,
    dataCenter: (state) => (index) => state.dataCenters[index],
  },
  mutations: {
    setDataCenter(state, { dataCenter, index }) {
      state.dataCenters[index] = dataCenter;
    },
    addDataCenter(state, dc) {
      state.dataCenters.push(dc);
    },
  },
  actions: {
    async newDataCenter({ commit, dispatch, state }, { lat, lon }) {
      let maxLblIndex = 0;
      for (let i = 0; i < state.dataCenters.length; i += 1) {
        if (state.dataCenters[i].name.startsWith('Unnamed ')) {
          const lblIndex = Number.parseInt(state.dataCenters[i].name.replace('Unnamed ', ''), 10);
          if (lblIndex > maxLblIndex) {
            maxLblIndex = lblIndex;
          }
        }
      }

      const dc = {
        name: `Unnamed ${maxLblIndex + 1}`,
        numClusters: 1,
        solarArea: 0,
        numTurbines: 0,
        lat: lat || 0,
        lon: lon || 0,
      };

      commit('addDataCenter', dc);
      dispatch('saveDataCenters');
      return state.dataCenters.length - 1;
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
