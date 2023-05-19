<template>
  <div>
    <p>통화명 : {{ exchange.cur_unit }} | {{ exchange.cur_nm }} </p>
    <p>환율 : {{ exchange.exchange }}</p>
  </div>
</template>

<script>
export default {
  name: 'ExchangeListItem',
  props: {
    exchange: Object,
  }
  
}
</script>

<style>

</style>