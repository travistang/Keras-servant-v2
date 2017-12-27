<template>
  <div class="card">
    <div class="header">
      <slot name="title"></slot>
      <p class="category">
        <slot name="subTitle"></slot>
      </p>
    </div>
    <div class="content">
      <div :id="chartId" class="ct-chart"></div>
      <div class="footer">
        <div class="chart-legend">
          <slot name="legend"></slot>
        </div>
        <hr>
        <div class="stats">
          <slot name="footer"></slot>
        </div>
        <div class="pull-right">
        </div>
      </div>
    </div>

  </div>
</template>
<script>
import store from '../../../store'
  export default {
    name: 'chart-card',
    props: {
      footerText: {
        type: String,
        default: ''
      },
      headerTitle: {
        type: String,
        default: 'Chart title'
      },
      chartType: {
        type: String,
        default: 'Line' // Line | Pie | Bar
      },
      chartOptions: {
        type: Object,
        default: () => {
          return {}
        }
      },
      chartData: {
        type: Object,
        default: () => {
          return {
            labels: [],
            series: []
          }
        }
      },
      updateInterval: {
        type: Number,
        default: () => {return 2000}
      },
      colors: {
        type: Array,
      }
    },
    data () {
      return {
        chartId: 'no-id',
        chart: null,
        timer: null,

      }
    },
    methods: {
      /***
       * Initializes the chart by merging the chart options sent via props and the default chart options
       */
      initChart () {
        var chartIdQuery = `#${this.chartId}`
        this.chart = this.$Chartist[this.chartType](chartIdQuery, this.chartData, this.chartOptions)
        this.timer = setInterval(() => {
          this.chart.update()
        },this.updateInterval)
      },
      /***
       * Assigns a random id to the chart
       */
      updateChartId () {
        var currentTime = new Date().getTime().toString()
        var randomInt = this.getRandomInt(0, currentTime)
        this.chartId = `div_${randomInt}`
      },
      getRandomInt (min, max) {
        return Math.floor(Math.random() * (max - min + 1)) + min
      },
    },
    watch: {
      'chart': function() {
        if (this.chart != null && this.timer == null) {
          console.log("setting timer")
          // this.timer = setInterval(() => {
          //   this.chart.update(this.chartData)
          // },this.updateInterval)
        }
      }
    },
    mounted () {
      this.updateChartId()
      this.$nextTick(this.initChart)
      // trigger update on interval
    }
  }

</script>
<style>

</style>
