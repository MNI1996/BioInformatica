<template>
<div>
  <div class="row">
    <iframe src="https://www.ncbi.nlm.nih.gov/Structure/icn3d/full.html?pdbid=1ubq" width="1200" height="600" style="border-color: aquamarine ;" ></iframe>
  </div>
  <div class="row">

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