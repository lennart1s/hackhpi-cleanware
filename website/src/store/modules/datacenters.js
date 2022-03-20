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
    removeDataCenter(state, index) {
      state.dataCenters.splice(index, 1);
    },
  },
  actions: {
    async addTask({ dc, task }) {
      fetch(`http://localhost:5000/dc/${dc}/task/${task}`, {
        method: 'PUT',
      });
    },
    async newDataCenter({ commit, dispatch, state }, { lat, lon }) {
      /* let maxLblIndex = 0;
      for (let i = 0; i < state.dataCenters.length; i += 1) {
        if (state.dataCenters[i].name.startsWith('Unnamed ')) {
          const lblIndex = Number.parseInt(state.dataCenters[i].name.replace('Unnamed ', ''), 10);
          if (lblIndex > maxLblIndex) {
            maxLblIndex = lblIndex;
          }
        }
      } */

      const dc = {
        name: `DataCenter ${state.dataCenters.length + 1}`,
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
    /* saveDataCenters({ state }) {
      sessionStorage.setItem('dataCenters', JSON.stringify(state.dataCenters));
    }, */
    async getWeatherForDataCenter({ state }, i) {
      const dc = state.dataCenters[i];

      const resp = await fetch('http://localhost:8000/?days=2', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          lat: dc.lat,
          long: dc.lon,
          capacity: dc.solarArea,
          turbines: dc.numTurbines,
        }),
      });

      const data = await resp.json();
      console.log(data);
      state.dataCenters[i].weather = data;
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
