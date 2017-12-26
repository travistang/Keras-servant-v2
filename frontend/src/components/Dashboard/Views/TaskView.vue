<template>
  <div>
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
    <div class="col-lg-4">
      <stats-card
        icon="ti-target"
        iconClass="icon-big text-center icon-success"
        :objectId="objectId"
        attrName="acc"
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
      objectId: this.$route.params.id,
    }
  },



}
</script>

<style>
</style>
