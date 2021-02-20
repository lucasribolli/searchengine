import Vue from 'vue'
import App from './App.vue'
import router from '@/router';
import { BootstrapVue, BSpinner, BLink } from 'bootstrap-vue'
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

Vue.use(BootstrapVue)

Vue.component('b-link', BLink)
Vue.component('b-spinner', BSpinner)

const API_ROOT = "http://127.0.0.1:8088";
Vue.prototype.$api_search = API_ROOT + "/api/search";
Vue.prototype.$per_page = 10;

Vue.config.productionTip = false

new Vue({
  router,
  el: '#app',
  render: h => h(App),
}).$mount('#app')