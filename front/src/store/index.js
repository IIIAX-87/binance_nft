import Vue from 'vue'
import Vuex from 'vuex'
import Axios from 'axios';
import moment from "moment";

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
    series: {
      data: [{
        name: 'null',
        data: []
      }],
      options: {
            tooltip: {
            custom: function({seriesZ, seriesIndex, dataPointIndex, w}) {
              console.log(w.globals.seriesZ)
              return '<div class="arrow_box">' +
                      '<span><h5>' + w.globals.seriesZ[seriesIndex][dataPointIndex]['buyer']['buyer_name'] + ' </h5>' + moment(w.globals.seriesZ[seriesIndex][dataPointIndex]['order_success_time']).format("DD.MM.YYYY hh:mm:ss") +'</span></br>' +
                      '<span>' + w.globals.seriesZ[seriesIndex][dataPointIndex]['price']+ ' ' + w.globals.seriesZ[seriesIndex][dataPointIndex]['currency']['name'] + '</span>' +
                      '</div>'
            }
},
            chart: {
              height: 100,
              type: 'scatter',
              zoom: {
                type: 'xy'
              },
              animations: {
                enabled: false
              },
            },
            dataLabels: {
              enabled: false

            },
            grid: {
              xaxis: {
                lines: {
                  show: true
                }
              },
              yaxis: {

                lines: {
                  show: true
                }
              },
            },
            xaxis: {
              type: 'datetime',
              labels: {
          show: true,
          rotate: -45,
          rotateAlways: false,
          hideOverlappingLabels: true,
          showDuplicates: false,
          trim: false,
          minHeight: undefined,
          maxHeight: 120,
          style: {
              colors: [],
              fontSize: '12px',
              fontFamily: 'Helvetica, Arial, sans-serif',
              fontWeight: 400,
              cssClass: 'apexcharts-xaxis-label',
          },
          offsetX: 0,
          offsetY: 0,
          format: undefined,
          formatter: undefined,
          datetimeUTC: true,
          datetimeFormatter: {
              year: 'yyyy',
              month: "MMM 'yy",
              day: 'dd MMM',
              hour: 'HH:mm:ss',
          },
      },

            },
            yaxis: {
            }
          },
    }
  },
  getters: {
    NFT_TYPES: state => {
      return state.nft_types;
    },
    TOP_TRANSACTIONS: state => {
      return state.top_transactions;
    },
    TRANSACTIONS: state => {
      return state.series;
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
      state.series.data[0]['data'] = []
      state.series.data[0]['name'] = payload[0]['product']['product_title']
      let arrayLength = payload.length
      for (let i = 0; i < arrayLength; i++) {
        state.series.data[0]['data'].push([payload[i]['order_success_time'],parseInt(payload[i]['price'], 10), payload[i]])

      }

    },
  },
  actions: {
    GET_NFT_TYPES: async (context, payload) => {
      let {data} = await Axios.get('http://rdp.tekhnodom.ru:8000/api/nft_type/?format=json&json');
      context.commit('SET_NFT_TYPES', data);
    },
    GET_TOP_TRANSACTIONS: async (context, payload) => {
      let {data} = await Axios.get('http://rdp.tekhnodom.ru:8000/api/transaction_top/?nft_type=' + payload.nft_type + '&top=' + payload.top + '&format=json&json');
      context.commit('SET_TOP_TRANSACTIONS', data);
    },
    GET_TRANSACTIONS: async (context, payload) => {
      let {data} = await Axios.get('http://rdp.tekhnodom.ru:8000/api/transaction/?product=' + payload + '&format=json&json');
      context.commit('SET_TRANSACTIONS', data);

    },
  },
  modules: {
  },
  methods:{
      fillData (label) {
    return moment(label).format("DD.MM.YYYY hh:mm:ss");
  }
  },

})
