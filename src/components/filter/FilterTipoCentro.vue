<template lang="html">
  <div class="filter">
    <h5>{{ $t('centertype') }}</h5>
    <div class="">
      <div class="filterList">
        <span v-for="tipo in tiposdecentro"
              :class="{active: checkedTiposdecentro.indexOf(tipo) != -1}"
              @click="addOrDeleteTipoDeCentro(tipo)">{{tipo}}</span>
      </div>
      <div class="filterList action-buttons">
        <span @click="disableAll();">{{ $t('disable-all') }}</span>
        <span @click="enableAll();">{{ $t('enable-all') }}</span>
      </div>
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
        'CFEA',
        'CMUS',
        'EASD',
        'ESAD',
        'CDAN'
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
        'CFEA',
        'CMUS',
        'EASD',
        'ESAD',
        'CDAN'
      ]
    };
  },
  methods: {
    filter(centro) {
      for(var i = 0; i < this.checkedTiposdecentro.length; i++) {
        if (centro.nome.startsWith(this.checkedTiposdecentro[i]))
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
    },
    enableAll() {
      this.checkedTiposdecentro = this.tiposdecentro.slice(0);
      eventBus.$emit('filterOrSortChanged', 'filterTipoCentro');
    },
    disableAll() {
      this.checkedTiposdecentro = [];
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
      "centertype": "Tipos de Centro:",
      "disable-all": "Desactivar todas",
      "enable-all": "Activar todas"
    },
    "es": {
      "centertype": "Tipos de Centro:",
      "disable-all": "Desactivar todas",
      "enable-all": "Activar todas"
    }
  }
</i18n>
