<template>
  <div>
      <!--<list-clustal-result v-for="i in data" :data=i /> -->
      <p>{{listHomologas(data)}}</p>

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
            /*listTuplas(tuplas) {
                var tuplasSalt = [];
                for (var i = 0; i < tuplas.length; i++) {
                    var rst = {
                        id: tuplas[i][0],
                        seqs: this.parseSeq(tuplas[i][1])
                    };
                    tuplasSalt.push(rst)
                }
                return tuplasSalt;
            },*/

            listHomologas(tuplas) {
                var listFinal = [];
                for (var i = 0; i < tuplas.length; i++) {
                    var listReturn = []
                    var id = tuplas[i][0];
                    var res = this.parseSeq(tuplas[i][1]);

                    for (var j = 0; j < res.length; j++) {
                        var par = (id, res[j]);
                        listReturn.push(par);
                    }
                    listFinal.push(listReturn)
                }
                return(this.transposedMatrix(listFinal))

                //Falta transponer listFinal y retornarla


            },


            transposedMatrix(lists){
                resList = [];
                for(var i = 0; i < lists.length; i++){
                    auxList = [];
                    for(list in lists){
                        elem = list[i];
                        auxList.push(elem);
                    }
                    resList.push(auxList);
                }
                return resList;
            }
        }
    }

             //const tuplaList = this.listTuplas(tuplas);
             /*console.log(tuplaList)
             var listEnd = [];
             for (var i= 0; i< tuplaList.length; i++) {
                 //console.log("estoy en el for i")
                 for (var j = 0; j < tuplaList.length; j++) {
                     //console.log("estoy en el for de j")
                     var rst = (
                                tuplaList[0][j],
                                tuplaList[1][i]
                     );
                     console.log(rst[0])
                     listEnd.push(rst)
                     //console.log(rst)
                 }
             }
             return listEnd */
             //console.log(listEnd)

             //[(10, [1,2]), (20, [3,4]), (30, [5,6])
             //[[(10, 1),(20,3), 30, 5)] [(10, 2), (20,4), (30,6)]]


                    //[(10, [1,2]), (20, [3,4]), (30, [5,6])
                    //i = 0 => id = 10
                    //         res = [1,2]
                    //    j = 0 => par = (10, 1)
                    //             listReturn = [(10,1)]
                    //    j = 1 => par = (10, 2)
                    //              listReturn = [(10,1), (10,2)]
                    //              listFinal.[[(10,1), (10,2)]]

                    //i = 1 => id = 20
                    //         res = [3,4]
                    //          listReturn = []
                    //      j = 0 => par = (20, 3)
                    //              listReturn = [(20,3)]
                    //      j = 1 => par = (20,4)
                    //              listReturn = [(20,3), (20,4)]
                    //              listFinal = [[(10,1), (10,2)], [(20,3), (20,4)]]

                    //i = 2 => id = 30
                    //         res = [5,6]
                    //      j = 0 => par = (30, 5)
                    //              listReturn = [(30,5)]
                    //      j = 1 => par = (30,6)
                    //              listReturn = [(30,5), (30,6)]
                    //              listFinal = [[(10,1), (10,2)], [(20,3), (20,4)], [(30,5), (30,6)]]


             //[[(10, 1),(20,3), (30, 5)] [(10, 2), (20,4), (30,6)]]

</script>




    }

<style scoped>

</style>