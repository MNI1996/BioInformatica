<template>
<div>
  <div v-if="result!==null">
    <div class="row welcome" >
      <h5>Resultados de {{result["id"]}}</h5>
    </div>
    <botonera/>
    <div class="row welcome">
      <h2>Secuencia:</h2>
      <h2 v-if="result!==null" >{{parseSeq(result["seq"])}}</h2>
    </div>
    <div class="row welcome" v-if="visualizer">
      <js-mol-viewer :cod="generateURL()"/>
    </div>
    <div class ="row welcome " v-if="viewAlign">
      <h3>Proteínas Homólogas: </h3>
      <div class="col" v-for="i in result['clustal']">
        <link-homologas :idP="i[0]" />
      </div>
    </div>
    <div class="row welcome " v-if="viewAlign">
      <div class=" col col-md-6">
        <h3>Alineamientos con Homólogas</h3>
        <clustal-result :data="result['clustal']" />
      </div>
      <div class=" col col-md-6">
        <h3>Gráfico de conservación</h3>
        <d-s-s-p-viewer :id="result['id']" :number-of-graphs="result['numGraph']"/>
      </div>

    </div>
    <div class="row welcome" v-if="viewDssp">
      <clustal-result :data="result['dssp']"/>
    </div>
    <button class="btn btn-lg btn-success btn-block" @click="goToHome">Volver a Buscar</button>
  </div>
  <div v-else>
    <h2>Procesando...</h2>
  </div>
</div>
</template>

<script>
import {mapGetters} from "vuex";
import JsMolViewer from "../components/JsMolViewer.vue";
import BlastViewer from "../components/BlastViewer.vue";
import ClustalResult from "../components/ClustalResult.vue";
import DSSPViewer from "../components/DSSPViewer.vue";
import LinkHomologas from "../components/LinkHomologas.vue";
import Botonera from "../components/Botonera.vue";



export default {
name: "ResultPage",
  components: { LinkHomologas, DSSPViewer, ClustalResult, BlastViewer, JsMolViewer, Botonera},
  computed:{
    ...mapGetters(["result","viewAlign","viewDssp","visualizer"])
  },
  methods:{
    generateURL(){
      return "https://www.ncbi.nlm.nih.gov/Structure/icn3d/full.html?pdbid="+this.result["id"]
    },
    goToHome(){
      this.$router.push({name:"home"})
    }
  }

}
</script>

<style scoped>

</style>