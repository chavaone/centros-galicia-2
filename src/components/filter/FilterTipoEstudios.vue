<template lang="html">
  <div class="filter">
    <h5>{{ $t('studiestype') }}</h5>
    <div class="filterList">
      <span v-for="tipo in tiposDeEstudios"
            :class="{active: checkedTiposDeEstudios.indexOf(tipo.cod) != -1}"
            @click="addOrDeleteEstudio(tipo.cod)">{{tipo.nombre}}</span>
    </div>
    <div class="no-flex-fallback">
      <div class="form-check"
           v-for="tipo in tiposDeEstudios">
        <input  type="checkbox"
                class="form-check-input"
                :value="tipo.cod" :id="tipo.cod + '-checkbox'"
                v-model="checkedTiposDeEstudios"
                @change="filterChanged()">
        <label  class="form-check-label"
                :for="tipo.cod + '-checkbox'">
          {{tipo.nombre}}
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
      tiposDeEstudios: [
        {
          nombre: 'Infantil',
          cod: 'inf'
        },
        {
          nombre: 'Primaria',
          cod: 'pri'
        },
        {
          nombre: 'ESO',
          cod: 'eso'
        },
        {
          nombre: 'BAC',
          cod: 'bac'
        },
        {
          nombre: 'ESO de Adultos',
          cod: 'esa'
        },
        {
          nombre: 'BAC de Adultos',
          cod: 'baca'
        },
        {
          nombre: 'Educación Especial',
          cod: 'esp'
        }
      ],
      checkedTiposDeEstudios: []
    };
  },
  methods: {
    filter(centro) {
      for(var i = 0; i < this.checkedTiposDeEstudios.length; i++) {
        if (centro.ensinanzas.indexOf(this.checkedTiposDeEstudios[i]) != -1)
          return true;
      }
      return false;
    },
    filterChanged() {
      eventBus.$emit('filterOrSortChanged', 'filterTipoDeEstudios');
    },
    addOrDeleteEstudio(est) {
      var index = this.checkedTiposDeEstudios.indexOf(est);
      if(index == -1) {
        this.checkedTiposDeEstudios.push(est);
      } else {
        this.checkedTiposDeEstudios.splice(index, 1);
      }
      eventBus.$emit('filterOrSortChanged', 'filterTipoDeEstudios');
    }
  },
  created(){
    this.checkedTiposDeEstudios = this.tiposDeEstudios.map((c)=>{return c.cod;});
  }
}
</script>

<style lang="scss">
</style>

<i18n>
  {
    "gl": {
      "studiestype": "Estudos:"
    }
  }
</i18n>
