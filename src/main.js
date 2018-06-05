import Vue from 'vue'
import VueI18n from 'vue-i18n'
import VueClipboard from 'vue-clipboard2'
import Meta from 'vue-meta';
import galite from 'ga-lite';

//Setup i18n
Vue.use(VueI18n)
const i18n = new VueI18n({
  locale: 'gl',
  fallbackLocale: 'gl'
})

Object.defineProperty(Vue.prototype, '$locale', {
    get: function () {
      return i18n.locale
    },
    set: function (locale) {
      i18n.locale = locale
    }
  })

Vue.use(VueClipboard)

//Setup metadata SEO
Vue.use(Meta);

//Google Analytics
galite('create', 'UA-XXXXX-X', 'auto')
galite('send', 'pageview')

import './assets/scripts/imports.js'

export const eventBus = new Vue()

import App from './App.vue'
new Vue({
  i18n,
  render: h => h(App),
  mounted () {
      // You'll need this for renderAfterDocumentEvent.
      document.dispatchEvent(new Event('render-event'))
    }
}).$mount('#app')
