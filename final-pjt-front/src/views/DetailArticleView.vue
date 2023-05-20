<template>
  <div>
    <h1>게시글 상세 정보</h1>
    <div class="mb-5 d-flex">
      <button class="btn btn-light">수정하기</button>
      <button class="btn btn-danger" @click="deleteArticle">삭제하기</button>
    </div>
    <div>
      <p>제목 : {{ article.title }} </p>
      <p>작성자 : {{ article.username }} </p>
      <p>생성 날짜 : {{ article.created_at }}</p>
      <p>내용 : {{ article.content }} </p>
    </div>
    <button class="btn btn-primary" @click="goBack">뒤로가기</button>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailArticleView',
  data() {
    return {
      article: null
    }
  },
  created() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/`,
      })
        .then((res) => {
          this.article = res.data
        })
        .catch(err => console.log(err))
    },
    deleteArticle() {
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/delete/`,
      })
        .then((res) => {
          alert('게시글이 삭제되었습니다.')
          this.$router.push({ name: 'community' })
        })
        .catch(err => console.log(err))
    },
    goBack() {
      this.$router.go(-1)
    }
  }
}
</script>

<style>

</style>