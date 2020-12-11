<template>
<div class="col">
  <a  style="font-size: 30px" :href=url(idP)> {{idP}}</a>
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
      return "https://www.rcsb.org/structure/"+this.idP
    }
  }
}
</script>

<style scoped>

</style>