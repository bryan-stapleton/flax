import Vue from 'vue'
import App from './App.vue'
import PortalVue from 'portal-vue'
import { BootstrapVue } from 'bootstrap-vue'
import VueGoogleCharts from 'vue-google-charts'

Vue.config.productionTip = false
Vue.use(PortalVue)
Vue.use(BootstrapVue)
Vue.use(VueGoogleCharts)

new Vue({
  render: h => h(App),
}).$mount('#app')