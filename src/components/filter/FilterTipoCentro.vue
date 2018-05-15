<template lang="html">
  <div class="filter">
    <h5>{{ $t('centertype') }}</h5>
    <div  class="form-check"
          v-for="tipo in tiposdecentro">
      <input  type="checkbox"
              class="form-check-input"
              :value="tipo" :id="tipo + '-checkbox'"
              v-model="checkedTiposdecentro"
              @change="filterChanged()">
      <label class="form-check-label"
      :for="tipo + '-checkbox'">
        {{tipo}}
      </label>
    </div>
  </div>
</template>

<script>
import { eventBus } from '../../main.js';

export default {
  data : function() {
    return {
      tiposdecentro: [
        'IES',
        'CEE',
        'CEIP',
        'CPI',
        'EPAPU',
        'CIFP',
        'EEI',
        'CEP',
        'CRA',
        'CFEA'
      ],
      checkedTiposdecentro: [
        'IES',
        'CEE',
        'CEIP',
        'CPI',
        'EPAPU',
        'CIFP',
        'EEI',
        'CEP',
        'CRA',
        'CFEA'
      ]
    };
  },
  methods: {
    filter(centro) {
      for(var i = 0; i < this.checkedTiposdecentro.length; i++) {
        if (centro.nombre.startsWith(this.checkedTiposdecentro[i]))
          return true;
      }
      return false;
    },
    filterChanged() {
      eventBus.$emit('filterOrSortChanged', 'filterTipoCentro');
    }
  }
}
</script>

<style lang="scss">
</style>

<i18n>
  {
    "gl": {
      "centertype": "Tipos de Centro:"
    }
  }
</i18n>
