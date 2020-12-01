<template>
  <div class="container-fluid">
    <div class="row" style="background-color:#150485 ;">
      <div class="col-8">
        <h1 >Analizer</h1>
      </div>
    </div>
        <!-- use router-link component for navigation. -->
        <!-- specify the link by passing the `to` prop. -->
        <!-- `<router-link>` will be rendered as an `<a>` tag by default -->

        <!--<router-link :to="{name: 'rooms'}">Go to Rooms</router-link>-->


      <!-- route outlet -->
      <!-- component matched by the route will render here -->
      <router-view></router-view>
  </div>
</template>

<script>


export default {
  name: "App",
  computed:{

  }
}
</script>