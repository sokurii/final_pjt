<template>
  <div class="article-details">
    <h1>게시글 상세 정보</h1>
    <div class="actions">
      <router-link
        :to="{
          name: 'UpdateArticle',
          params: { id: article.id, title: article.title, content: article.content },
        }"
      >
        <button class="btn btn-light">수정하기</button>
      </router-link>
      <button class="btn btn-danger" @click="deleteArticle">삭제하기</button>
    </div>
    <div class="article-info">
      <p><strong>제목:</strong> {{ article.title }}</p>
      <p><strong>작성자:</strong> {{ article.username }}</p>
      <p><strong>작성 날짜:</strong> {{ article.created_at.slice(0, 19).replace('T', ' ') }}</p>
      <p><strong>내용:</strong> {{ article.content }}</p>
    </div>
    <hr>
    <h3>댓글 목록</h3>
    <CommentList :comments="article.comment_set" :id="article.id"/>

    <button class="btn btn-primary" @click="goBack">뒤로가기</button>
  </div>
</template>

<script>
import CommentList from '@/components/CommentList.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'DetailArticleView',
  components: {
    CommentList,
  },
  data() {
    return {
      article: {},
    }
  },
  mounted() {
    this.getArticleDetail()
  },
  methods: {
    getArticleDetail() {
      axios
        .get(`${API_URL}/api/v1/articles/${this.$route.params.id}/`)
        .then((res) => {
          this.article = res.data
        })
        .catch((err) => console.log(err))
    },
    deleteArticle() {
      axios
        .delete(`${API_URL}/api/v1/articles/${this.$route.params.id}/delete/`)
        .then((res) => {
          alert('게시글이 삭제되었습니다.')
          this.$router.push({ name: 'community' })
        })
        .catch((err) => console.log(err))
    },
    goBack() {
      this.$router.push({ name: 'community' })
    },
  },
}
</script>

<style scoped>
.article-details {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}

.article-details h1 {
  font-size: 24px;
  margin-bottom: 20px;
}

.article-details .actions {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
}

.article-details .actions button {
  margin-right: 10px;
}

.article-details .article-info p {
  margin-bottom: 10px;
}

.article-details hr {
  margin-top: 30px;
  border: none;
  border-top: 1px solid #ccc;
}

.article-details .btn-primary {
  margin-top: 20px;
}

</style>
