<template>
    <div>

        <h1 class="mb-4">생성 페이지</h1>
        <form @submit.prevent="createPost">
        <div class="form-group">
            <label for="title">제목</label>
            <input v-model="title" type="text" id="title" class="form-control">
        </div>
        <div class="form-group">
            <label for="content">내용</label>
            <textarea v-model="content" id="content" class="form-control"></textarea>
        </div>
        <button type="submit" class="btn btn-light">생성하기</button><br>
        <br>
        <router-link to="/community" class="btn btn-light">돌아가기</router-link> 

        </form>
    </div>

</template>

<script>
export default {

}
</script>

<style>

</style>