<template>
  <div class="row">
    <div class="col-md-12">
      <paper-table
        title="Task list"
        :data="$store.state.tasks.tasks"
        :columns="$store.state.tasks.taskAttributes"
        :sub-title="taskList.length + ' Tasks'"
        @item-click="(item) => this.itemClicked(item)"
      >
<!-- :sub-title="$store.state.tasks.tasks.length + 'Tasks'" -->
      </paper-table>
    </div>
  </div>

</template>
<script>
import store from '../../../store'
import { mapGetters } from 'vuex'
import PaperTable from 'components/UIComponents/PaperTable.vue'
export default {
  components: {
    PaperTable
  },
  data(){
    return {
        querySubscription: null,
    }
  },
  computed: {
    ...mapGetters({
      taskList: 'getTaskList'
    })
  },
  methods: {
    itemClicked: function(item) {
      let id = item.id
      this.$router.push({name: 'task_details',params: {"id": id}})
    }
  },

  created: function() {
    // get the list of tasks from the database
    let parse = this.$store.state.parse.parseServer
    let query = parse.Query("Task")
    this.querySubscription = query.subscribe()
    this.querySubscription.on("open",function(){
      console.log("subscribing task list")
    })
    this.querySubscription.on("create",function(task){
      this.$store.commit("add_task",task)
    })
    this.querySubscription.on("update",function(task){
      this.$store.commit("update_task",task)
    })
  },

  beforeDestroy: function() {
    this.querySubscription.unsubscribe()
  }

}
</script>
<style>
</style>
