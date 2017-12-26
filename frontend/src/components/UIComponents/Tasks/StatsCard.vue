<!-- Wrapping the StatsCard component around-->
<template>
  <div>
    <stats-card>
      <div :class="iconClass" slot="header">
        <i :class="icon"></i>
      </div>
      <div class="numbers" slot="content">
        <p>{{attrName | capitalize }}</p>
        {{displayValue | firstNDigits(4)}}
      </div>
      <div class="stats" slot="footer">
        <!-- <i class="ti-reload"></i> Updated now -->
      </div>
    </stats-card>
  </div>
</template>

<script>
import StatsCard from '../Cards/StatsCard'
export default {
  components: {
    StatsCard,
  },
  data() {
    return {
      value: null,
      maxValue: null,
      query: null,
      subscription: null,

      updateFunc: (value) => {
        let arr = value.get(this.attrName)
        if(typeof arr == 'object') this.value = arr[arr.length - 1]
        else this.value = arr
        if(this.maxAttrName != null){
          let max = value.get(this.maxAttrName)
          this.maxValue = max
        }
      },
    }
  },
  props: ["icon","iconClass","name","attrName","objectId","maxAttrName"],
  mounted: function() {
    this.buildQuery()
    this.subscription = this.query.subscribe()
    this.subscription.on('open',() => {
      console.log("subscription started")
    })
    this.subscription.on('update',this.updateFunc)
    this.subscription.on('close',() => {
      console.log("subscription closed")
    })

  },
  beforeDestroy: function() {
    this.subscription.unsubscribe()
  },
  computed: {
    displayValue: function() {
      if(this.value == null) return 'N/A'
      if(this.maxValue != null){
        return `${this.value}/${this.maxValue}`
      }
      else return this.value
    }
  },
  filters: {
    capitalize: function(value) {
      if (!value) return ''
      value = value.toString()
      return value.charAt(0).toUpperCase() + value.slice(1)
    },
    firstNDigits: function(v,n) {
      if(typeof v === "number") {
        return v.toFixed(n)
      }
      // not even a number
      return v
    }
  },
  methods: {
    buildQuery: function() {
      // build the query here
      this.query = new this.$store.state.parse.parseServer.Query("Task")
      this.query.select(this.attrName)
      // also include the attribute name of the "maximum value" of the quantity if it is given
      if(this.maxAttrName) this.query.select(this.maxAttrName)
      // initial fetch
      this.query.get(this.objectId).then(this.updateFunc)
    }
  }
}

</script>

<style>
</style>
