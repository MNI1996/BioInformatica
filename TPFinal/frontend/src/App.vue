<template>
  <div class="container-fluid">
    <div class="row" style="background-color:#150485 ;">
      <div class="col-2">
        <router-link :to="{name: 'home'}">
          <img src="Images/Logo.png" alt="Brainy" style="width: 100px;height: 75px;" class="img-fluid">
        </router-link>
      </div>

      <div class="col-8">
        <h1 >Analizer</h1>
      </div>

      <div class="col-1">
        <router-link :to="{name: 'ranking'}" v-if="logged">
          <button class="btn btn-lg btn-success btn-block"><img src="Images/rank.png" alt="" class="img-fluid" style="height: 40px;width: 60px"></button>
        </router-link>
      </div>

      <div class="col-1">
        <router-link :to="{name: 'profile'}" v-if="logged">
          <img src="Images/Profile.png" alt="" style="height: 50px;width: 65px" class="img-fluid">
        </router-link>
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