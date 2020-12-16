<template>
  <div>
    <div v-for="i in numberOfGraphs">
      <img style="margin-top:130px; width: 100%" :src=urlImage(i-1) alt="">
    </div>
  </div>
</template>

<script>
import {mapGetters} from "vuex";
export default {
  name: "AlignViewer",
  props:{
    id:"",
    numberOfGraphs:0
  },
  computed:{
    ...mapGetters(["result"])
  },
  methods:{
    urlImage(n){
      return "Images/"+this.result["id"].slice(0,-2)+"/Align/"+n+".png"
    }
  }
}

</script>

<style scoped>

</style>