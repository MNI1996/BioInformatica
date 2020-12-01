<template>
<div>
  <div class="row">
    <iframe src="https://www.ncbi.nlm.nih.gov/Structure/icn3d/full.html?pdbid=1ubq" width="1200" height="600" ></iframe>
  </div>
  <div class="row">
    <iframe src="https://2struccompare.cryst.bbk.ac.uk/index.php" width="1000" height="600"></iframe>
    <div class="col">
      <div style="height: 400px; width: 400px; position: relative;" class='viewer_3Dmoljs' :data-pdb=cod data-backgroundcolor='0xffffff' data-style='cartoon' data-surface="opacity:0.8"></div>
    </div>
  </div>
</div>
</template>

<script>
import {mapGetters} from "vuex";
/* source code :https://github.com/ncbi/icn3d*/
export default {
  props:{
    cod:""
  },
  computed:{
    ...mapGetters(["codMuestra"])
  }
 }






</script>

<style scoped>

</style>