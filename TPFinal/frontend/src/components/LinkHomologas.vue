<template>
<div class="col">
  <a  style="font-size: 30px" :href=url(idP) target="_blank"> {{idP}}</a>
</div>
</template>

<script>
export default {
name: "LinkHomologas",
  props:{
    idP:""
  },
  methods:{
    url(){
      return "https://www.rcsb.org/structure/"+this.idP.slice(0,-2)
    }
  }
}
</script>

<style scoped>

</style>