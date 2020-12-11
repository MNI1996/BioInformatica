<template>
  <div>
    <div v-for= "ls in listHomologas(data)">
      <list-clustal-result :data="ls" />
    </div>
  </div>

</template>

<script>
    import {mapGetters} from "vuex";
    import ListClustalResult from "./ListClustalResult.vue";
    export default {
        name: "ClustalResult",
        components: {ListClustalResult},
        computed: {
            ...mapGetters(["result"])
        },
        props: {
            data: null
        },
        methods: {
            parseSeq(seq) {
                var charperline = (seq.length / 30) + 1
                var cutvalue = seq.length / parseInt(charperline)
                var rsf = []

                for (var i = 0; i < charperline; i++) {
                    var res = seq.substring(parseInt(cutvalue) * i, parseInt(cutvalue) * (i + 1));
                    rsf.push(res)
                }
                return rsf


            },

            listHomologas(tuplas) {
                var listFinal = [];
                for (var i = 0; i < tuplas.length; i++) {
                    var listReturn = []
                    var id = tuplas[i][0];
                    var res = this.parseSeq(tuplas[i][1]);


                    for (var j = 0; j < res.length; j++) {
                        var par ={id:id, res:res[j]};
                        listReturn.push(par);
                    }
                    listFinal.push(listReturn)
                }
                var al_return=this.transposedMatrix(listFinal)
                return(al_return)


            },
            transposedMatrix(lists){
                var resList = [];
                for(var i = 0; i < lists[0].length; i++){
                    var auxList = [];
                    for(var j=0;j< lists.length;j++){
                        var elem = lists[j][i];
                        auxList.push(elem);
                    }
                    resList.push(auxList);
                }
                return resList;
            }
        }
    }



</script>






<style scoped>

</style>