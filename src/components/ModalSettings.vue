<template lang="html">
  <div class="modal fade"
       id="settingsModal"
       tabindex="-1"
       role="dialog"
       aria-labelledby="settingsModalLabel"
       aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="settingsModalLabel">{{ $t('title')}}</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <AQDLanguageSelector></AQDLanguageSelector>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LanguageSelector from './LanguageSelector.vue'

export default {
  components: {
    'AQDLanguageSelector': LanguageSelector,
  }
}
</script>

<style lang="scss" scoped>

p {
  text-align: justify;
  text-indent: 0.5em;
}

video,
img {
  display: block;
  margin: 0.5em auto;
}

.modal-dialog {
  width: 90vw !important;
  height: 90vh !important;
  max-height: 100%;
  max-width: 100%;
}

@media (min-width: 800px) {
  .modal-dialog {
    width: 750px !important;
  }
}

</style>


<i18n>
  {
    "gl": {
      "title": "Preferencias"
    },
    "es": {
      "title": "Preferencias"
    }
  }
</i18n>
