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

  }
}
</script>

<style scoped>

</style>