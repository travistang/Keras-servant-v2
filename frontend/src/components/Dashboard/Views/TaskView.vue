<template>
  <div>
    <div class="col-lg-4">
      <stats-card
        icon="ti-alert"
        iconClass="icon-big text-center icon-danger"
        name="Loss"
        :value="value"
      />
    </div>
    <div class="col-lg-4">
      <stats-card
        icon="ti-target"
        iconClass="icon-big text-center icon-success"
        name="Accuracy"
        :value="value"
      />
    </div>
  </div>
</template>

<script>
  import store from '../../../store'
  import StatsCard from '../../UIComponents/Tasks/StatsCard'
export default {
  components: {
    'stats-card': StatsCard,
  },
  data(){
    return {
      queryClient: new this.$store
                    .state
                    .parse
                    .parseServer
                    .LiveQueryClient({
        applicationId: this.$store.state.parse.applicationId,
        masterKey: this.$store.state.parse.masterKey,
        javascriptKey: this.$store.state.parse.masterKey,
        serverURL: this.$store.state.parse.serverLiveQueryURL,
      }),
      query: null,
      // querySubscription: null,
      clientSubscription: null,
      value: 0,
    }
  },
  mounted: function() {
    this.buildQuery()
    // this.querySubscription = this.query.subscribe()
    this.clientSubscription = this.queryClient.subscribe(this.query,"12345")

    this.clientSubscription.on('open',() => {
      console.log("subscription started")
    })
    this.clientSubscription.on('create',function(task) {
      console.log("new object:" + JSON.stringify(task))
    })
    this.clientSubscription.on('update',function(task) {
      console.log("update object:" + JSON.stringify(task))
    })
    this.clientSubscription.on('close',() => {
      console.log("subscription closed")
    })

    this.queryClient.on('error',(error) => {
      console.log(`error: ${JSON.stringify(error)}`)
    })

    // start the connection here
    this.queryClient.open()
  },
  beforeDestroy: function() {
    this.queryClient.unsubscribe(this.clientSubscription)
  },
  methods: {
    buildQuery: function() {
      // build the query here
      this.query = new this.$store.state.parse.parseServer.Query("Task")

      // this.query.find({
      //   success: function(results){
      //     console.log(`There are ${results.length} tasks`)
      //
      //   },
      //   error: function(error){
      //     console.log(`error occured while query: ${error.code} ${error.message}`)
      //   }
      // })
    }
  }

}
</script>

<style>
</style>
