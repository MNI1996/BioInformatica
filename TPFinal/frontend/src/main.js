import Vue from 'vue'
import VueRouter from 'vue-router'
import axios from 'axios'
import VueAxios from 'vue-axios'
import App from './App.vue'
import "../assets/app.css"
import 'vuejs-noty/dist/vuejs-noty.css'
import 'es6-promise/auto'
import VueNoty from 'vuejs-noty'
import store from './store'
import Home from "./pages/Home.vue";

require('bootstrap');
import 'bootstrap/dist/css/bootstrap.min.css';
import '../Styles.css';

Vue.use(VueAxios, axios)
Vue.use(VueRouter)
Vue.use(VueNoty)
Vue.config.productionTip = false

const router = new VueRouter({
  routes: [
    { path: '/', name:"home", component: Home },

  ]
})

new Vue({
  el: '#app',
  components: {App: App},
  store,
  router,
  render: h => h(App)
})