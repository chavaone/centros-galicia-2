<template>
  <div id="app" class="container">
    <div class="alert alert-primary" role="alert" v-if="! loadedDistances">
      {{ $t('loading-distances') }}
    </div>
    <div class="alert alert-primary" role="alert" v-if="! loadedTimes">
      {{ $t('loading-times') }}
    </div>
    <header>
      <AQDMainHeaderBar :position="position" :activeCenters="activeCenters" :language="currentLanguage"></AQDMainHeaderBar>
      <nav class="barra">
        <div class="info">
          <span>{{ $t('number-centers', [activeCenters.length]) }}</span>
        </div>
        <AQDSortControl ref="sortBar" :sortRef="'sortBar'" :showTitle="false"></AQDSortControl>
        <a class="btn btn-primary" data-toggle="collapse" href="#asideSortFilter" role="button" aria-expanded="false" aria-controls="asideSortFilter">Ordenar y Filtrar</a>
      </nav>
    </header>
    <main>
      <aside class="collapse" id="asideSortFilter">
        <form>
          <AQDSortControl ref="sortAside" :sortRef="'sortAside'"></AQDSortControl>
          <AQDFilterList ref="filterList"></AQDFilterList>
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
import listaCentros from './assets/scripts/db/centros.js'
import OSMFunctions from './assets/scripts/OSMFunctions.js'

//Components
import Center from './components/Center.vue'
import MainHeaderBar from './components/MainHeaderBar.vue'
import FilterList from './components/filter/FilterList.vue'
import SortList from './components/sort/SortList.vue'

window.Sortable = require('sortablejs');


export default {
  name: 'app',
  data () {
    return {
      currentLanguage: 'gl',
      activeCenters: [],
      position: {
        'lat': 43,
        'lon': -8
      },
      loadedDistances: false,
      loadedTimes: false,
    }
  },
  components: {
    'AQDCenter': Center,
    'AQDFilterList': FilterList,
    'AQDMainHeaderBar': MainHeaderBar,
    'AQDSortControl': SortList
  },
  methods: {
    loadCenters(origin) {
      this.activeCenters = listaCentros;
      if (! origin.startsWith("sort")) {
        this.activeCenters = this.$refs.filterList.filter(this.activeCenters);
      } else {
        this.activeCenters = this.$refs[origin].sort(this.activeCenters);
      }
      this.doCentersSortable();
    },
    getLocation() {
      console.log("getLocation");
      var self = this;
      navigator.geolocation.getCurrentPosition (function(pos) {
            self.position = {
                lat: pos.coords.latitude,
                lon: pos.coords.longitude
            };
            eventBus.$emit('locationChanged', self.position);
        });
    },
    updateOSMData(position) {
      this.loadedTimes = false;
      this.loadedDistances = false;
      var self = this;

      OSMFunctions.updateOSMTimes(listaCentros, position, function () {
        self.loadedTimes = true;
      });

      OSMFunctions.updateOSMDistances(listaCentros, position, function () {
        self.loadedDistances = true;
      });
    },
    doCentersSortable() {
      var tabla = document.getElementById("lista-centros"),
          sortable = Sortable.create(tabla, {
            handle: 'header',
            ghostClass: 'ghost-sortable',
            animation: 100,
            delay: 20,
          });
    }
  },
  created() {
    eventBus.$on('filterOrSortChanged', this.loadCenters);
    eventBus.$on('locationChanged', this.updateOSMData)

    //this.loadCenters();
    this.getLocation();
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
      "number-centers": "Seleccionados un total de {0} centros",
      "loading-times": "Estamos cargando os tempos dende a súa localización a cada centro. Espere por favor.",
      "loading-distances": "Estamos cargando as distancias dende a súa localización a cada centro. Espere por favor."
    }
  }
</i18n>
