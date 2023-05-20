import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../router'

import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    token: null,
    articles: [],
    depositProducts: [],
    savingProducts: [],
    exchanges: [],
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name : 'home' })
    },
    GET_DEPOSIT_PRODUCTS(state, depositProducts) {
      state.depositProducts = depositProducts
    },
    GET_SAVING_PRODUCTS(state, savingProducts) {
      state.savingProducts = savingProducts
    },
    GET_EXCHANGES(state, exchanges) {
      state.exchanges = exchanges
    },

    GET_ARTICLES(state, articles) {
      state.articles = articles
    }
  },
  actions: {
    signUp(context, payload) {
      const username = payload.id
      const password1 = payload.password1
      const password2 = payload.password2
      const gender = payload.selectedGender
      const age = payload.selectedAge
      const residence = payload.selectedResidence


      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2, gender, age, residence,
        }
      })
        .then(res => {
          // context.commit('SIGN_UP', res.data.key)
          context.commit('SAVE_TOKEN', res.data.key)
          alert('회원가입이 완료되었습니다!')
        })
        .catch(err => {
          alert('잘못 입력하셨습니다. 다시 입력하세요.')
        })
    },

    logIn(context, payload) {
      const username = payload.id
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then(res => {
          context.commit('SAVE_TOKEN', res.data.key)
          alert('로그인 되었습니다!')
        })
        .catch(()=> {
          alert('잘못 입력하셨습니다. 다시 입력하세요.')
        })

    },
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        },
      })
        .then(res =>
          { context.commit('GET_ARTICLES', res.data) }
        )
        .catch(err => {console.log(err)})
    },

    getDepositProducts(context) {
      axios({
        method: 'get',
        url: `${API_URL}/finlife/deposit-products/`
      })
        .then(res => 
          context.commit('GET_DEPOSIT_PRODUCTS', res.data)
        )
        .catch(err => console.log(err))
    },

    getSavingProducts(context) {
      axios({
        method: 'get',
        url: `${API_URL}/finlife/saving-products/`
      })
        .then(res => 
          context.commit('GET_SAVING_PRODUCTS', res.data)
        )
        .catch(err => console.log(err))
    },

    getExchanges(context) {
      axios({
        method: 'get',
        url: `${API_URL}/finlife/exchangeinfo/`
      })
        .then(res =>
          context.commit('GET_EXCHANGES', res.data)
        )
        .catch(err => console.log(err))
    }
  },
  modules: {
  }
})
