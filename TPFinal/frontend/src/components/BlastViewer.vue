<template>
  <div>
    <div v-for="p in blast">
      <blast-result  :data= p />
    </div>
  </div>


</template>

<script>
import BlastResult from "./BlastResult.vue";
export default {
  name: "BlastViewer",
  components: {BlastResult},
  props:{
    blast:null
  },
  methods:{
    sinGaps(i){
      var p2 = i[1].replaceAll("-"," ").trim()
      var par=(i[0],p2)
      return par
    }
  }
}
</script>

<style scoped>

</style>