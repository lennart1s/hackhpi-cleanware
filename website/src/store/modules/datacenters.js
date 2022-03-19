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
      });
      dispatch('saveDataCenter');
    },
    saveDataCenter({ state }) {
      sessionStorage.setItem('dataCenters', JSON.stringify(state.dataCenters));
    },
    loadDataCenters({ state }) {
      const data = sessionStorage.getItem('dataCenters');
      if (data) {
        state.dataCenters = JSON.parse(data);
      }
    },
  },
};
