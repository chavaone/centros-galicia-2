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
          <h5 class="modal-title" id="cambiarPosicionModalLabel">Cambiar Localización</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <div class="">
            <span>{{position}}</span>
          </div>
          <input type="text" v-model="position.lat" @change="changedLocation">
          <input type="text" v-model="position.lon" @change="changedLocation">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { eventBus } from '../main.js'

export default {
  props: {
    position: Object
  },
  data() {
    return {}
  },
  methods:{
    changedLocation() {
      eventBus.$emit('locationChanged', this.position);
    }
  }
}

</script>

<style lang="scss">
//  @import "~leaflet/dist/leaflet.css";

  .modal-dialog {
    width: 50%;
    max-width: 100vw;
    max-height: 100vh;
  }
</style>

<i18n>
  {
    "gl": {

    }
  }
</i18n>
