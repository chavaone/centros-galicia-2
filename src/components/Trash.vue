<template lang="html">
  <div>
    <span>
      <a class="nav-link" href="#" data-toggle="modal" data-target="#trashModal">
        <i class="fa fa-trash"></i>
        <span>{{trashedCentros.length}}</span>
      </a>
    </span>
    <div class="modal fade"
         id="trashModal"
         tabindex="-1"
         role="dialog"
         aria-labelledby="trashLabel"
         aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="trashLabel">{{$t('trash-title')}}</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <div class="">
              <AQDCenter v-for="centro in trashedCentros" :centro="centro" :key="centro.cod"></AQDCenter>
              <p v-if="trashedCentros.length == 0">{{$t('no-centers')}}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { eventBus } from '../main.js'
import Center from './Center.vue'

export default {
  data() {
    return {
      trashedCentros: []
    }
  },
  methods: {
    addRemoveCenter(center) {
      var index = this.trashedCentros.indexOf(center);
      if (index == -1) {
        this.trashedCentros.push(center);
      } else {
        this.trashedCentros.splice(index, 1);
      }
    },
    filter (center) {
      return this.trashedCentros.indexOf(center) == -1;
    }
  },
  created() {
    eventBus.$on('trashcenter', this.addRemoveCenter);
  },
  components: {
    'AQDCenter': Center
  }
}
</script>

<style lang="scss" scoped>
  @media (min-width: 800px) {
    .modal-dialog {
      width: 50vw !important;
    }
  }
</style>

<i18n>
  {
    "gl" : {
      "trash-title": "Centros no Lixo",
      "no-centers": "Non hai centros no lixo."
    },
    "es" : {
      "trash-title": "Centros en la papelera",
      "no-centers": "No hay centros en la papelera."
    }
  }
</i18n>
