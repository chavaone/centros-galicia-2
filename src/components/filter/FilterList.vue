<template lang="html">
  <div id="filter-list">
    <h4>{{ $t('filter-title') }}</h4>
    <component v-for="filter in activeFilters" :is="filter" :ref="filter" :key="filter"></component>
  </div>
</template>

<script>
import FilterProvincia from './FilterProvincia.vue'
import FilterTipoCentro from './FilterTipoCentro.vue'
import FilterTipoEstudios from './FilterTipoEstudios.vue'
import FilterDistancia from './FilterDistancia.vue'

export default {
  data() {
    return {
      activeFilters: [
        'AQDFilterProvincia',
        'AQDFilterTipoCentro',
        'AQDFilterTipoEstudios',
        'AQDFilterDistancia'
      ]
    };
  },
  components: {
    'AQDFilterProvincia': FilterProvincia,
    'AQDFilterTipoCentro': FilterTipoCentro,
    'AQDFilterTipoEstudios': FilterTipoEstudios,
    'AQDFilterDistancia': FilterDistancia
  },
  methods: {
    filter (centers) {
      var activeCenters = centers;
      for(var i = 0; i < this.activeFilters.length; i++) {
        activeCenters = activeCenters.filter(this.$refs[this.activeFilters[i]][0].filter)
      }
      return activeCenters;
    }
  }
}
</script>

<style lang="scss">
  @import "../../assets/styles/filters.scss";
</style>

<i18n>
  {
    "gl": {
      "filter-title": "Filtrar"
    }
  }
</i18n>
