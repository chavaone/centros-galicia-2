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
          <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
          <div class="centerList">
          <p>{{centersString}}</p>
          </div>
          <button type="button" name="button" v-clipboard:copy="centersString">Copiar a portapapeles</button>
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
  }
}

</script>

<style lang="scss">
  .modal-dialog {
    width: 75%;
    max-width: 100vw;
    max-height: 100vh;

    .centerList {
      width: 300px;
      height: 50%;
      overflow: scroll;
      margin:auto;
      word-wrap: break-word;
    }
  }
</style>

<i18n>
  {
    "gl": {

    }
  }
</i18n>
