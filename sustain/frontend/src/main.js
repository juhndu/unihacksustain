import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import StarRating from 'vue-star-rating'
import VueGeolocation from 'vue-browser-geolocation';

Vue.config.productionTip = false
Vue.component('star-rating', StarRating);
Vue.use(VueGeolocation);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')

