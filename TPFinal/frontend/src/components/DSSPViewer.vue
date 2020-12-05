<template>
  <div>
    <img :src=urlImage() alt="">
  </div>
</template>

<script>
import {mapGetters} from "vuex";
export default {
name: "DSSPViewer",
  computed:{
    ...mapGetters(["result"])
  },
  methods:{
  urlImage(){
    return "Images/dssp/"+this.result["id"]+".png"
  }
  }
}

</script>

<style scoped>

</style>