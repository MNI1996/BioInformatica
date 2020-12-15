<template>
  <div class="row ">
    <div class="col">
      <button class="btn btn-lg btn-success btn-block" @click="setV">Mostrar Estructura</button>
    </div>
    <div class="col">
      <button class="btn btn-lg btn-success btn-block" @click="setVA">Mostrar Alineamientos</button>
    </div>
    <div class="col">
      <button class="btn btn-lg btn-success btn-block" @click="setVD">Mostrar DSSP</button>
    </div>
    <div class="col">
      <a :href="generateDowloadLink('1UBQ_A')" class="btn-info btn btn-lg" :download="generateFileName('1UBQ_A','fa')">Descarga archivo Clustal</a>
    </div>
  </div>
</template>

<script>
export default {
name: "Botonera",
  methods:{
    setV(){this.$store.dispatch("setVisualizer")},
    setVA(){this.$store.dispatch("setViewA")},
    setVD(){this.$store.dispatch("setViewD")},
    generateDowloadLink(id){return "Files/"+id.slice(0,-2)+".fa"  },
    generateFileName(id,extension){return id.slice(0,-2)+"."+extension}
  }

}
</script>

<style scoped>

</style>