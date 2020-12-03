<template>
  <div class="row info">
    <div class="col">
      <h3> {{data[0]}}</h3>
    </div>
    <div class="col">
      <p> {{data[1].replaceAll('-',' ').trim()}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "BlastResult",
  props:{
    data:null
  }
}
</script>

<style scoped>

</style>