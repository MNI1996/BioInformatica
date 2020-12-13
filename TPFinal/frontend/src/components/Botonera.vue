<template>
  <div class="row ">
    <div class="col">
      <button class="btn btn-lg btn-success btn-block" @click="setV">Mostrar Estructura</button>
    </div>
    <div class="col">
      <button class="btn btn-lg btn-success btn-block" @click="setVA">Mostrar Alineamientos</button>
    </div>
    <div class="col">
      <button class="btn btn-lg btn-success btn-block" @click="setVD">Mostrar Dssp</button>
    </div>
  </div>
</template>

<script>
export default {
name: "Botonera",
  methods:{
    setV(){this.$store.dispatch("setVisualizer")},
    setVA(){this.$store.dispatch("setViewA")},
    setVD(){this.$store.dispatch("setViewD")}
  }

}
</script>

<style scoped>

</style>