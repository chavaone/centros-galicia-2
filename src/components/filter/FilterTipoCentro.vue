<template lang="html">
  <div class="filter">
    <h5>{{ $t('centertype') }}</h5>
    <div class="filterList">
      <span v-for="tipo in tiposdecentro"
            :class="{active: checkedTiposdecentro.indexOf(tipo) != -1}"
            @click="addOrDeleteTipoDeCentro(tipo)">{{tipo}}</span>
    </div>
    <div class="no-flex-fallback">
      <div class="form-check"
           v-for="tipo in tiposdecentro">
        <input  type="checkbox"
                class="form-check-input"
                :value="tipo" :id="tipo + '-checkbox'"
                v-model="checkedTiposdecentro"
                @change="filterChanged()">
        <label  class="form-check-label"
                :for="tipo + '-checkbox'">
          {{tipo}}
        </label>
      </div>
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
    },
    addOrDeleteTipoDeCentro(tipo) {
      var index = this.checkedTiposdecentro.indexOf(tipo);
      if(index == -1) {
        this.checkedTiposdecentro.push(tipo);
      } else {
        this.checkedTiposdecentro.splice(index, 1);
      }
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
