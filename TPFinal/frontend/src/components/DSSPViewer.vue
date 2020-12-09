<template>
  <div>
    <div v-for="i in numberOfGraphs">
      <img :src=urlImage(i) alt="">
    </div>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
export default {
name: "DSSPViewer",
  props:{
    id:"",
    numberOfGraphs:0
  },
  computed:{
    ...mapGetters(["result"])
  },
  methods:{
  urlImage(n){
    return "Images/dssp/"+this.result["id"]+"/"+n+".png"
  }
  }
}

</script>

<style scoped>

</style>