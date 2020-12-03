<template>
  <div>
    <div v-for="p in blast">
      <list-clustal-result  :data=p />
    </div>
  </div>


</template>

<script>
import ListClustalResult from "./ListClustalResult.vue";
export default {
  name: "BlastViewer",
  components: {ListClustalResult},
  props:{
    blast:null
  }
}
</script>

<style scoped>

</style>