<template>

  <div class="text-center" id="margen" v-if="result === null">
    <div class="row">
      <label style="color: aliceblue">
        Ingrese codigo de proteina
        <input type="text" v-model="codigo" class="input-group"/>
      </label>
      <button @click="search" class="btn btn-lg btn-success">Buscar</button>
    </div>
    <div class="row">
      <js-mol-viewer :cod= codBase />
    </div>0
  </div>

  <div v-else style="color: aliceblue">
    <div class="row">
      <h1>Resultados de {{codigo}}</h1>
    </div>
    <div class="row">
        <h2>Secuencia:</h2>
    </div>
    <div class="row">
      <h5>{{result["seq"]}}</h5>
    </div>
    <div class="row">
      <!-- las analogas v-for -->
    </div>
    <div class="row">
      <div class="col">
        <js-mol-viewer :cod=this.result["id"] />
      </div>
      <div class="col">

      </div>
    </div>
    <div class="row">
      <div class="col">

      </div>
      <div class="col">

      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import JsMolViewer from "../components/JsMolViewer.vue";

export default {
  name: "Home",
  components: {JsMolViewer},
  data(){
    return{
      codigo:"",
      codBase:"1UBQ",
      rutaC:""
    }
  },
  computed:{
    ...mapGetters(["result"])

  },


  mounted(){
    //this.changeBackground();
  },

  methods:{
    search(){
      let data={
        id:this.codigo,
        rutaC:this.rutaC
      }
      this.$store.dispatch("search", this.codigo)
    },

    changeBackground(){
      var index=document.getElementById('body')
      index.style.cssText="background-color:#1aa6b7;background-image: url('Images/background tapestry.png');"
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