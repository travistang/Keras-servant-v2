<!-- Wrapping the StatsCard component around-->
<template>
  <div>
    <stats-card>
      <div :class="iconClass" slot="header">
        <i :class="icon"></i>
      </div>
      <div class="numbers" slot="content">
        <p>{{name}}</p>
        {{value}}
      </div>
      <div class="stats" slot="footer">
        <!-- <i class="ti-reload"></i> Updated now -->
      </div>
    </stats-card>
  </div>
</template>

<script>
import StatsCard from '../Cards/StatsCard'
export default {
  components: {
    StatsCard,
  },
  data() {

  },
  props: ["icon","iconClass","name","value"],
}

</script>

<style>
</style>
