<template>
  <div>
    <div class="board-title d-flex flex-column justify-content-center">
      <img class="article-img" src="../assets/chat.png" alt="">
      <div><h1 class="board-title-text text-center"><strong>커뮤니티</strong></h1></div>
      <div><h5 class="text-center pt-3">나와 비슷한 관심사를 가진 사람들과 금융 정보를 공유해요</h5></div>
      <div><h5 class="text-center">자유롭게 소통하고, 소소한 금융 꿀팁도 알아가세요!</h5></div>
    </div>
    <div class="create-article-container">
      <div class="article-title text-start">
        <h2><strong>게시글 작성</strong></h2>
      </div>
      <form @submit.prevent="createArticle" >
        <div class="create-article-form">
          <label for="title">제목:</label>
          <input type="text" id="title" v-model="title" required><br>
          <label for="content">내용:</label>
          <textarea id="content" cols="30" rows="10" v-model="content" required></textarea><br>
        </div>
        <div class="submit-btn d-flex justify-content-between">
          <button class="btn btn-primary" @click="goBack">뒤로가기</button>
          <button type="submit" id="submit" class="btn btn-success">게시글 작성</button>
        </div>  
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CreateArticleView',
  data() {
    return {
      title: null,
      content: null,
    }
  },
  computed: {
    token() {
      return this.$store.state.token
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      if (!title) {
        alert('제목을 입력해주세요!')
        return
      } else if (!content) {
        alert('내용을 입력해주세요!')
        return
      }

      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/`,
        data: { title, content },
        headers: {
          Authorization: `Token ${ this.token }`
        }
      })
        .then((res) => {
          alert('게시글이 작성되었습니다.')
          this.$router.push({ name: 'community' })
        })
        .catch(err => console.log(err))
    },
    goBack() {
      this.$router.push({ name: 'community' })
    },
  }
}
</script>

<style scoped>
.create-article-container {
  background-color: #fff;
  padding: 80px;
  height: calc(100% -100px);
}

.create-article-form {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.article-title{
  margin-bottom: 50px;
}

label {
  margin-bottom: 5px;
}

input[type="text"],
textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 10px;
}

button {
  padding: 10px 20px;
}

/* .submit-btn{
  margin-left: auto;  
} */
.btn-success{
  background-color:#6da36f;
  border: none;
}
</style>
