<template>
  <div>
      <list-clustal-result v-for="i in data" :data=i />
  </div>
</template>

<script>
import {mapGetters} from "vuex";
import ListClustalResult from "./ListClustalResult.vue";
export default {
name: "ClustalResult",
  components: {ListClustalResult},
  computed:{
  ...mapGetters(["result"])
  },
  props:{
    data:null
  }


}
</script>

<style scoped>

</style>