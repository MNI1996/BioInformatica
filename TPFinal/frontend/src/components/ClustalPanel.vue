<template>
  <div  class=" welcome">
    <div class="row">
      <label >
       <p> Ingrese codigo de proteina</p>
        <input type="text" v-model="id" class="input-group"/>
      </label>
    </div>
    <div class="row">
      <div class="col col-md-4">
        <label>
          <p>Ingrese la ruta de su clustal</p>
          <input type="text" v-model="clustal_path" class="input-group"/>
        </label>
      </div>
      <div class="col col-md-4">
        <p> Defina word size</p>
          <select name="word_size" v-model="word_size">
            <option selected value="3">default</option>
            <option value="6">6</option>
            <option value="12">12</option>
          </select>
      </div>
      <div class="col col-md-4">
        <p>Defina nro de muestras</p>
        <select name="num_align" v-model="num_align">
          <option selected value="5">default</option>
          <option value="10">10</option>
          <option value="15">15</option>
        </select>
      </div>
    </div>
    <div class="row">
      <div class="col col-md-4">
        <label >
          <p>Ingrese un e-value</p>
          <input type="text" v-model="e_value" class="input-group"/>
        </label>
      </div>
      <div class="col col-md-4">
        <label >
          <p> Ingrese penalidad de gaps</p>

          <input type="text" v-model="gapopen" class="input-group"/>
        </label>
      </div>
      <div class="col col-md-4">
        <label >
         <p> Ingrese % de identidad minimo deseado</p>
          <input type="text" v-model="identity" class="input-group"/>
        </label>
      </div>
    </div>
    <div class="row">
      <div class="col-md-4">

        <button @click="search" class="btn btn-lg btn-success btn-block">Buscar</button>
      </div>
    </div>
  </div>

</template>

<script>
import {mapGetters} from "vuex";
export default {
name: "ClustalPanel",
  computed:{
  ...mapGetters(["resultSeq"])
  },
  data(){
    return{
      clustal_path: "",
      id: "",
      chain: "A",
      identity: 39.9,
      num_align: 5,
      e_value: 0.001,
      db: "pdb",
      word_size: 3,
      gapopen:11
    }
  },
  methods:{
    search(){
      let data={
        clustal_path: this.clustal_path,
        id: this.id,
        chain: this.chain,
        identity: this.identity,
        num_align: this.identity,
        e_value: this.e_value,
        db: this.db,
        word_size: this.word_size,
        gapopen:this.gapopen
      }
      this.$store.dispatch("search", data)
    },
  }

}
</script>

<style scoped>

</style>