<template>
  <div class="bg-white">
    <h1 class="p-3">게시글 목록</h1>
    <router-link :to="{ name: 'CreateArticle' }" class="btn btn-primary">게시글 작성하기</router-link>
    
    <div class="board_container">
      <b-table striped hover :items="articles" :fields="fields" :per-page="perPage">
        <template #cell(title)="{ item }">
          <router-link :to="{ name: 'DetailArticle', params: { id: item.id } }">{{ item.title }}</router-link>
        </template>
        <template #cell(username)="{ item }">
          {{ item.username }}
        </template>
        <template #cell(created_at)="{ item }">
          {{ item.created_at }}
        </template>
      </b-table>

      <b-pagination
        v-model="currentPage"
        :total-rows="articles.length"
        :per-page="perPage"
        align="center"
        class="mt-3"
      ></b-pagination>
    </div>
  </div>
</template>

<script>
import { BTable, BPagination } from 'bootstrap-vue'
import ArticleListItem from './ArticleListItem.vue'

export default {
  name: 'ArticleList',
  components: {
    BTable,
    BPagination,
    ArticleListItem,
  },
  data() {
    return {
      currentPage: 1,
      perPage: 10,
      fields: [
        { key: 'title', label: '제목' },
        { key: 'username', label: '작성자' },
        { key: 'created_at', label: '날짜' },
      ],
    }
  },
  computed: {
    articles() {
      return this.$store.state.articles
    },
    // noArticles() {
    //   return this.$store.state.articles && this.$store.state.articles.length === 0
    // },
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      this.$store.dispatch('getArticles')
    },
  },
}
</script>

<style>
.board_container{
  margin: 50px 100px 200px;
  background-color: #fff;
}
</style>
