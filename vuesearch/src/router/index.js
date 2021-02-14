import Vue from 'vue';
import Router from 'vue-router'

import VueSearch from '@/views/VueSearch.vue';
import SearchEngine from '@/components/SearchEngine';
import Warning from '@/views/Warning';

Vue.use(Router);

const router = new Router({
    mode: 'history',
    routes: [
      { 
        path: '*', 
        redirect: '/' 
      },
      {
        path: '/',
        name: 'vuesearch',
        component: VueSearch,
      },
      {
        path: '/search?q=:q',
        name: 'search',
        component: SearchEngine,
        props: true,
        children: [
          {
            path: '/warning/:code',
            name: 'warning',
            component: Warning,
            props: true
          }
        ]
      }
    ]
})

export default router;