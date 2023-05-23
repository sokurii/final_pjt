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
    name: 'App',
    components: {
      NavBar,
      FootBar,
    },
  };
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #000000;
  /* background-color: #F3F2E9; */
  position: relative;
  min-height: 100vh;
  /* height: 100vh; */
  display: flex;
  flex-direction: column;
}

router-view {
  flex-grow: 1;
}

nav a {
  font-weight: bold;
  color: black;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #e98f1a;
}
</style>
