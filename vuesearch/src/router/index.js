import Vue from 'vue';
import Router from 'vue-router'

import Home from '@/views/Home.vue';
import SearchEngine from '@/components/SearchEngine';
import Warning from '@/views/Warning';

Vue.use(Router);

const router = new Router({
    routes: [
      {
        path: '/',
        name: 'home',
        component: Home,
      },
      {
        path: '/search:q',
        name: 'search',
        component: SearchEngine,
        props: true
      },
      {
        path: '/warning',
        name: 'warning',
        component: Warning
      }
    ]
})

export default router;
