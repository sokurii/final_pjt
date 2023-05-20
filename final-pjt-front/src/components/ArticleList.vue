<template>
  <div>
    <h1>게시글 목록</h1>
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
  },
  mounted() {
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