<template>
  <div>
    <form @submit.prevent="createComment">
      <h4>댓글 작성</h4>
      <span>
        <b-form-input v-model="content" placeholder="내용" style="width: 300px; height:50px;" ></b-form-input>
      </span>
      <button type="submit" class="btn btn-success">작성하기</button>
    </form>

    <CommentListItem 
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
    />
  </div>
</template>

<script>
import CommentListItem from './CommentListItem.vue'

import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentList',
  components: {
    CommentListItem,
  },
  data() {
    return {
      content: null,
    }
  },
  props: {
    comments: Array,
    id: Number,
  },
  methods: {
    createComment() {
      const content = this.content
      if (!content) {
        alert('내용을 입력해주세요!')
        return
      }

      axios({
        method: 'post',
        url: `${API_URL}/api/v1/articles/${this.id}/comments/`,
        data: { content },
        headers: {
          Authorization: `Token ${ this.$store.state.token }`
        }
      })
        .then((res) => {
          alert('댓글이 작성되었습니다.')
          this.$router.go(0)
        })
        .catch(err => console.log(err))
    },

  }
}
</script>

<style>

</style>