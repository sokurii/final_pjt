<template>
  <div>
    <!-- <ExchangeList /> -->
    <ExchangeCalculator />
  </div>
</template>

<script>
import ExchangeList from '@/components/ExchangeList'
import ExchangeCalculator from '@/components/ExchangeCalculator'

export default {
  name: 'ExchangeView',
  components: {
    ExchangeList,
    ExchangeCalculator,
  }
}
</script>

<style>

</style>