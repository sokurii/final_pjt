<template>
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

</template>

<script>
// import {mapGetters} from 'vuex'
export default {
    name:'NavBar',
    data(){
        return{

        }
    },
    // methods:{
    //     logout(){
    //         this.$store.dispatch('logout')
    //     }
    // },
    // computed:{
    //     ...mapGetters(['isLoggedIn',]),
    //     loginState(){
    //         return (this.isLoggedIn) ? 'Logout' : 'Login'
    //     }
    // },
}
</script>

<style scoped>
    

    .navbar {
    display: flex;
    /* position : fixed; 여기 고정되게 ... 고민해보기 */
    justify-content: space-between;
    background-color: #F3F2E9;
    height: 90px;
    }

    .menu{
    display : flex;
    justify-content: center;
    align-items: center;
    gap:20px;
    padding-left: 200px;
    }

    .account{
    display:flex;
    gap:20px;
    padding-right: 200px;
    }

    /* .nav {
    padding: 30px;
    } */

</style>