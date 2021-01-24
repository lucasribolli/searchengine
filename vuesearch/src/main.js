import Vue from 'vue'
import App from './App.vue'
import Router from'vue-router'
import SearchEngine from './components/SearchEngine.vue'
import Result from './components/Result.vue'
import { BootstrapVue, IconsPlugin, PaginationPlugin } from 'bootstrap-vue'
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(Router)
Vue.use(PaginationPlugin)

const router = new Router({
  routes:[
    {
      path: '/',
      name: 'searchengine',
      component: SearchEngine
    },
    {
      path: '/result/:id',
      name: 'result',
      component: Result,
      props: true
    }
  ]
})

const API_ROOT = "http://127.0.0.1:8088";
Vue.prototype.$api_search = API_ROOT + "/api/search";

Vue.config.productionTip = false

new Vue({
  el: '#app',
  render: h => h(App),
  router
})