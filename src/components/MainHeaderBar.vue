<template lang="html">
  <div>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
              <a class="navbar-brand" href="#">Centros Educativos de Galicia</a>

              <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#menuprincipal" aria-controls="menuprincipal" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>

              <div class="collapse navbar-collapse" id="menuprincipal">
                <ul class="navbar-nav justify-content-end ml-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="#" data-toggle="modal" data-target="#cambiarPosicionModal" @click="positionModalEnabled">
                          {{ $t('change-coords') }}
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#" data-toggle="modal" data-target="#cambiarExportarCentros" :class="{disabled: activeCenters.length == 0}">
                          {{ $t('export-center') }}
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#" data-toggle="modal" data-target="#settingsModal">
                          {{ $t('settings') }}
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#" data-toggle="modal" data-target="#aboutModal">
                          {{ $t('about') }}
                        </a>
                    </li>
                </ul>

              </div>
    </nav>
    <AQDModalChangePosition :position="position"></AQDModalChangePosition>
    <AQDModalExportCenters :centers="activeCenters"></AQDModalExportCenters>
    <AQDAboutModal></AQDAboutModal>
    <AQDModalSettings></AQDModalSettings>
  </div>
</template>

<script>
import ModalChangePosition from './ModalChangePosition.vue'
import ModalExportCenters from './ModalExportCenters.vue'
import ModalAbout from './ModalAbout.vue'
import ModalSettings from './ModalSettings.vue'


import { eventBus } from '../main.js';

export default {
  props: {
    position: Object,
    activeCenters: Array,
    language: String
  },
  components: {
    'AQDModalChangePosition': ModalChangePosition,
    'AQDModalExportCenters': ModalExportCenters,
    'AQDModalSettings': ModalSettings,
    'AQDAboutModal': ModalAbout
  },
  methods: {
    positionModalEnabled() {
      eventBus.$emit('positionModalEnabled');
    }
  }
}
</script>

<style lang="scss">

</style>

<i18n>
  {
    "gl": {
      "change-coords": "Cambiar Localización",
      "export-center": "Exportar Centros",
      "about": "Axuda e Contacto",
      "settings": "Preferencias"
    },
    "es": {
      "change-coords": "Cambiar Localización",
      "export-center": "Exportar Centros",
      "about": "Ayuda y Contacto",
      "settings": "Preferencias"
    }
  }
</i18n>
