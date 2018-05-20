<template lang="html">
  <div class="modal fade"
       id="cambiarExportarCentros"
       tabindex="-1"
       role="dialog"
       aria-labelledby="cambiarExportarCentrosModalLabel"
       aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="cambiarExportarCentrosLabel">Exportar Centros</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <p v-html="$t('explicacion-1')"></p>
          <code class="codigos">{{centersString}}</code>
          <!-- <button type="button" name="button" @click="copy">Copiar a portapapeles</button>-->
          <p v-html="$t('explicacion-2')"></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    centers: Array
  },
  computed: {
    centersString () {
      return this.centers.map((center) => {return center.cod;}).join(" ");
    }
  },
  methods: {
    copy() {
      //TODO
    }
  }
}

</script>

<style lang="scss">
  .modal-dialog {
    width: 90vw !important;
    height: 90vh !important;

    max-height: 100%;
    max-width: 100%;

    code.codigos {
      display: block;
      height: 200px;
      overflow: scroll;
      margin: 1em;
    }
  }
</style>

<i18n>
  {
    "gl": {
      "explicacion-1": "No seguinte cadro podes ver os códigos de todos os centros que tiñas na lista por orde:",
      "explicacion-2": "Para gardar esta lista e empregala, copia os códigos anteriores seleccionándoos todos e premendo <kbd>Ctrl</kbd> + <kbd>C</kbd> ou a opción de copiar pulsando o botón dereito do rato."
    },
    "es": {
      "explicacion-1": "En el siguiente cuadro puedes ver los códigos de todos los centros que tenías en la lista por orden:",
      "explicacion-2": "Para guardar esta lista y usarla, copia los códigos anteriores seleccionándolos todos y pulsando <kbd>Ctrl</kbd> + <kbd>C</kbd> o la opción de copiar pulsando el botón derecho del ratón."
    }
  }
</i18n>
