<template>
  <div class="row">
    <iframe :src=cod width="1200" height="600" ></iframe>
  </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
  props:{cod:""},
  computed:{
    ...mapGetters(["codMuestra","result"])
  },


}






</script>

<style scoped>

</style>