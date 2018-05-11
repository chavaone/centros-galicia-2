<template>
  <div id="app" class="container">
    <main>
      <aside class="collapse">
        <form>
          <div id="sort-list">

          </div>
          <div id="filter-list">
            <component v-for="filter in activeFilters" :is="filter" :ref="filter" :key="filter"></component>
          </div>
        </form>
      </aside>
      <section id="lista-centros">
        <AQDCenter v-for="centro in activeCenters" :centro="centro" :key="centro.cod"></AQDCenter>
      </section>
    </main>
    <footer>

    </footer>
  </div>
</template>

<script>
import { eventBus } from './main.js'

//Components
import Center from './components/Center.vue'
import FilterProvincia from './components/filter/FilterProvincia.vue'
import listaCentros from './assets/scripts/db/centros.js'

export default {
  name: 'app',
  data () {
    return {
      activeFilters: [
        'AQDFilterProvincia'
      ],
      activeCenters: []
    }
  },
  components: {
    'AQDCenter': Center,
    'AQDFilterProvincia': FilterProvincia
  },
  methods: {
    loadCenters() {
      var centros = listaCentros;
      for(var i = 0; i < this.activeFilters.length; i++) {
        centros = centros.filter(this.$refs[this.activeFilters[i]][0].filter)
      }
      this.activeCenters =  centros;
    }
  },
  created() {
    eventBus.$on('filterChanged', this.loadCenters);
  }
}
</script>

<style lang="scss">
@import '../node_modules/bootstrap/scss/bootstrap.scss';

#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
