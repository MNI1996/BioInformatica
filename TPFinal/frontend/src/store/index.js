import Vue from 'vue'
import Vuex from 'vuex'

import createLogger from "vuex/dist/logger";

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'
const apiUrl = "http://localhost:5000"

function showErrorWithNoty(error) {
  if (error.response) {
    Vue.noty.error(error.response.data.message, {killer: true})
  } else if (error.message) {
    Vue.noty.error("Error interno")
  } else {
    Vue.noty.error("Error desconocido", {killer: true})
  }
}

export default new Vuex.Store({
  strict: debug,
  plugins: debug ? [createLogger()] : [],
  state:{
    result:null,
    codMuestra:"1THJ"
  },
  getters:{
    result: (state) => state.result,
    codMuestra: (state)=>state.codMuestra,
  },
  mutations: {
    setResult: (state, result) => state.result = result,
  },
  actions:{
    async search({commit},data){
      Vue.noty.success("Su Peticion esta siendo procesada, esto llevara un tiempo")
     await Vue.axios.post( `${apiUrl}/pdb`,data)
                    .then(response=>{commit('setResult', response.data)
                                      Vue.noty.info("Ya estan sus resultados")})
                    .catch((error)=>{showErrorWithNoty(error)});
    },

  },
})