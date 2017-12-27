<template>
  <div>
    <chart-card
      :chartData="chartData"
      :chartOption="chartOption"
      :chartId="chartId"
      :colors="colors"
      :updateInterval="updateInterval"
    >
      <span slot="title">Graph</span>
      <!-- <span slot="subTitle"> 24 Hours performance</span> -->
      <div slot="legend">
        <div v-for="ind in chartData.series.length">
          <i :style="getLegendStyle(ind - 1)" class="fa fa-circle" />
          {{monitoredAttrs[ind - 1]}}
        </div>
      </div>
      <div slot="footer">
        Updated every {{updateInterval | toSec}} secs
      </div>
    </chart-card>
  </div>
</template>

<script>
import ChartCard from '../Cards/ChartCard'
import Legend from 'chartist-plugin-legend'
import store from '../../../store'
export default {
  components: {
    ChartCard,
  },
  props: ["attrNames","objectId","chartId","updateInterval"],
  data() {
    return {
      colors: this.prepareColors(),
      chartData: {
        labels: [],
        series: [],
      },
      chartOption: {
        scales: {
          xAxes: [{
              gridLines: {
                  show: false,
              }
          }],
          yAxes: [{
              gridLines: {
                show: false
              }
          }]
        },
      },

      query: null,
      subscription: null,
    }
  },
  filters: {
    toSec: function(v){
      if (typeof v === 'number') return v / 1000
      return v
    }
  },
  computed: {
    monitoredAttrs: function() {
      return this.attrNames.split(',')
    }
  },
  methods: {
    prepareColors: function(){
      return "royalblue burlywood limegreen coal crimson darkred darksalmon dodgerblue firebrick chocolate peru steelblue tan teal wheat".split(' ')
    },
    getLegendStyle: function(ind) {
      return `color: ${this.colors[ind]}`
    },
    buildQuery: function() {
      this.query = new store.state.parse.parseServer.Query("Task")
      for(var i in this.monitoredAttrs)
      {
        this.query.select(this.monitoredAttrs[i])
      }
      this.query.get(this.objectId,{
        success: (task) =>{
          this.populateValues(task)
        },
        error: (obj,e) => {
          //this.$route.go
          console.log(e)}
      })

      this.subscription = this.query.subscribe()
      this.subscription.on('open',() => {console.log("subscription opened")})
      this.subscription.on('update',(v) => {
        // TODO: if some of the values didnt update, it will be repeated. Fix this
        for(var i in this.monitoredAttrs){
          let attr = this.monitoredAttrs[i]
          let vals = v.get(attr)
          // push the last value to the corresponding series
          this.chartData.series[i].push(vals[vals.length - 1])
        }
      })

    },
    populateValues: function(task) {
      for(var attr_id in this.monitoredAttrs) {
        let attr_name = this.monitoredAttrs[attr_id]
        let values = task.get(attr_name)
        // ignore all monitored attributes that are not a series
        if (typeof values != 'object') continue
        for (var v in values) {
          // copy the data one by one
          this.chartData.series[attr_id].push(values[v])
        }
      }
    }
  },
  created: function() {
    // create socket here
    // initial value population
    for(var i in this.monitoredAttrs) {
      this.chartData.series.push([])
    }
    this.buildQuery()
  },
  beforeDestroy: function() {
    this.subscription.unsubscribe()
  }
}
</script>

<style>
.ct-series-a .ct-line,
.ct-series-a .ct-point {
  stroke: royalblue;
}
.ct-series-b .ct-line,
.ct-series-b .ct-point {
  stroke: burlywood;
}
.ct-series-c .ct-line,
.ct-series-c .ct-point {
  stroke: limegreen;
}
.ct-series-d .ct-line,
.ct-series-d .ct-point {
  stroke: coral;
}
.ct-series-e .ct-line,
.ct-series-e .ct-point {
  stroke: crimson;
}
.ct-series-f .ct-line,
.ct-series-f .ct-point {
  stroke: darkred;
}
.ct-series-g .ct-line,
.ct-series-g .ct-point {
  stroke: darksalmon;
}
.ct-series-h .ct-line,
.ct-series-h .ct-point {
  stroke: dodgerblue;
}
.ct-series-i .ct-line,
.ct-series-i .ct-point {
  stroke: firebrick;
}
.ct-series-j .ct-line,
.ct-series-j .ct-point {
  stroke: chocolate;
}
.ct-series-k .ct-line,
.ct-series-k .ct-point {
  stroke: peru;
}
.ct-series-l .ct-line,
.ct-series-l .ct-point {
  stroke: steelblue;
}
.ct-series-m .ct-line,
.ct-series-m .ct-point {
  stroke: tan;
}
.ct-series-n .ct-line,
.ct-series-n .ct-point {
  stroke: teal;
}
.ct-series-o .ct-line,
.ct-series-o .ct-point {
  stroke: wheat;
}
</style>
