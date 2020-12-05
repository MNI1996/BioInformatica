<template>
  <div class="row info">
    <div class="col-2" >
      <h2> {{data[0]}}</h2>
    </div>
    <div class="col-10">
      <p> {{parseSeq(data[1])}}</p>
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
    parseSeq(seq){
      var charperline=(seq.length/30)+1
      var cutvalue= seq.length/parseInt(charperline)
      var rsf=[]
      for (var i = 0; i < charperline; i++)
      {
        var res = seq.substring(parseInt(cutvalue)*i,parseInt(cutvalue)*(i+1));
        rsf+=res+"\n"
      }
      return rsf
    }
  }
}
</script>

<style scoped>

</style>