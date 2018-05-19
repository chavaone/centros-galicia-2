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
          nombre: this.$i18n.t('infantil'),
          cod: 'inf'
        },
        {
          nombre:  this.$i18n.t('primaria'),
          cod: 'pri'
        },
        {
          nombre:  this.$i18n.t('eso'),
          cod: 'eso'
        },
        {
          nombre:  this.$i18n.t('bac'),
          cod: 'bac'
        },
        {
          nombre:  this.$i18n.t('esa'),
          cod: 'esa'
        },
        {
          nombre:  this.$i18n.t('baca'),
          cod: 'baca'
        },
        {
          nombre:  this.$i18n.t('esp'),
          cod: 'esp'
        },
        {
          nombre:  this.$i18n.t('fp'),
          cod: 'fp'
        },
        {
          nombre:  this.$i18n.t('musica'),
          cod: ['mus', 'mus-sup']
        },
        {
          nombre:  this.$i18n.t('art-des'),
          cod: ['prof-art-des', 'sup-desenho']
        },
        {
          nombre:  this.$i18n.t('idiomas'),
          cod: "idiomas"
        },
        {
          nombre:  this.$i18n.t('dramatico'),
          cod: "sup-drama"
        }
      ],
      checkedTiposDeEstudios: []
    };
  },
  methods: {
    filter(centro) {
      for(var i = 0; i < this.checkedTiposDeEstudios.length; i++) {
        if (Array.isArray(this.checkedTiposDeEstudios[i])){
            for (var j = 0; j < this.checkedTiposDeEstudios[i].length; j++){
              if (centro.ensinanzas[this.checkedTiposDeEstudios[i][j]]) {
                return true;
              }
            }
        }
        if (centro.ensinanzas[this.checkedTiposDeEstudios[i]])
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
      "studiestype": "Estudos:",
      "infantil": "Infantil",
      "primaria": "Primaria",
      "eso": "ESO",
      "bac": "BAC",
      "esa": "ESO de Adultos",
      "baca": "Bacharelato de Adultos",
      "esp": "Educación Especial",
      "fp": "FP",
      "musica": "Música",
      "art-des": "Arte e Deseño",
      "idiomas": "Idiomas",
      "dramatico": "Arte Dramático"
    },
    "es": {
      "studiestype": "Estudos:",
      "infantil": "Infantil",
      "primaria": "Primaria",
      "eso": "ESO",
      "bac": "BAC",
      "esa": "ESO de Adultos",
      "baca": "Bachillerato de Adultos",
      "esp": "Educación Especial",
      "fp": "FP",
      "musica": "Música",
      "art-des": "Arte y Diseño",
      "idiomas": "Idiomas",
      "dramatico": "Arte Dramático"
    }
  }
</i18n>
