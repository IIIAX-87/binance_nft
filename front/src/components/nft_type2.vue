<template>
  <b-form inline>
    <b-container fluid>
      <b-row align-h="center">
        <b-col sm="2">
        <b-form-input size="sm" placeholder="Кол-во:" v-model="top">
        </b-form-input>
        </b-col>
        <b-col sm="2">Выбери тип:</b-col>
        <b-col sm="2">
        <b-form-select size="sm"
            @change="GET_TOP_TRANSACTIONS({'nft_type': nft_type, 'top': top})"
            v-model="nft_type">
          <b-form-select-option
              v-for="nft_type in NFT_TYPES"
              :key="nft_type.id"
              :value="nft_type.id">
            {{ nft_type.name }}
          </b-form-select-option>
        </b-form-select>
        </b-col>
      </b-row>
    </b-container>


      <b-form-group
          v-if="nft_type">
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
      >
        <div id="chart">
    <apexchart
        v-if="TRANSACTIONS.data[0].data.length > 1"
        type="scatter"
        height="500"
        :options="TRANSACTIONS.options"
        :series="TRANSACTIONS.data">
    </apexchart>

</div>
      </b-form-group>

    </b-form>

</template>

<script>

import {mapActions, mapGetters} from "vuex";
export default {
  name: 'nft_type2',
  data () {
    return {
      series: null,
      options: null,
      nft_type: null,
      product: null,
      top: 10,
      transactions: null,

    }
  },
  computed : {
    ...mapGetters(['NFT_TYPES', 'TOP_TRANSACTIONS', 'TRANSACTIONS',]),
  },
  methods:{
    ...mapActions(['GET_TOP_TRANSACTIONS', 'GET_TRANSACTIONS']),
  },
  mounted() {
  this.$store.dispatch('GET_NFT_TYPES');
}
}
</script>