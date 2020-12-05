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
      <h6 v-if="result!==null" >{{parseSeq(result["seq"])}}</h6>
    </div>
    <div class="row welcome">
        <iframe :src=generateURL() width="1200" height="600" ></iframe>
    </div>
    <div class="row">
      <d-s-s-p-viewer/>
    </div>
    <div class=" welcome ">
        <h3>Alineamientos con Homologas</h3>
        <clustal-result :data="result['clustal']" />
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

export default {
  name: "Home",
  components: {DSSPViewer, ClustalResult, ClustalViewer, BlastViewer, JsMolViewer},
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



/**
> Here's the app:
>
> <template>
>         <div id="jsmolDiv" style="width: 600px; height:400px"></div>
> </template>
>
> <script>
> var jmol = 'jmol';
> var jme = 'jme';
>
> var JmolInfo = {
>     width: 600,
>     height: 400,
>     debug: false,
>     color: 'black',
>     use: 'HTML5',
>     addSelectionOptions: true,
>     disableJ2SLoadMonitor: true,
>     disableInitialConsole: true,
>     j2sPath: '/js/jsmol/j2s',
>     //defaultModel: ":morphine",
>     script: '',
> };
>
> var JMEInfo = {
>     use: 'HTML5',
>     visible: true,
>     //divId: 'jmediv',
>     options: 'autoez;nocanonize',
> };
>
> export default {
>     components: {},
>     data: () => ({}),
>     computed: {},
>     methods: {},
>     mounted: function() {
>         this.$loadScript('/js/jsmol/JSmol.min.nojq.js').then(() => {
>             this.$loadScript('/js/jsmol/js/JSmolJME.js').then(() => {
>                 this.$loadScript(
>                     '/js/JSME_2017-02-26/jsme/jsme.nocache.js'
>                 ).then(() => {
>                     $('#jsmolDiv').html(Jmol.getAppletHtml('jmol',
> JmolInfo));
>                     jme = Jmol.getJMEApplet('jme', JMEInfo, jmol);
>                 });
>             });
>         });
>     },
> };
> </script>
*/
</style>