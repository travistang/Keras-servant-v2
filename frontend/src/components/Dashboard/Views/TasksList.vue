<template>
  <div class="row">
    <div class="col-md-12">
      <paper-table
        title="Task list"
        :data="$store.state.tasks.tasks"
        :columns="$store.state.tasks.taskAttributes"

        :sub-title="taskList.length + ' Tasks'"
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
  computed: {
    ...mapGetters({
      taskList: 'getTaskList'
    })
  },
  sockets:
  {
      message: function(msg)
      {
        console.log("meesage:" + msg)
        store.commit("add_task",{name:"Message",status: msg})
        // this.$socket.send('hello')
      },
      hello: function(msg)
      {
        console.log("server says hello:" + msg)
        store.commit("add_task", {name: "Hello Message", status: msg})
      },
      connect: function() {
        console.log("connect from taskslist")
        this.$socket.send("world")
      }
  }
}
</script>
<style>
</style>
