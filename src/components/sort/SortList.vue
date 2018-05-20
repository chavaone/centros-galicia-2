<template lang="html">
  <div id="sort-list" :class="{custom : customSelected, horizontal: showTitle}">
    <h4>{{ $t('sort') }}</h4>
    <div class="sortSelect">
      <span v-for="(method, key) in availableMethods"
      @click="changeSort(method)"
      :class="{active: selectedMethod == method}"
      v-t="method.name"></span>
    </div>
    <div class="no-flex-fallback">
      <select v-model="selectedMethod" @change="changeSort" >
        <option v-for="(method, key) in availableMethods" :value="method" v-t="method.name"></option>
      </select>
    </div>
    <a href="#" @click="changeSort(selectedMethod)">
      <i class="fas fa-sync-alt"></i>
      {{ $t('resort')}}
    </a>
  </div>
</template>

<script>
import SortMethods from '../../assets/scripts/SortMethods.js';
import { eventBus } from '../../main.js';

export default {
  data () {
    return {
      availableMethods: {
        name: {
          name: 'sort-by-name',
          fun: SortMethods.sortByName
        },
        time: {
          name: 'sort-by-time',
          fun: SortMethods.sortByTime
        },
        distance: {
          name: 'sort-by-distance',
          fun: SortMethods.sortByDistance
        }
      },
      selectedMethod: null,
      customSelected: false
    }
  },
  props: {
    showTitle: {
      type: Boolean,
      default: true
    },
    sortRef: {
      type: String
    }
  },
  methods: {
    sort (centros) {
      if (! this.selectedMethod) return centros;
      return centros.sort(this.selectedMethod.fun);
    },
    changeSort(method){
      this.selectedMethod = method;
      this.customSelected = false;
      eventBus.$emit('filterOrSortChanged', this.sortRef);
    },
    setCustomSort() {
      this.customSelected = true;
    }
  }
}
</script>

<style lang="scss" scoped>

  $selected-color: darken(#007bff, 5%);
  $unselected-color: lighten($selected-color, 10%);
  $custom-selected-color: lighten($selected-color, 10%);
  $custom-unselected-color: lighten($unselected-color, 10%);

  h4 {
    display: inline;
    font-size: 0.9em;
  }

  a {
    display: none;
  }

  div.sortSelect {
    display: none;
  }


 @supports (display:flex) {

   div.no-flex-fallback {
     display: none;
   }

  div.sortSelect {
    display: inline-flex;

    span {
      padding: 0.2em 1em;
      border: #007bff solid 1px;
      background: $unselected-color;
      cursor: pointer;
      text-transform: uppercase;
      font-size: 0.8em;
      color:white;
      font-weight: bold;
    }

    span.active {
      background: $selected-color;
    }

    span:first-child {
      border-top-left-radius: 0.2rem;
      border-bottom-left-radius: 0.2rem;
    }

    span:last-child {
      border-top-right-radius: 0.2rem;
      border-bottom-right-radius: 0.2rem;
    }
  }

  div.custom {

    a {
      margin-left: 0.5em;
      display: inline-block;
      text-align: center;
    }

    span {
      background-color: $custom-unselected-color;
      color: #e3e3e3;
    }
    span.active {
      background-color: $custom-selected-color;
    }
  }

  .horizontal {

    margin-bottom: 1em;

    h4 {
      display: block;
      font-size: 1.5rem;
    }

    div.sortSelect {
      display: flex;
      flex-direction: column;
      align-content: center;
      text-align: center;

      span {
        padding: 0.75em;
        margin-bottom: 0.2em;
        border-radius: 0.2rem;
      }
    }

    s {
      margin-top: 0.5em;
    }

  }
}
</style>

<i18n>
  {
      "gl": {
        "sort": "Ordenar:",
        "resort": "Reordenar",
        "sort-by-name": "Nome",
        "sort-by-time": "Tempo",
        "sort-by-distance": "Distancia"
      },
      "es": {
        "sort": "Ordenar:",
        "resort": "Reordenar",
        "sort-by-name": "Nombre",
        "sort-by-time": "Tiempo",
        "sort-by-distance": "Distancia"
      }
  }
</i18n>
