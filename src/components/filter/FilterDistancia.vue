<template lang="html">
  <div class="filter">
    <h5>{{ $t('time') }}</h5>
    <span>{{prettyTime}}</span>
    <input type="range" :min="minvalue" :max="maxvalue" v-model="currentvalue" @change="filterChanged()">
  </div>
</template>

<script>
import { eventBus } from '../../main.js';

export default {
  data() {
    return {
      minvalue: -1,
      maxvalue: 360,
      defaultvalue: -1,
      currentvalue: -1
    };
  },
  computed: {
    prettyTime () {
      var minutos = this.currentvalue;
      if (minutos == -1) return this.$i18n.t("unlimited");
      var ret = "",
          hours = Math.floor(minutos / 60),
          minutes = Math.floor((minutos % 60));

          if (hours) {
              ret = hours.toString() + "h. ";
          }

          if (minutes) {
              ret = ret + minutes.toString() + "min. ";
          }

      return ret;
    }
  },
  methods: {
    filter(centro) {
      if (! centro.osm) return true;
      if (this.currentvalue == -1) return true;
      return (centro.osm.tiempo < this.currentvalue * 60);
    },
    filterChanged() {
      eventBus.$emit('filterOrSortChanged', 'filterTiempo');
    }
  }
}
</script>

<style lang="scss">
</style>

<i18n>
  {
    "gl": {
      "unlimited": "Ilimitado",
      "time": "Máximo Tempo en Coche:"
    },
    "es": {
      "unlimited": "Ilimitado",
      "time": "Máximo Tiempo en Coche:"
    }
  }
</i18n>
