<template>
  <div id="app" class="container">
    <header>
      <AQDMainHeaderBar></AQDMainHeaderBar>
      <nav class="barra">
        <div class="info">
          <span>{{ $t('number-centers', [activeCenters.length]) }}</span>
        </div>
        <!-- Component Sort selector -->
        <!-- Component button sort filter -->
      </nav>
    </header>
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
import MainHeaderBar from './components/MainHeaderBar.vue'
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
    'AQDFilterProvincia': FilterProvincia,
    'AQDMainHeaderBar': MainHeaderBar
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
    this.loadCenters();
  }
}
</script>

<style lang="scss">
@import "./assets/styles/variables.scss";
@import "~bootstrap/scss/bootstrap.scss";
@import "./assets/styles/mixins.scss";

body {
    background-color: $background-color;
}

nav.barra {
  @include make-box;
  @include make-row;
  margin: 0.7em 0;
  padding: 0.35em 0;

  .info {
    @include make-col-ready;
    @include make-col(6);
    margin-top:7px;
    font-size:0.75em;
  }
}

main {
  @include make-row();
  display: flex !important;

  aside {
    @include make-col-ready();
    @include make-col(12);
    margin-bottom: 1em;

    @include media-breakpoint-up(sm) {
    @include make-col(3);
            display: inline-block !important;
    }
  }

  aside>form {
      @include make-box;
  }

  section {
      @include make-col-ready();
      @include make-col(12);

      @include media-breakpoint-up(sm) {
          @include make-col(9);
      }
    }
}
</style>

<i18n>
  {
    "gl": {
      "number-centers": "Seleccionados un total de {0} centros"
    }
  }
</i18n>
