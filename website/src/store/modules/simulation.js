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
  },
};
