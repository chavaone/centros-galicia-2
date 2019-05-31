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
          <h5 class="modal-title" id="cambiarExportarCentrosLabel" v-html="$t('title')"></h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <p v-html="$t('explicacion-1')"></p>
          <code id="listaCodigos" class="codigos" @copy="onCopy()">{{centersString}}</code>
          <div class="btn-group acciones" role="group" aria-label="Acciones">
            <a class="btn btn-primary" :href="'data:text/plain;charset=utf-8,' + encodeURIComponent(centersString)" :download="$t('download-txt-name')" v-html="$t('download-txt')"></a>
            <button class="btn btn-primary" type="button" name="button" @click="copy" v-html="$t('copy-clipboard')"></button>
            <button class="btn btn-primary" type="button" name="button" @click="downloadPDF" v-html="$t('download-pdf')"></button>
          </div>
        </div>
        <div id="pdftext" v-html="centersList"></div>
      </div>
    </div>
  </div>
</template>

<script>
import galite from 'ga-lite'
import jsPDF from 'jspdf'
export default {
  props: {
    centers: Array
  },
  computed: {
    centersString () {
      return this.centers.map((center) => {return center.cod;}).join(" ");
    },
    centersList () {
      return this.centers.map((center) => {return "<p>" + center.cod + " - " + center.nome + "</p>";}).join("");
    }
  },
  methods: {
    copy() {
      navigator.clipboard.writeText(this.centersString);
      galite('send', 'event', 'export', 'copyCodes');
    },
    downloadPDF() {
      var doc = new jsPDF();
      doc.fromHTML(document.getElementById('pdftext').innerHTML, 15, 15, {
        'width': 170
      });
      galite('send', 'event', 'export', 'downloadPDF');
      doc.save(this.$i18n.t('download-pdf-name'));
    },
    onCopy() {
      galite('send', 'event', 'export', 'copyCodes');
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

    .acciones {
      display: flex;
      margin: 1em 0;
      justify-content: center;
    }
  }
  #pdftext {
    display: none;
  }
</style>

<i18n>
  {
    "gl": {
      "download-txt": "Descargar como ficheiro de texto",
      "download-pdf": "Descargar como PDF",
      "download-txt-name": "centros.txt",
      "download-pdf-name": "centros.pdf",
      "title": "Exportar Centros",
      "copy-clipboard": "Copiar ó portapapeis",
      "explicacion-1": "No seguinte cadro podes ver os códigos de todos os centros que tiñas na lista por orde:"
    },
    "es": {
      "download-txt": "Descargar como ficheiro de texto",
      "download-pdf": "Descargar como PDF",
      "download-txt-name": "centros.txt",
      "download-pdf-name": "centros.pdf",
      "title": "Exportar Centros",
      "copy-clipboard": "Copiar al portapapeles",
      "explicacion-1": "En el siguiente cuadro puedes ver los códigos de todos los centros que tenías en la lista por orden:"
    }
  }
</i18n>
