<template lang="html">
  <div id="sort-list">
    <h4>{{ $t('sort') }}</h4>
    <select v-model="selectedMethod" @change="changeSort">
      <option v-for="(method, key) in availableMethods" :value="method">{{method.name}}</option>
    </select>
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
          name: this.$i18n.t('sort-by-name'),
          fun: SortMethods.sortByName
        },
        time: {
          name: this.$i18n.t('sort-by-time'),
          fun: SortMethods.sortByTime
        },
        distance: {
          name: this.$i18n.t('sort-by-distance'),
          fun: SortMethods.sortByDistance
        },
      },
      selectedMethod: null
    }
  },
  methods: {
    sort (centros) {
      if (! this.selectedMethod) return centros;
      return centros.sort(this.selectedMethod.fun);
    },
    changeSort(){
      eventBus.$emit('filterOrSortChanged');
    }
  }
}
</script>

<style lang="css">
</style>

<i18n>
  {
      "gl": {
        "sort": "Ordenar",
        "sort-by-name": "Ordenar por nome",
        "sort-by-time": "Ordenar por tempo",
        "sort-by-distance": "Ordenar por distancia"
      }
  }
</i18n>
