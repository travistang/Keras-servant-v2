<template>
  <div>
    <div class="row">
      <div class="col-lg-4">
        <stats-card
          icon="ti-desktop"
          iconClass="icon-big text-center icon-success"
          :objectId="objectId"
          attrName="status"
        />
      </div>
      <div class="col-lg-4">
        <stats-card
          icon="ti-bar-chart"
          iconClass="icon-big text-center icon-success"
          :objectId="objectId"
          attrName="epoch"
          maxAttrName="total_epochs"
        />
      </div>
      <div class="col-lg-4">
        <stats-card
          icon="ti-alert"
          iconClass="icon-big text-center icon-danger"
          :objectId="objectId"
          attrName="loss"
        />
      </div>
    </div>

    <!-- 2nd row-->
    <div class="row">
      <div class="col-lg-6">
        <chart-card
          :objectId="objectId"
          :updateInterval="updateInterval"
          attrNames="loss"
        />
      </div>
      <div class="col-lg-6">
        <chart-card
          :objectId="objectId"
          :updateInterval="updateInterval"
          attrNames="acc"
        />
      </div>
    </div>
  </div>
</template>

<script>
  import store from '../../../store'
  import StatsCard from '../../UIComponents/Tasks/StatsCard'
  import ChartCard from '../../UIComponents/Tasks/ChartCard'
export default {
  components: {
    'stats-card': StatsCard,
    'chart-card': ChartCard,
  },
  data(){
    return {
      objectId: this.$route.params.id,
      updateInterval: 2000,
    }
  },



}
</script>

<style>
</style>
