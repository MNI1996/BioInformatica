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
    codMuestra:"1THJ",
    viewAlign:false,
    viewDssp:false,
    visualizer:false
  },
  getters:{
    result:     (state)=> state.result,
    codMuestra: (state)=> state.codMuestra,
    viewAlign:  (state)=> state.viewAlign,
    viewDssp:   (state)=> state.viewDssp,
    visualizer: (state)=> state.visualizer
  },
  mutations: {
    setResult: (state, result) => state.result = result,
    setVA:(state)=>state.viewAlign= !state.viewAlign,
    setVD:(state)=>state.viewDssp= !state.viewDssp,
    setVisualizer:(state)=>state.visualizer= !state.visualizer,
    resetResult:(state)=>state.result=null
  },
  actions:{
    async search({commit},data){
      Vue.noty.success("Su Peticion esta siendo procesada, esto llevara un tiempo")
     await Vue.axios.post( `${apiUrl}/pdb`,data)
                    .then(response=>{commit('setResult', response.data)
                                      Vue.noty.info("Ya estan sus resultados")})
                    .catch((error)=>{showErrorWithNoty(error)});
    },
    async setViewA({commit}){ commit("setVA")},
    async setViewD({commit}){commit("setVD")},
    async setVisualizer({commit}){commit("setVisualizer")},
    async resetSearch({commit}){commit("resetResult")}

  },
})