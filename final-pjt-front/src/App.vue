<template>
  <div id="app">
    <nav class = 'navbar'>
      <div class='menu'>       
        <router-link to="/">
          <img src="./assets/mmop.png" alt="" style="max-width:150px">
        </router-link>
        <router-link to="/">홈</router-link> 
        <router-link to="/finance">금융상품비교</router-link> 
        <router-link to="/map">지도</router-link> 
        <router-link to="/community">게시판</router-link>
      </div>
      <div class='account'>
        <router-link to="/login">로그인</router-link>
        <router-link to="/profile">프로필</router-link> 
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
  color: #000000;
  background-color: #F3F2E9;
  
}

.navbar {
  display: flex;
  justify-content: space-between;
  background-color: #F3F2E9;
  height: 90px;
}

.menu{
  display : flex;
  justify-content: center;
  align-items: center;
  /* justify-content: space-between; */
  gap:20px;
  padding-left: 200px;
}

.account{
  display:flex;
  gap:20px;
  padding-right: 200px;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: black;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #e98f1a;
}

footer {
  position : fixed;
  left:0;
  bottom: 0;
  width: 100%;
  padding: 10px;
  color: white;
  background-color: #6d6b6b;
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
