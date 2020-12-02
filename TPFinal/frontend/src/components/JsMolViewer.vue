<template>
  <div class="row">
    <div style="height: 400px; width: 400px; position: relative;" class='viewer_3Dmoljs' :data-pdb=cod data-backgroundcolor='0xffffff' data-style='cartoon' data-surface="opacity:0.8"></div>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
/* source code :https://github.com/ncbi/icn3d*/
export default {
  props:{cod:""},
  computed:{
    ...mapGetters(["codMuestra","result"])
  },

}






</script>

<style scoped>

</style>