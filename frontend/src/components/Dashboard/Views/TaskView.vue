<template>
  <div>
    <stats-card>
      <div class="icon-big text-center icon-success" slot="header">
        <i class="ti-alert"></i>
      </div>
      <div class="numbers" slot="content">
        <p>Loss</p>
        3.14
      </div>
      <div class="stats" slot="footer">
        <!-- <i class="ti-reload"></i> Updated now -->
      </div>
    </stats-card>
  </div>
</template>

<script>
  import StatsCard from '../../UIComponents/Cards/StatsCard'
export default {
  components: {
    'stats-card': StatsCard,
  },
  data(){},
}
</script>

<style>
</style>
