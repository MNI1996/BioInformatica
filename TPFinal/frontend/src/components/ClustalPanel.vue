<template>
  <div  class=" welcome">
    <div class="row">
      <div class="col">
        <label >
          <h5> Ingrese codigo de proteina</h5>
          <input type="text" v-model="id" class="input-group"/>
        </label>
      </div>
      <div class="col">
        <label >
          <h5> Ingrese la cadena deseada</h5>
          <input type="text" v-model="chain" class="input-group"/>
        </label>
      </div>
    </div>
    <div class="row">
      <div class="col col-md-4">
        <label>
          <h5>Ingrese la ruta de su clustal (*)</h5>
          <input type="text" v-model="clustal_path" class="input-group"  />
        </label>
      </div>
      <div class="col col-md-4">
        <h5> Defina word size</h5>
          <select name="word_size" v-model="word_size">
            <option selected value="3">3</option>
            <option value="6">6</option>
            <option value="12">12</option>
          </select>
      </div>
      <div class="col col-md-4">
        <h5>Defina nro de muestras</h5>
        <label>
          <select name="num_align" v-model="num_align">
            <option selected value="5">5</option>
            <option value="10">10</option>
            <option value="15">15</option>
          </select>
        </label>
      </div>
    </div>
    <div class="row">
      <div class="col col-md-4">
        <label >
          <h5>Ingrese un e-value</h5>
          <input type="text" v-model="e_value" class="input-group"/>
        </label>
      </div>
      <div class="col col-md-4">
        <label >
          <h5> Ingrese penalidad de gaps</h5>

          <input type="text" v-model="gapopen" class="input-group"/>
        </label>
      </div>
      <div class="col col-md-4">
        <label >
         <h5> Ingrese % de identidad minimo deseado</h5>
          <input type="text" v-model="identity" class="input-group"/>
        </label>
      </div>
    </div>
    <div class="row">
      <div class="col-md-4">

        <button @click="search" class="btn btn-lg btn-success btn-block">Buscar</button>
      </div>
    </div>
    <div class="row">
      <h5>(*) La ruta estandar suele ser C:\\Program Files (x86)\\ClustalW2\\clustalw2</h5>
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
      clustal_path: "C:\\Program Files (x86)\\ClustalW2\\clustalw2",
      id: "",
      chain: "A",
      identity: 39.9,
      num_align: "5",
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
        num_align: this.num_align,
        e_value: this.e_value,
        db: this.db,
        word_size: this.word_size,
        gapopen:this.gapopen
      }
      this.$store.dispatch("search", data)
      this.$router.push({name: "result"})

    },
    defaultClustal(){
      return "C:\\Program Files (x86)\\ClustalW2\\clustalw2"
    }
  }

}
</script>

<style scoped>

</style>