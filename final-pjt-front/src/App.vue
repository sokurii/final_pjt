<template>
  <div id="app">
    <nav-bar></nav-bar>
    <router-view></router-view>
    <foot-bar></foot-bar>
  </div>
</template>

<script>
  import NavBar from './NavBar.vue';
  import FootBar from './FootBar.vue';

  export default {
    name:'App',
    components :{
      NavBar,
      FootBar,
    }
    }
  
</script>

<style>
/* #app {
  text-align: center;
  color: #000000;
  position: relative;
  min-height: 100vh;
  height: 100vh;
  flex-grow: 1;
} */

/* .content {
  * padding-bottom: 60px;  FootBar의 높이와 같은 값으로 설정 
} */




</style>
