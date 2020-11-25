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
    async search({commit},id){
      Vue.noty.success("Su Peticion esta siendo procesada, esto llevara un tiempo")
     await Vue.axios.get( `${apiUrl}/pdb?id=${id}`)
                    .then(response=>{commit('setResult', response.data)
                                      Vue.noty.info("Ya estan sus resultados")})
                    .catch(()=>{Vue.noty.error("No se encuentra el codigo")});
    },

  },
})