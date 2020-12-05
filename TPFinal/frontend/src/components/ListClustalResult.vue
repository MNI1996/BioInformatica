<template>
  <div class="row info">
    <div class="col-2" >
      <a :href=url() >
        <h2>
          {{data[0]}}
        </h2>
        </a>
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
    },
    url(){
      return "https://www.rcsb.org/structure/"+this.data[0]
    }
  }
}
</script>

<style scoped>

</style>