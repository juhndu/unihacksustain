import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import StarRating from 'vue-star-rating'
import VueGeolocation from 'vue-browser-geolocation';
import axios from 'axios'
import VueAxios from 'vue-axios'
import * as VueGoogleMaps from 'vue2-google-maps'

Vue.config.productionTip = false
Vue.component('star-rating', StarRating);
Vue.use(VueGeolocation);
Vue.use(VueAxios, axios)

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyCKtPukhHO9i3gFbNYy9Pblm7luQ_N4mAE',
    libraries: 'places', // This is required if you use the Autocomplete plugin
  },
})


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

