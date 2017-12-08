<template>
  <div class="row">
    <div class="col-md-12">
      <paper-table
        title="Task list"
        :data="$store.state.tasks.tasks"
        :columns="$store.state.tasks.taskAttributes"
        :sub-title="$store.state.tasks.tasks.length + 'Tasks'">

      </paper-table>
    </div>
  </div>

</template>
<script>
import PaperTable from 'components/UIComponents/PaperTable.vue'
export default {
  components: {
    PaperTable
  },
}
</script>
<style>
</style>
