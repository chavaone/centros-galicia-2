import Vue from 'vue'
import VueI18n from 'vue-i18n'

//Setup i18n
Vue.use(VueI18n)
const i18n = new VueI18n({
  locale: 'gl'
})

import './assets/scripts/imports.js'

export const eventBus = new Vue()

import App from './App.vue'
new Vue({
  i18n,
  render: h => h(App)
}).$mount('#app')
