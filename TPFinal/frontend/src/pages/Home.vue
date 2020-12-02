<template>

    <div class="row" v-if="result === null" >
      <clustal-viewer/>
      <div style="height: 400px; width: 400px; position: relative;" class='viewer_3Dmoljs' data-pdb='1UBQ' data-backgroundcolor='0xffffff' data-style='cartoon' data-surface="opacity:0.8"></div>

    </div>


  <div v-else class="welcome" >
    <div class="row">
      <h5>Resultados de {{result["id"]}}</h5>
    </div>
    <div class="row">
        <h2>Secuencia:</h2>
    </div>
    <div class="row">
      <h5 v-if="result!==null">{{result["seq"]}}</h5>
    </div>
    <div class="row">
      <div class="col">
        <js-mol-viewer :cod=codigo />
      </div>
      <div class="col">
        <blast-viewer/>
      </div>
    </div>

  </div>
</template>

<script>
import {mapGetters} from "vuex";
import JsMolViewer from "../components/JsMolViewer.vue";
import BlastViewer from "../components/BlastViewer.vue";
import ClustalViewer from "../components/ClustalPanel.vue";

export default {
  name: "Home",
  components: {ClustalViewer, BlastViewer, JsMolViewer},
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