<template>
  <div style="height: 400px; width: 400px; position: relative;" class='viewer_3Dmoljs' :data-pdb=cod data-backgroundcolor='0xffffff' data-style='cartoon'></div>
</template>

<script>
import {mapGetters} from "vuex";
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