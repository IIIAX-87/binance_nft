<template>
  <div class="about">
    <h1>This is an about page</h1>
    <scatter-chart class="small" :chart-data="datacollection" :options="options"></scatter-chart>
  </div>
</template>
<script>
import ScatterChart from './LineChart.js'
import moment from 'moment'
  export default {
    components: {
      ScatterChart
    },
    data () {
      return {
        datacollection: null,
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
    mounted () {
      this.fillData()
    },
    methods: {
      fillData () {
        this.datacollection = {
  datasets: [{
    label: 'Mystery Box',
    data: [{
      x: 1499516102000,
      y: 43
    }, {
      x: 1499516103000,
      y: 42
    }, {
      x: 1499516103300,
      y: 50
    }, {
      x: 1499516403500,
      y: 22
    }],
    backgroundColor: 'rgb(255, 99, 132)'
  }],
}
      },
    }
  }
</script>

<style>
  .small {
    max-width: 600px;
    margin: 150px auto;
  }
</style>
