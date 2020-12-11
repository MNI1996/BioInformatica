<template>

    <div class="row" v-if="result === null" >
      <clustal-viewer/>
    </div>


  <div v-else  >
    <div class="row welcome" >
      <h5>Resultados de {{result["id"]}}</h5>
    </div>
    <div class="row welcome">
     <h2>Secuencia:</h2>
      <h2 v-if="result!==null" >{{parseSeq(result["seq"])}}</h2>
    </div>
    <div class="row welcome">
        <iframe :src=generateURL() width="1200" height="600" ></iframe>
    </div>
    <div class ="row welcome ">
      <h3>Proteínas Homólogas: </h3>
        <div class="col" v-for="i in result['clustal']">
          <link-homologas :idP="i[0]" />
        </div>
    </div>
    <div class="row welcome ">
      <div class=" col col-md-6">
        <h3>Alineamientos con Homólogas</h3>
        <clustal-result :data="result['clustal']" />
      </div>
      <div class=" col col-md-6">
        <h3>Gráfico de conservación</h3>
        <d-s-s-p-viewer :id="result['id']" :number-of-graphs="result['numGraph']"/>
      </div>

    </div>

  </div>
</template>

<script>
import {mapGetters} from "vuex";
import JsMolViewer from "../components/JsMolViewer.vue";
import BlastViewer from "../components/BlastViewer.vue";
import ClustalViewer from "../components/ClustalPanel.vue";
import ClustalResult from "../components/ClustalResult.vue";
import DSSPViewer from "../components/DSSPViewer.vue";
import LinkHomologas from "../components/LinkHomologas.vue";

export default {
  name: "Home",
  components: {LinkHomologas, DSSPViewer, ClustalResult, ClustalViewer, BlastViewer, JsMolViewer},
  data() {
    return {
      codigo: "",
      codBase: "1UBQ",
      clustal_path: ""
    }
  },
  computed: {
    ...mapGetters(["result"])

  },
  mounted() {
    //this.changeBackground();
  },
  methods:{
    generateURL(){
      return "https://www.ncbi.nlm.nih.gov/Structure/icn3d/full.html?pdbid="+this.result["id"]
    },
    parseSeq(seq){
      var charperline=(seq.length/47)+1
      var cutvalue= seq.length/parseInt(charperline)
      var rsf=[]
      for (var i = 0; i < charperline; i++)
      {
        var res = seq.substring(parseInt(cutvalue)*i,parseInt(cutvalue)*(i+1));
        rsf+=res+"\n"
      }
      return rsf
    }

  }

}
</script>

<style scoped>
#margen div
{
  margin-top: 50px;
}




</style>