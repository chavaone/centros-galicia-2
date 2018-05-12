<template>
  <div id="app" class="container">
    <div class="alert alert-primary" role="alert" v-if="! loadedDistances">
      {{ $t('loading-distances') }}
    </div>
    <div class="alert alert-primary" role="alert" v-if="! loadedTimes">
      {{ $t('loading-times') }}
    </div>
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
    <AQDModalChangePosition :position="position"></AQDModalChangePosition>
  </div>
</template>

<script>
import { eventBus } from './main.js'
import OSMFunctions from './assets/scripts/OSMFunctions.js'

//Components
import Center from './components/Center.vue'
import MainHeaderBar from './components/MainHeaderBar.vue'
import ModalChangePosition from './components/ModalChangePosition.vue'
import FilterProvincia from './components/filter/FilterProvincia.vue'
import listaCentros from './assets/scripts/db/centros.js'

window.Sortable = require('sortablejs');


export default {
  name: 'app',
  data () {
    return {
      activeFilters: [
        'AQDFilterProvincia'
      ],
      activeCenters: [],
      position: {
        'lat': 43,
        'lon': -8
      },
      loadedDistances: false,
      loadedTimes: false
    }
  },
  components: {
    'AQDCenter': Center,
    'AQDFilterProvincia': FilterProvincia,
    'AQDMainHeaderBar': MainHeaderBar,
    'AQDModalChangePosition': ModalChangePosition
  },
  methods: {
    loadCenters() {
      var centros = listaCentros;
      for(var i = 0; i < this.activeFilters.length; i++) {
        centros = centros.filter(this.$refs[this.activeFilters[i]][0].filter)
      }
      this.activeCenters =  centros;
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
    eventBus.$on('filterChanged', this.loadCenters);
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
