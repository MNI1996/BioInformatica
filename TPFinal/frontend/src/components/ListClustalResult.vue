<template>
  <div class="row">
    <div class="col">
      <H2> {{data[0]}}</H2>
    </div>
    <div class="col">
      <h2> {{data[1]}}</h2>
    </div>
  </div>

</template>

<script>
export default {
name: "ListClustalResult",
  props:{
    data:null
  }
}
</script>

<style scoped>

</style>