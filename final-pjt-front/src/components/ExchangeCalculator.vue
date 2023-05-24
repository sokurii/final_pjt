<template>
  <div class="exchange-container">
    <h2>환율 계산기</h2>
    <div class="m-5">
      <b-input-group size="lg" prepend="$">
        <b-form-select v-model="exchange1" :options="exchangeName"></b-form-select>
        <b-form-input type="number" v-model="exchangeInput" @input="validateInput"></b-form-input>
      </b-input-group>
      <br>
      <button class="btn btn-primary" @click="change">CHANGE</button>
      <b-input-group size="lg" append="￦">
        <b-form-input type="number" v-model="exchangeOutput" disabled></b-form-input>
        <b-form-select v-model="exchange2" :options="exchangeName"></b-form-select>
      </b-input-group>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ExchangeCalculator',
  data() {
    return {
      exchangeInput: null,
      exchangeOutput: 0,
      exchange1: 'USD 미국 달러',
      exchange2: 'KRW 한국 원',
    }
  },
  computed: {
    exchanges() {
      return this.$store.state.exchanges
    },
    exchangeName() {
      return this.exchanges.map(exchange => exchange.cur_unit + ' ' + exchange.cur_nm)
    },
    exchangeValue() {
      const exchangeValue = {}
      this.exchanges.forEach(exchange => {
        const exchangeKey = exchange.cur_unit + ' ' + exchange.cur_nm
        exchangeValue[exchangeKey] = parseFloat(exchange.exchange.replace(',',''))
      })
      return exchangeValue
    }
  },
  methods: {
    validateInput() {
      // 숫자 이외의 문자 제거
      this.exchangeInput = this.exchangeInput.replace(/[^0-9.]/g, '');
      this.calculateExchange();
    },
    calculateExchange() {
      const exchange1 = this.exchange1
      const exchange2 = this.exchange2
      const exchangeRate = this.exchangeValue[exchange1] / this.exchangeValue[exchange2]
      this.exchangeOutput = this.exchangeInput * exchangeRate
    },
    change() {
      const temp = this.exchange1
      this.exchange1 = this.exchange2,
      this.exchange2 = temp
      this.exchangeInput = this.exchangeOutput
      this.exchangeOutput = this.exchangeInput * this.exchangeValue[this.exchange1] / this.exchangeValue[this.exchange2]
    }
  }
  
}
</script>

<style>

</style>