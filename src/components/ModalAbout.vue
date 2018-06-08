<template lang="html">
  <div class="modal fade"
       id="aboutModal"
       tabindex="-1"
       role="dialog"
       aria-labelledby="aboutModalLabel"
       aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="aboutModalLabel">{{ $t('title')}}</h5>
          <button type="button" class="close" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <p v-html="$t('licencia-codigo', {url:'https://github.com/chavaone/centros-galicia-2'})"></p>
          <p v-html="$t('desarrollador', {email: 'marcos.chavarria [at] edu.xunta [dot] es'})"></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
}
</script>

<style lang="scss">
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
      "title": "Sobre este aplicativo",
      "licencia-codigo": "O aplicativo 'Centros Educativos de Galicia' é Software Libre licenciado baixo GPL-v3. O seu código fonte está dispoñible en GitHub no repositiorio <a href='{url}'>chavaone/centros-galicia-2</a>",
      "desarrollador": "O principal desenvolvedor deste software é Marcos Chavarría Teijeiro e podes contactar con el empregando o enderezo de correo electrónico {email}."
    },
    "es": {
      "title": "Sobre esta aplicación",
      "licencia-codigo": "La aplicación 'Centros Educativos de Galicia' es Software Libre licenciado baixo GPL-v3. Su código fuente está disponible en GitHub en el repositiorio <a href='{url}'>chavaone/centros-galicia-2</a>",
      "desarrollador": "El principal desarrollador de este software es  Marcos Chavarría Teijeiro y puedes contactar con él usando la dirección de correo electrónico {email}."
    }
  }
</i18n>
-->
