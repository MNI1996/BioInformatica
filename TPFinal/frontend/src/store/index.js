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
    result:null,
  },
  getters:{
    result: (state) => state.result,
  },
  mutations: {
    setResult: (state, result) => state.result = result,
  },
  actions:{
    async search({commit},id){
      let response = await Vue.axios.get( `${apiUrl}/pdb?id=${id}`);
      commit('setResult', response.data)
    }
  },
})