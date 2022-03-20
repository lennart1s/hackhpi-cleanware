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
  },
};
