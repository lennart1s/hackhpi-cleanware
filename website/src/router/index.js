import Vue from 'vue';
import VueRouter from 'vue-router';
import DataCenter from '@/views/DataCenter.vue';
import HomeView from '../views/HomeView.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
  {
    path: '/dc/:dcIndex([0-9]+)',
    name: 'DataCenter',
    component: DataCenter,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
