<template>
  <div class="row info alineamientos" >
    <p class="alineamientos" v-for="i in data "> {{parseBlock(i)}}<br> </p>
  </div>
</template>

<script>
export default {
name: "ListClustalResult",
  props:{
    data:null
  },
  methods:{
  parseBlock(block){
    return block['id']+": "+block["res"]+"\n" ;
  },



  }
}
</script>

<style scoped>

</style>