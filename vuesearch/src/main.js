import Vue from 'vue'
import App from './App.vue'
import Router from'vue-router'
import SearchEngine from './components/SearchEngine.vue'
import Result from './components/Result.vue'
import { BootstrapVue, IconsPlugin, PaginationPlugin } from 'bootstrap-vue'
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
import { BLink } from 'bootstrap-vue'
import { BSpinner } from 'bootstrap-vue'
import { BImg } from 'bootstrap-vue'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(PaginationPlugin)
Vue.use(Router)
Vue.component('b-link', BLink)
Vue.component('b-spinner', BSpinner)
Vue.component('b-img', BImg)

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