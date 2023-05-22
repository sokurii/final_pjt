<template>
  <div>
    <h2>게시글 수정</h2>
    <form @submit.prevent="updateArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model="title"><br>
      <label for="content">내용 : </label>
      <textarea
        id="content" cols="30" rows="10"
        v-model="content"
      >
      </textarea><br>
      <button type="submit" id="submit" class="btn btn-success">게시글 수정</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'UpdateArticleView',
  data() {
    return {
      title: this.$route.params.title,
      content: this.$route.params.content,
    }
  },
  methods: {
    updateArticle() {
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
        method: 'put',
        url: `${API_URL}/api/v1/articles/${this.$route.params.id}/update/`,
        data: { title, content },
      })
        .then((res) => {
          alert('게시글이 수정되었습니다.')
          this.$router.push({ name: 'DetailArticle', params: { id: this.$route.params.id } })
        })
        .catch(err => console.log(err))
    },
  }

}
</script>

<style>

</style>