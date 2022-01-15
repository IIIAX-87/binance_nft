import Vue from 'vue'
import Vuex from 'vuex'
import Axios from 'axios';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    nft_types: null,
    top_transactions: null,
    transactions: {
      alldata:[],
      datasets: [{
        label: 'Mystery Box',
        data: [],
        backgroundColor: 'rgb(255, 99, 132)'
        }],
},
  },
  getters: {
    NFT_TYPES: state => {
      return state.nft_types;
    },
    TOP_TRANSACTIONS: state => {
      return state.top_transactions;
    },
    TRANSACTIONS: state => {
      return state.transactions;
    },
  },
  mutations: {
    SET_NFT_TYPES: (state, payload) => {
      state.nft_types = payload;
    },
    SET_TOP_TRANSACTIONS: (state, payload) => {
      state.top_transactions = payload;
    },
    SET_TRANSACTIONS: (state, payload) => {
      var arrayLength = payload.length
      for (var i = 0; i < arrayLength; i++) {
        state.transactions.datasets[0].data.push({x: payload[i].order_success_time, y: Number(payload[i].price)})

      } state.transactions.alldata.push(payload);
    },
  },
  actions: {
    GET_NFT_TYPES: async (context, payload) => {
      let {data} = await Axios.get('http://ec2-52-50-121-50.eu-west-1.compute.amazonaws.com:8000/api/nft_type/?format=json&json');
      context.commit('SET_NFT_TYPES', data);
    },
    GET_TOP_TRANSACTIONS: async (context, payload) => {
      let {data} = await Axios.get('http://ec2-52-50-121-50.eu-west-1.compute.amazonaws.com:8000/api/transaction_top/?nft_type=' + payload.nft_type + '&top=' + payload.top + '&format=json&json');
      context.commit('SET_TOP_TRANSACTIONS', data);
    },
    GET_TRANSACTIONS: async (context, payload) => {
      let {data} = await Axios.get('http://ec2-52-50-121-50.eu-west-1.compute.amazonaws.com:8000/api/transaction/?product=' + payload + '&format=json&json');
      context.commit('SET_TRANSACTIONS', data);
    },
  },
  modules: {
  }
})
