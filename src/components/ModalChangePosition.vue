<template lang="html">
  <div class="modal fade"
       id="cambiarPosicionModal"
       tabindex="-1"
       role="dialog"
       aria-labelledby="cambiarPosicionModalLabel"
       aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="cambiarPosicionModalLabel">{{ $t('title')}}</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <p>{{$t('explicacion')}}</p>
          <div class="aqd-map-container">
            <l-map ref="map" :zoom="zoom" :center="center" @click="mapClicked">
              <l-tile-layer :url="url" :attribution="attribution" ></l-tile-layer>
              <l-marker :lat-lng="marker"></l-marker>
              <v-geosearch :options="geosearchOptions"></v-geosearch>
            </l-map>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import L from 'leaflet';
import { eventBus } from '../main.js';
import { LMap, LTileLayer, LMarker } from 'vue2-leaflet';
import { OpenStreetMapProvider } from 'leaflet-geosearch';
import VGeosearch from 'vue2-leaflet-geosearch/Vue2LeafletGeosearch';

delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: '/static/marker-icon2.png',
  iconUrl: '/static/marker-icon2.png',
  shadowUrl: require('leaflet/dist/images/marker-shadow.png')
});

export default {
  props: {
    position: Object
  },
  components: {
      LMap,
      LTileLayer,
      LMarker,
      VGeosearch },
  data() {
    return {
      zoom:8,
      center: L.latLng(43, -8),
      url:'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      geosearchOptions: { // Important part Here
        provider: new OpenStreetMapProvider(),
        style: 'bar',
        searchLabel: this.$i18n.t('search-label'),
        marker: {                                           // optional: L.Marker    - default L.Icon.Default
          icon: L.icon({
            iconUrl: '/static/marker-icon3.png',
            iconSize: [25, 41],
            iconAnchor: [12, 41],
            popupAnchor: [1, -34]
          }),
          draggable: false,
        },
        maxMarkers: 6,
      },
    }
  },
  computed: {
    marker() {
      return L.latLng(this.position.lat, this.position.lon);
    }
  },
  methods:{
    changedLocation() {
      eventBus.$emit('locationChanged', this.position);
    },
    mapClicked(e){
      //Not move pointer if geosearch control is clicked.
      if(e.originalEvent.target.parentElement.parentElement.className.indexOf('geosearch') != -1 || e.originalEvent.target.parentElement.parentElement.parentElement.className.indexOf('geosearch') != -1) return;

      this.position.lat = e.latlng.lat;
      this.position.lon = e.latlng.lng;
      this.changedLocation();
    },
    //Leaflet thinks the map is tiny and renders the tiles very slowly. So we have to tell it to update the size
    fixRendering() {
      var self = this;
      setTimeout(function () {
        self.$refs.map.mapObject.invalidateSize();
      }, 500);
    }
  },
  created() {
    eventBus.$on('positionModalEnabled', this.fixRendering)
  }
}

</script>

<style lang="scss">
  @import "~leaflet/dist/leaflet.css";
  @import "~leaflet-geosearch/assets/css/leaflet.css";

  .aqd-map-container {
    width: 100%;
    height: 75vh;
  }

  .modal-dialog {
    width: 90vw !important;
    height: 90vh !important;
  }

</style>

<i18n>
  {
    "gl": {
        "title": "Cambiar Localización",
        "explicacion": "Para cambiar a localización fai click no mapa. O punteiro azul marca a localización actual da aplicación. Tamén podes empregar a barra de busca para procurar algunhas rúas. Unha vez atopada a posición que queres preme no mapa para marcala.",
        "search-label": "Introduza enderezo"
    }
  }
</i18n>
