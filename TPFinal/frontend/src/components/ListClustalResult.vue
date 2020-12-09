<template>
  <div class="row info">
    <div class="col-2" >
      <a :href=url() >
        <h6>
          {{data[0]}}
        </h6>
        </a>
    </div>
    <div class="col-10">
      <h6> {{parseSeq(data[1], data[0])}}</h6>
    </div>
  </div>
</template>

<script>
export default {
name: "ListClustalResult",
  props:{
    data:null
  },
  methods:{
  /*  parseSeq(seq, id){
      var charperline=(seq.length/60)+1
      var cutvalue= seq.length/parseInt(charperline)
      var rsf=[]
      var tuplas = []
      for (var i = 0; i < charperline; i++)
      {
        var res = seq.substring(parseInt(cutvalue)*i,parseInt(cutvalue)*(i+1));
        rsf+=res+"\n"
      }
      //return rsf
      tuplas.append(id,rsf)

    },*/
    url(){
      return "https://www.rcsb.org/structure/"+this.data[0]
    },


  }
}
</script>

<style scoped>

</style>