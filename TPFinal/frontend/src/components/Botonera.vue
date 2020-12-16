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
      <a :href="generateDowloadLinkA(result['id'],'txt')" class="btn-info btn btn-lg" :download="generateFileName(result['id'],'txt')">Descarga archivo Clustal</a>
    </div>
    <div class="col">
      <a :href="generateDowloadLinkS(result['id'],'fa')" class="btn-info btn btn-lg" style="font-size: 20px" :download="generateFileName(result['id'],'fa')">Descarga archivo de DSSP</a>
    </div>
    </div>
</template>

<script>
import {mapGetters} from "vuex";

export default {
name: "Botonera",
  computed:{...mapGetters(["result"])},
  methods:{
    setV(){this.$store.dispatch("setVisualizer")},
    setVA(){this.$store.dispatch("setViewA")},
    setVD(){this.$store.dispatch("setViewD")},
    generateDowloadLinkA(id,extension){return "Files/Align/"+id.slice(0,-2)+"."+extension  },
    generateDowloadLinkS(id,extension){return "Files/Dssp/"+id.slice(0,-2)+"."+extension  },
    generateFileName(id,extension){return id.slice(0,-2)+"."+extension}
  }

}
</script>

<style scoped>

</style>