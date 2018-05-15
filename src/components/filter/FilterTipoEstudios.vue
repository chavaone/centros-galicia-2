<template lang="html">
  <div class="filter">
    <h5>{{ $t('studiestype') }}</h5>
    <div class="estudiosList">
      <span v-for="tipo in tiposDeEstudios"
            :class="{active: checkedTiposDeEstudios.indexOf(tipo.cod) != -1}"
            @click="addOrDeleteEstudio(tipo .cod)">{{tipo.nombre}}</span>
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
$selected-color: darken(#007bff, 5%);
$unselected-color: lighten($selected-color, 10%);

  div.estudiosList {
    display: flex;
    flex-wrap: wrap;

    span {
      flex: 1 1 50%;
      padding: 0.2em 1em;
      border: #007bff solid 1px;
      background: $unselected-color;
      cursor: pointer;
      text-transform: uppercase;
      text-align: center;
      font-size: 0.8em;
      color:white;
      font-weight: bold;
    }

    span:nth-child(1) {
      border-top-left-radius: 0.2rem;
    }

    span:nth-child(2) {
      border-top-right-radius: 0.2rem;
    }

    span:last-child {
      border-bottom-left-radius: 0.2rem;
      border-bottom-right-radius: 0.2rem;
    }

    span.active {
      background: $selected-color;
    }

  }
</style>

<i18n>
  {
    "gl": {
      "studiestype": "Estudos:"
    }
  }
</i18n>
