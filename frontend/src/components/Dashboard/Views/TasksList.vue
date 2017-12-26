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
      console.log('item:' + JSON.stringify(item))
      let id = item.objectId
      console.log("going to id:" + id)
      this.$router.push({name: 'task_details',params: {"id": id}})
    },
  },

  created: function() {
    // empty the task list first
    store.commit('clear_task')
    // get the list of tasks from the database
    let parse = this.$store.state.parse.parseServer
    let query = new parse.Query("Task")
    query.select('objectId','name') // get the name of the tasks as well
    // fetch initial task list
    query.find({
      success: function(tasks){
        for(var i in tasks){
          store.commit("add_task",tasks[i])
        }
      },
      error: function(err) {
        // TODO: handle error here
        console.log(err)
      }
    })
    this.querySubscription = query.subscribe()

    this.querySubscription.on("create",function(task){
      store.commit('add_task',task)
    })
    this.querySubscription.on("update",function(task){
      store.commit("update_task",task)
    })
  },

  beforeDestroy: function() {
    this.querySubscription.unsubscribe()
  }

}
</script>
<style>
</style>
