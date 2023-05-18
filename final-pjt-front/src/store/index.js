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
    articles: [],
    token: null,

    products: [
    ],
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
    GET_DEPOSIT_PRODUCTS(state, products) {
      state.products = products
    }

  },
  actions: {
    signUp(context, payload) {
      const username = payload.id
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then(res => {
          // context.commit('SIGN_UP', res.data.key)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch(err => console.log(err))
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
        })
        .catch(err => console.log(err))

    },

    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${ context.state.token }`
        }
          .then(res =>
            { context.commit('GET_ARTICLES', res.data) }
          )
          .catch(err => {console.log(err)})
      })
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
    }
  },
  modules: {
  }
})
