import Vue from 'vue'
import Vuex from 'vuex'
import {WalletStore} from './walletstore'
Vue.use(Vuex)

export const store = new Vuex.Store({
  modules: {
    WalletStore
  }
});
