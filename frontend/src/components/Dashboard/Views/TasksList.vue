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

}
</script>
<style>
</style>
