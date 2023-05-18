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
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #000000;
  background-color: #F3F2E9;
  position: relative;
  min-height: 100vh;
  height: 100vh;
}

.content {
  padding-bottom: 60px; /* FootBar의 높이와 같은 값으로 설정 */
}

/* 
.navbar {
  display: flex;
  justify-content: space-between;
  background-color: #F3F2E9;
  height: 90px;
} */

/* .menu{
  display : flex;
  justify-content: center;
  align-items: center;
  gap:20px;
  padding-left: 200px;
} */

/* .account{
  display:flex;
  gap:20px;
  padding-right: 200px;
} */

/* nav {
  padding: 30px;
} */

nav a {
  font-weight: bold;
  color: black;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #e98f1a;
}



/* @media (max-width:768px) {
    footer {
        font-size: 0.5rem;
    }
} */
</style>
