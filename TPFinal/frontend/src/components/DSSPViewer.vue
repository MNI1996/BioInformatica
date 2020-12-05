<template>
  <div>
    <img src="Images/res.png" alt="">
  </div>
</template>

<script>
import {SvgMsa} from 'vue-svg-msa'
import 'vue-svg-msa/dist/vue-svg-msa.css'
/*var opts = {
  el: document.getElementById("result"),
  vis: {
    conserv: false,
    overviewbox: false
  },
// smaller menu for JSBin
  menu: "small",
  bootstrapMenu: true
};

var m = new msa.msa(opts);
m.u.file.importURL("file:///C:/Users/pc/Desktop/Facu/Bioinformatica/BioInformatica/TPFinal/backend/clustal/out_clustal_file.fa", function(){
  m.render();
});*/
export default {
name: "DSSPViewer",
  date(){
    return{
      seqs:[{
        seq: 'ATCATCATCATCATCATACTCATTTTTACAT---CATCATACTACATCATCATATACTCATTTTTACATCATC-TCTT',
        id: 'seqid1',
        name: 'sequence1',
        color: 'red'
      }]
    }
  }
}

</script>

<style scoped>

</style>