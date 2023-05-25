<template>
  <div>
    <div class="board-title d-flex flex-column justify-content-center">
      <img class="article-img" src="../assets/chat.png" alt="">
      <div><h1 class="board-title-text text-center"><strong>커뮤니티</strong></h1></div>
      <div><h5 class="text-center pt-3">나와 비슷한 관심사를 가진 사람들과 금융 정보를 공유해요</h5></div>
      <div><h5 class="text-center">자유롭게 소통하고, 소소한 금융 꿀팁도 알아가세요!</h5></div>
    </div>
    <ArticleList />
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList.vue'

export default {
  name: 'CommunityView',
  components: {
    ArticleList,
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch('getArticles')
      } else {
        alert('로그인이 필요한 서비스입니다!')
        this.$router.push({ name: 'login' })
      }
    }
  }
}
</script>

<style>
.article-img {
  position: absolute;
  top: 45%;
  left: 50%;
  transform: translate(-50%, -50%);
  width:650px;
  object-fit: cover;
  opacity: 0.5;
  z-index: -1;
}

</style>
