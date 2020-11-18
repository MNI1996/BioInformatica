<template>
  <div id="jsmolDiv" style="width: 600px; height:400px"></div>
</template>

<script>
var jmol = 'jmol';
var jme = 'jme';
var JmolInfo = {
  width: 600,
  height: 400,
  debug: false,
  color: 'black',
  use: 'HTML5',
  addSelectionOptions: true,
  disableJ2SLoadMonitor: true,
  disableInitialConsole: true,
  j2sPath: '/js/jsmol/j2s',
  //defaultModel: ":morphine",
  script: '',
};

var JMEInfo = {
  use: 'HTML5',
  visible: true,
  //divId: 'jmediv',
  options: 'autoez;nocanonize',
};
export default {
  name: "JsMolViewer",
  components: {},
     data(){return null},
     computed: {},
     methods: {},
     mounted() {
        this.$loadScript('/js/jsmol/JSmol.min.nojq.js').then(() => {
             this.$loadScript('/js/jsmol/js/JSmolJME.js').then(() => {
                 this.$loadScript('/js/JSME_2017-02-26/jsme/jsme.nocache.js').then(() => {
                     $('#jsmolDiv').html(Jmol.getAppletHtml('jmol',JmolInfo));
                          jme = Jmol.getJMEApplet('jme', JMEInfo, jmol);
                       });
                });
          });
     },
 }


}



</script>

<style scoped>

</style>