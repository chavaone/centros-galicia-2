<template lang="html">
  <div class="">
    <h4>{{ $t('welcome-message')}}</h4>
    <p>{{ $t('app-goal')}}</p>
    <p>{{ $t('inst1') }}</p>

    <div class="alert alert-primary" role="alert" v-if="! loadedDistances">
      {{ $t('loading-distances') }}
    </div>
    <div class="alert alert-primary" role="alert" v-if="! loadedTimes">
      {{ $t('loading-times') }}
    </div>

    <p>{{ $t('inst2') }}</p>

    <button class="btn btn-primary btn-lg" @click="loadCenters()" :class="{disabled: !loadedTimes || ! loadedDistances}">
      {{ $t('apply-filters') }}
    </button>

    <p>{{ $t('inst3') }}</p>

    <p>{{$t('disclaimer')}}</p>


  </div>
</template>

<script>
import { eventBus } from '../main.js'

export default {
  props: {
    welcome: Boolean,
    loadedDistances: Boolean,
    loadedTimes: Boolean
  },
  methods: {
    loadCenters() {
      eventBus.$emit('loadCenters');
    }
  }
}
</script>

<style lang="css" scoped>
  p {
    text-indent: 1em;
    text-align: justify;
  }

  button {
    margin: 1em auto;
    display: block;
    text-align: center;
  }

</style>

<i18n>
  {
    "gl": {
      "welcome-message": "Benvido a aplicación Centros Educativos de Galicia",
      "app-goal": "O obxectivo desta aplicación é facilitar a profesores e mestres do ensino público galego a participación nos concursos de elección de centros: o concurso xeral de translados (CXT) e o concurso de adxudicación de destinos provisionais (CADP).",
      "inst1": "Para empregar a aplicación primeiro marca a túa localización na opción do menú 'Cambiar Localización' ou permitindo que o teu navegador acceda a túa localización. Espera a que se carguen os datos relativos a túa localización.",
      "inst2": "A continuación selecciona os teus criterios de filtrado e ordenación empregando a barra lateral se estás nun ordenador ou o menú desplegable co botón 'Filtros' se empregas un móbil. Unha vez feito isto, preme no seguinte botón:",
      "inst3": "Cada vez que se modifiquen os filtros ou o criterio de ordenación, borrarase a lista de centros. Para gardar esta lista podes empregar a opción do menú 'Exportar Centros'.",
      "disclaimer": "Este programa pode ter erros. Así que antes de enviar a túa instancia do CAPD ou do CXT comproba que os datos aportados pola aplicación se corresponden coa realidade.",
      "loading-times": "Estamos cargando os tempos dende a súa localización a cada centro. Espere por favor.",
      "loading-distances": "Estamos cargando as distancias dende a súa localización a cada centro. Espere por favor.",
      "apply-filters": "Aplicar Filtros"
    },
    "es": {
      "welcome-message": "Bienvenido a la aplicación Centros Educativos de Galicia",
      "app-goal": "El objetivo de esta aplicación es facilitar a profesores y maestros de la enseñanza pública gallega la participación en los concursos de elección de centros: el concurso general de translados (CXT) y el concurso de adjudicación de destinos provisionales (CADP).",
      "inst1": "Para usar la aplciación primero selecciona tu localización en la opción del menú 'Cambiar Localización' o permitiendo que tu navegador acceda a tu localización. Espera a que se carguen los datos relativos a tu localización.",
      "inst2": "A continuación selecciona tus criterios de filtrado y ordenación usando la barra lateral, si estás en un ordenador; o el menú desplegable con  el botón 'Filtros', si usas un móbil. Una vez hecho esto, pulsa en el siguiente botón:",
      "inst3": "Cada vez que se modifiquen los filtros o el criterio de ordenación, se borra la lista de centros. Para guardar esta lista puedes emplear la opción do menú 'Exportar Centros'.",
      "disclaimer": "Este programa puede tener fallos. Así que antes de enviar tu instancia del CAPD o del CXT comprueba que los datos aportados por la aplicación se corresponden con la realidad.",
      "loading-times": "Estamos cargando los tiempos de viaje desde su localización a cada centro. Espere por favor.",
      "loading-distances": "Estamos cargando la distancia desde su localización a cada centro. Espere por favor.",
      "apply-filters": "Aplicar Filtros"
    }
  }
</i18n>
