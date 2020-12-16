<template>
    <div class="row" v-if="result ===null" >
      <clustal-viewer/>
    </div>
</template>

<script>
import {mapGetters} from "vuex";
import ClustalViewer from "../components/ClustalPanel.vue";
import Botonera from "../components/Botonera.vue";

export default {
  name: "Home",
  components: {Botonera, ClustalViewer},
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

  methods:{

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