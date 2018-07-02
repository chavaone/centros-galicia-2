<template>
  <div id="app" class="container">
    <div class="alert alert-primary" role="alert" v-if="! loadedDistances">
      {{ $t('loading-distances') }}
    </div>
    <div class="alert alert-primary" role="alert" v-if="! loadedTimes">
      {{ $t('loading-times') }}
    </div>
    <header>
      <AQDMainHeaderBar :position="position" :activeCenters="activeCenters"></AQDMainHeaderBar>
      <nav class="barra">
        <span class="info">{{ $t('number-centers', [currentPage + 1, totalPages, activeCenters.length]) }}</span>
        <AQDSortControl ref="sortBar" :sortRef="'sortBar'" :showTitle="false" id="sortBar"></AQDSortControl>
        <span class="boton">
          <a class="btn btn-primary" data-toggle="collapse" href="#asideSortFilter" role="button" aria-expanded="false" aria-controls="asideSortFilter">Filtros</a>
        </span>
        <AQDTrash ref="trash"></AQDTrash>
      </nav>
    </header>
    <main>
      <aside class="collapse" id="asideSortFilter">
        <form>
          <AQDSortControl ref="sortAside" :sortRef="'sortAside'"></AQDSortControl>
          <AQDFilterList ref="filterList"></AQDFilterList>
        </form>
      </aside>
      <AQDDraggable v-model="activeCenters" @change="setCustomSort()" :options="sortableoptions">
          <AQDCenter v-for="centro in paginatedActiveCenters" :centro="centro" :key="centro.cod"></AQDCenter>
      </AQDDraggable>
      <nav class="center-pagination">
        <ul class="pagination">
          <li class="page-item"
              :class="{disabled: currentPage == 0}">
            <a class="page-link" href="#" tabindex="-1" @click="currentPage--">{{ $t('anterior') }}</a>
          </li>
          <li v-for="page in totalPages"
              class="page-item"
              :class="{active: currentPage == page - 1}">
            <a  class="page-link"
                @click="currentPage = page - 1;"
            >{{page}}</a>
          </li>
          <li class="page-item" :class="{disabled: currentPage == totalPages - 1}">
            <a class="page-link" @click="currentPage++;">{{ $t('seguinte') }}</a>
          </li>
        </ul>
      </nav>
    </main>
    <footer>

    </footer>
  </div>
</template>

<script>
import { eventBus } from './main.js'
import OSMFunctions from './assets/scripts/OSMFunctions.js'
import MetaData from './assets/scripts/MetaDataValues.js'
import Config from './config.js'

//Components
import Draggable from 'vuedraggable'
import Center from './components/Center.vue'
import MainHeaderBar from './components/MainHeaderBar.vue'
import FilterList from './components/filter/FilterList.vue'
import SortList from './components/sort/SortList.vue'
import Trash from './components/Trash.vue'

export default {
  metaInfo: MetaData,
  data () {
    return {
      centers: [],
      activeCenters: [],
      position: {
        'lat': 43,
        'lon': -8
      },
      loadedDistances: false,
      loadedTimes: false,
      currentPage: 0,
      itemsPerPage: 100,
      resultCount: 0,
      sortableoptions: {
        handle: 'h3.name',
      }
    }
  },
  computed: {
    totalPages() {
      return Math.ceil(this.resultCount / Config.centersPerPage);
    },
    paginatedActiveCenters() {
      this.resultCount = this.activeCenters.length;

      if (this.currentPage >= this.totalPages) {
        this.currentPage = Math.max(0, this.totalPages - 1);
      }

      var index = this.currentPage * Config.centersPerPage;

      return this.activeCenters.slice(index, index + Config.centersPerPage);
    }
  },
  components: {
    'AQDDraggable': Draggable,
    'AQDCenter': Center,
    'AQDFilterList': FilterList,
    'AQDMainHeaderBar': MainHeaderBar,
    'AQDSortControl': SortList,
    'AQDTrash': Trash
  },
  methods: {
    loadCenters(origin) {

      if (origin.startsWith("sort")) {
        this.activeCenters = this.$refs[origin].sort(this.activeCenters);
      } else {
        this.activeCenters = this.$refs.filterList.filter(this.centers);
        this.activeCenters = this.activeCenters.filter(this.$refs.trash.filter);
      }
    },
    getLocation() {
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

      OSMFunctions.updateOSMTimes(this.centers, position, function () {
        self.loadedTimes = true;
      });

      OSMFunctions.updateOSMDistances(this.centers, position, function () {
        self.loadedDistances = true;
      });
    },
    setCustomSort() {
      this.$refs.sortAside.setCustomSort();
      this.$refs.sortBar.setCustomSort();
    },
    dbLoaded() {
      this.centers = raw_centers_db;
      this.activeCenters = this.centers;
      this.getLocation();
    }
  },
  created() {
    eventBus.$on('filterOrSortChanged', this.loadCenters);
    eventBus.$on('locationChanged', this.updateOSMData)

    var dbScript = document.createElement("script");
    dbScript.onload = this.dbLoaded;
    dbScript.src="/static/db.min.js";
    document.getElementById("app").appendChild(dbScript);
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
    align-items: center;
    justify-content: flex-start;

    .info {
      font-size:0.75em;
    }

    .boton {
      text-align: right;
      flex: 1;
    }

    #sortBar {
      display: none;
    }

    @include media-breakpoint-up(md) {
      .boton {
        display:none;
      }

      #sortBar {
        display: inline-block;
        text-align: right;
        flex: 1;
      }
    }
  }

  main {
    @include make-row();
    display: flex !important;

    aside {
      @include make-col-ready();
      @include make-col(12);
      margin-bottom: 1em;
      padding-right: 0;

      @include media-breakpoint-up(md) {
        @include make-col(3);
        display: inline-block !important;
      }
    }

    aside>form {
        @include make-box;

        @include media-breakpoint-up(md) {
            #sort-list {
              display: none;
            }
        }
    }

    &>div,
    &>.center-pagination {
        @include make-col-ready();
        @include make-col(12);

        @include media-breakpoint-up(md) {
            @include make-col(9);
        }
      }

      @include media-breakpoint-up(md) {
        &>.center-pagination {
          margin-left:25%;
        }
      }

      .pagination {
        justify-content: center;
        flex-wrap: wrap;
      }
  }

</style>

<i18n>
  {
    "gl": {
      "number-centers": "Amosando a páxina {0} de {1} para un total de {2} centros",
      "loading-times": "Estamos cargando os tempos dende a súa localización a cada centro. Espere por favor.",
      "loading-distances": "Estamos cargando as distancias dende a súa localización a cada centro. Espere por favor.",
      "seguinte": "Seguinte",
      "anterior": "Anterior"
    },
    "es": {
      "number-centers": "Mostrando la página {0} de {1} para un total de {2} centros",
      "loading-times": "Estamos cargando los tiempos de viaje desde su localización a cada centro. Espere por favor.",
      "loading-distances": "Estamos cargando la distancia desde su localización a cada centro. Espere por favor.",
      "seguinte": "Siguiente",
      "anterior": "Anterior"
    }
  }
</i18n>
