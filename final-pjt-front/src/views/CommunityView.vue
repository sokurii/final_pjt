<template>
  <div>
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

</style>
