import Vue from 'vue'
import App from './App.vue'
import Router from'vue-router'
import SearchEngine from './components/SearchEngine.vue'
import Result from './components/Result.vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(Router)

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

Vue.config.productionTip = false

new Vue({
  el: '#app',
  render: h => h(App),
  router
})