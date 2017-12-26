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
      query: null,
      subscription: null
    }
  },
  props: ["icon","iconClass","name","attrName","objectId"],
  mounted: function() {
    this.buildQuery()
    this.subscription = this.query.subscribe()

    this.subscription.on('open',() => {
      console.log("subscription started")
    })
    this.subscription.on('update',(value) => {
      let val = value.get(this.attrName)
      this.value = val[val.length - 1]
    })
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
      // initial fetch
      this.query.get(this.objectId).then((value) => {
        let arr = value.get(this.attrName)
        this.value = arr[arr.length - 1]
      })
    }
  }
}

</script>

<style>
</style>
