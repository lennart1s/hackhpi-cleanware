export default {
  state: {
    time: 0,
  },
  getters: {
    time: (state) => state.time,
  },
  mutations: {
    setTime(state, t) {
      state.time = t;
    },
  },
  actions: {
    async getStatus() {
      const resp = fetch('http://localhost:5000/status');
      const data = await resp.json();

      console.log(data);
    },
    getFakeData({ state }) {
      let valuesA = [425, 413, 511, 502, 492, 490, 493, 430, 428];
      let valuesB = [310, 322, 341, 372, 374, 407, 410, 408, 410];
      for (let i = 0; i <= state.time; i += 1) {
        valuesA = valuesA.unshift(0);
        valuesB = valuesB.unshift(0);
      }

      return { valuesA, valuesB };
    },
  },
};
