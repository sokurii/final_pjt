<template>
  <nav class = 'navbar'>
      <div class='menu'>       
        <router-link :to="{ name: 'home' }">
            <img src="./assets/mmop.png" alt="" style="max-width:150px">
        </router-link>
        <router-link :to="{ name: 'home' }">홈</router-link>
        <router-link @click.native="goToLogin" to="/finance">금융상품비교</router-link>
        <router-link @click.native="goToLogin" to="/exchange">환율</router-link>
        <router-link @click.native="goToLogin" to="/map">지도</router-link> 
        <router-link to="/community">게시판</router-link>
        <!-- <div>
          <a href="#" @click="goToFinance">금융상품비교</a>  |
          <a href="#" @click="goToExchange">환율</a>  |
          <a href="#" @click="goToMap">지도</a>  |
          <a href="#" @click="goToCommunity">게시판</a>
        </div> -->
      </div>
      <div class='account'>
        <span v-if="!isLogin">
          <router-link to="/login">로그인</router-link> |
          <router-link :to="{ name: 'signup' }">회원가입</router-link>
        </span>
        <span v-if="isLogin">
          <a href="" @click="logout">로그아웃</a> |
          <router-link :to="{ name: 'profile' }">프로필</router-link>
        </span>
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
    computed: {
      isLogin() {
        return this.$store.getters.isLogin;
      },
    },
    methods: {
      logout() {
        this.$store.commit('SAVE_TOKEN', null) // 토큰을 null로 설정하여 로그아웃 처리
        alert('로그아웃 되었습니다!')
        this.$router.push({ name: 'login' }) // 로그인 페이지로 이동
      },

      goToLogin() {
        if (!this.isLogin) {
          alert('로그인이 필요한 서비스입니다.')
          this.$router.push({ name: 'login' })
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
    },
}
</script>

<style>
    

    .navbar {
    display: flex;
    justify-content: space-between;
    background-color: #F3F2E9;
    width: 100%;
    height: 120px;
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

    .logout {
    font-weight: bold;
    color: black;
    text-decoration: none;
    }

    /* .nav {
    padding: 30px;
    } */

</style>