<template>
  <div>
    <div class="col-lg-4">
      <stats-card
        icon="ti-alert"
        iconClass="icon-big text-center icon-danger"
        name="Loss"
      />
    </div>
    <div class="col-lg-4">
      <stats-card
        icon="ti-target"
        iconClass="icon-big text-center icon-success"
        name="Accuracy"
      />
    </div>
  </div>
</template>

<script>
  import StatsCard from '../../UIComponents/Tasks/StatsCard'
export default {
  components: {
    'stats-card': StatsCard,
  },
  data(){},
}
</script>

<style>
</style>
