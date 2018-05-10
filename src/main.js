import Vue from 'vue'
import VueI18n from 'vue-i18n'

Vue.use(VueI18n)
import './assets/scripts/imports.js'

import App from './App.vue'

new Vue({
  el: '#app',
  render: h => h(App)
})
