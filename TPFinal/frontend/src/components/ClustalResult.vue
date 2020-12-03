<template>
  <div>
    <div class="row " v-for="i in data">
      <list-clustal-result :data=i />
    </div>

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