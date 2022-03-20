export default {
  state: {
    time: Date.now(),
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
