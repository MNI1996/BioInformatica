<template>
  <div class="text-center, row" id="margen">
    hi
  </div>
</template>

<script>


export default {
  name: "Home",
  computed:{

  },


  mounted(){
    this.changeBackground();
  },

  methods:{
    changeBackground(){
      var index=document.getElementById('body')
      index.style.cssText="background-color:#1aa6b7;background-image: url('Images/background tapestry.png');"
    }
  }
}
</script>

<style scoped>
#margen div
{
  margin-top: 50px;
}
</style>