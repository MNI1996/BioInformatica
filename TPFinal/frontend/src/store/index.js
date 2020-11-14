import Vue from 'vue'
import Vuex from 'vuex'
import createLogger from "vuex/dist/logger";

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'
const apiUrl = "http://localhost:5000"


export default new Vuex.Store({
  strict: debug,
  plugins: debug ? [createLogger()] : [],
  state:{

  },
  getters:{
  },
  mutations: {
  },
  actions: {
  },
})