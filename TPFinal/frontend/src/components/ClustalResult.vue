<template>
  <div>
    <ul>
      <list-clustal-result v-for="i in result['clustal']"/>
    </ul>
  </div>

</template>

<script>
import {mapGetters} from "vuex";
import ListClustalResult from "./ListClustalResult";
export default {
name: "ClustalResult",
  components: {ListClustalResult},
  computed:{
  ...mapGetters(["result"])
  },


}
</script>

<style scoped>

</style>