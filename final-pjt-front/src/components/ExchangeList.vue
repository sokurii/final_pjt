<template>
  <div class="exchange-container">
    <h2>오늘의 환율</h2>
    <p>{{ today }} 기준</p>
    <p>IDR, JPY는 100 화폐단위당 환율</p>
    <hr>
    <div class="">
      <ExchangeListItem 
        v-for="exchange in exchangesExceptKRW"
        :key="exchange.id"
        :exchange="exchange"
      />
    </div>
    <hr>
  </div>
</template>

<script>
import ExchangeListItem from './ExchangeListItem.vue'

export default {
  name: 'ExchangeList',
  components: {
    ExchangeListItem,
  },
  computed: {
    exchanges() {
      return this.$store.state.exchanges
    },
    exchangesExceptKRW() {
      return this.exchanges.filter(
        (exchange) => exchange.cur_unit != 'KRW'
      )
    },
    today() {
      const today = new Date();
      const year = today.getFullYear() // 현재 연도
      const month = today.getMonth() + 1 // 현재 월 (0부터 시작하므로 1을 더함)
      const day = today.getDate()

      return `${year}-${month}-${day}`
    }
  },
  mounted() {
    this.getExchanges()
  },
  methods: {
    getExchanges() {
      this.$store.dispatch('getExchanges')
    }
  }

}
</script>

<style>
.exchange-container{
  background-color: white;
  
}
</style>