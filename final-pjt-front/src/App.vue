<template>
  <div id="app">
    <nav>
      <div class='menu'>
        <router-link to="/">홈</router-link> |
        <router-link to="/finance">금융상품비교</router-link> |
        <router-link to="/map">지도</router-link> |
        <router-link to="/community">게시판</router-link>
      </div>
      <div class='account'>
        <router-link to="/profile">프로필</router-link> |
        <router-link to="/login">로그인</router-link>
      </div>
    </nav>
    <router-view/>
    <footer id="a" class="b">
      &copy; 2023. Lee Jin Hyeong, Park Jin Hee. All right reserved.
    </footer>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

footer {
  padding: 10px;
  color: white;
  background-color: black;
  display: flex;
  justify-content: center;
  align-content: center;
  font-size: 1rem;
}

@media (max-width:768px) {
    footer {
        font-size: 0.5rem;
    }
}
</style>
