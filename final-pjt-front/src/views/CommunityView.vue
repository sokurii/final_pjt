<template>
  <div>
    <h1>CommunityView</h1>
    <button @click='goToWrite'>글 작성하기</button>


  </div>
</template>

<script>


export default {
  name: 'CommunityView',
  methods:{
    goToWrite(){
      this.$router.push('/write')
    }
  }

}
</script>

<style>

</style>
