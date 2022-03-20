import VModal from 'vue-js-modal';
import 'vue-js-modal/dist/styles.css';

import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import '@/assets/main.styl';

Vue.config.productionTip = false;

Vue.use(VModal, {});

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
