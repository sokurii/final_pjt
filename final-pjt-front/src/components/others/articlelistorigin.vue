<template>
  <div id="container" class="bg-white">
    <!-- <h3 v-if="noArticles">생성된 게시글이 없습니다.</h3> -->
    <h1 class="p-3">게시글 목록</h1>
    <router-link :to="{ name: 'CreateArticle' }" class="btn btn-primary">게시글 작성하기</router-link>
    
      
    <ArticleListItem 
      v-for="article in articles"
      :key="article.id"
      :article="article"
    />

  </div>
</template>

<script>
import ArticleListItem from './ArticleListItem.vue'
export default {
  name: 'ArticleList',
  components: {
    ArticleListItem,
  },

  computed: {
    articles() {
      return this.$store.state.articles
    },
    noArticles() {
      return this.$store.state.articles && this.$store.state.articles.length === 0
    },
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      this.$store.dispatch('getArticles')
    }
  }
}
</script>

<style>

</style>