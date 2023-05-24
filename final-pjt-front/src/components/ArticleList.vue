<template>
  <div id="container" class="bg-white">
    <!-- 배너 영역  -->
    <div class="board-title d-flex flex-column align-items-center justify-content-center">
      <div><h1 class="board-title-text"><strong>커뮤니티</strong></h1></div>
      <div>Lorem, ipsum dolor sit amet consectetur adipisicing elit.<br>Illum recusandae maxime temporibus blanditiis reprehenderit quos cumque nulla unde sunt</div>
      <!-- <img src="@/assets/document.png"  style="width : 10% ; transform:rotate(20deg);" > -->
    </div>

    <!-- 내용 영역 -->
    <div class="article-list-container">
      <h2 class="mt-4 mb-3 p-2">총 {{ articles.length }}개의 게시글이 있습니다</h2>
      <div class="d-flex justify-content-end mr-2">
        <router-link :to="{ name: 'CreateArticle' }" class="board-btn">게시글 작성하기</router-link>
      </div>
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
        { key: 'created_at', label: '날짜', thStyle: { width: '20%' }},
      ],
    }
  },
  computed: {
    articles() {
      return this.$store.state.articles
    },
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
#container {
  height: 100vh; /* 화면 전체 높이로 설정 */
  flex-grow:1;
}

.article-list-container {
  padding: 20px 50px ;
  height: calc(100% - 500px); /* footer-bar.view를 제외한 높이로 설정 (60px는 footer-bar.view의 높이) */
  /* overflow-y: auto; */
}

.board-title {
  /* margin: 50px 0px; */

  background-color: #F3F2E9;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  padding: 20px; 
  height: 400px;
}


.board-btn {
  /* 버튼에 원하는 스타일을 적용하세요 */
  display: inline-block;
  padding: 10px 20px;
  background-color: #6da36f;
  color: #fff;
  border-radius: 5px;
  text-decoration: none;
}

.board-btn:hover {
  background-color: #3c643e;
}

.board-btn:focus {
  outline: none;
}


</style>
