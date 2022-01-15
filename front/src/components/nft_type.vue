<script src="../views/LineChart.js"></script>
<template>
  <div class="hello">
    <b-form>
      <b-form-group style="width: 50px; box-sizing: content-box; padding: 0 48% 0  "
      label="Количество:">
        <b-form-input class="input-group-btn" v-model="top">
        </b-form-input>
      </b-form-group>
      <b-form-group
      label="Тип:">
    <b-form-select
        @change="GET_TOP_TRANSACTIONS({'nft_type': nft_type, 'top': top})"
        v-model="nft_type">
      <b-form-select-option
          v-for="nft_type in NFT_TYPES"
          :key="nft_type.id"
          :value="nft_type.id">
        {{ nft_type.name }}
      </b-form-select-option>
    </b-form-select>
      </b-form-group>

      <b-form-group
          v-if="nft_type"
      label="Email address:">
    <b-form-select
        v-on:change="GET_TRANSACTIONS(product)"
        v-model="product">
      <b-form-select-option
          v-for="product in TOP_TRANSACTIONS"
          :key="product.id"
          :value="product.id">
        {{ product.product }}
      </b-form-select-option>
    </b-form-select>
      </b-form-group>
      <b-form-group
      v-if="product"
      label="Транзакции:">
        <scatter-chart v-if="TRANSACTIONS" class="small" :chart-data="TRANSACTIONS" :options="options"></scatter-chart>
        <b-table striped hover :items="TRANSACTIONS.alldata[0]"></b-table>
      </b-form-group>
    </b-form>
  </div>
</template>

<script>
import ScatterChart from './LineChart.js'
import moment from "moment";
import {mapGetters, mapActions} from 'vuex';
export default {
  components: {
      ScatterChart
    },
  data() {
    return {
      nft_type: null,
      product: null,
      top: 10,
      transactions: null,
      options: {
        scales: {
            xAxes: [{
              ticks: {
                userCallback: function (label) {
                  return moment(label).format("DD.MM hh:mm:ss,ms");
                }
              }
            }]
         }
 }
    }
  },
  name: 'nft_type',
  computed : {
    ...mapGetters(['NFT_TYPES', 'TOP_TRANSACTIONS', 'TRANSACTIONS',]),
  },
  methods:{
  ...mapActions(['GET_TOP_TRANSACTIONS', 'GET_TRANSACTIONS']),
  fillData (label) {
    return moment(label).format("DD.MM hh:mm:ss");
  },

},
  mounted() {
  this.$store.dispatch('GET_NFT_TYPES');
}
}
</script>

<style scoped>
.small {
    max-width: 600px;
    margin: 10px auto;
  }
</style>
