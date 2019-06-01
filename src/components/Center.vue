<template lang="html">
  <article :data-cod="centro.cod" :class="{trashed: centro.trashed}">
        <div class="info">
            <header>
                <h3 class="name">{{centro.nome}}</h3>
                <h5 class="city">{{centro.concello}}, {{centro.provincia}}</h5>
              </header>
            <div class="travel-info">
                <span class="travel-info__title">{{ $t('info-travel') }}</span>

                <div class="travel-info__content">

                  <span class="travel-info__item">
                    <img class="svg-inline--fa fa-w-16" src="/static/route.svg"/>
                    {{prettyDistance}}
                    <span class="travel-info__itemmore" v-if="routeData.cat1">
                      <span v-if="routeData.cat1 && (routeData.cat1.distancia > 500 || (centro.osm.details.distance < 1000 && routeData.cat1.distancia > 0))">
                        <span class="cat-icon cat-icon--1">1</span>{{ beautifyDistance(routeData.cat1.distancia/1000)}}
                      </span>
                      <span v-if="routeData.cat2 && (routeData.cat2.distancia > 500 || (centro.osm.details.distance < 1000 && routeData.cat2.distancia > 0))">
                        <span class="cat-icon cat-icon--2">2</span>{{ beautifyDistance(routeData.cat2.distancia/1000)}}
                      </span>
                      <span v-if="routeData.cat3 && (routeData.cat3.distancia > 500 || (centro.osm.details.distance < 1000 && routeData.cat3.distancia > 0))">
                        <span class="cat-icon cat-icon--3">3</span>{{ beautifyDistance(routeData.cat3.distancia/1000)}}
                      </span>
                    </span>
                  </span>

                  <span class="travel-info__item">
                    <i class="fas fa-clock"></i>
                    {{prettyTime}}
                    <span class="travel-info__itemmore" v-if="routeData.cat1">
                      <span v-if="routeData.cat1 && (routeData.cat1.tiempo > 120 || (centro.osm.details.duration < 900 && routeData.cat1.tiempo > 0))">
                        <span class="cat-icon cat-icon--1">1</span><span>{{ beautifyTime(routeData.cat1.tiempo)}}</span>
                      </span>
                      <span v-if="routeData.cat2 && (routeData.cat2.tiempo > 120 || (centro.osm.details.duration < 900 && routeData.cat2.tiempo > 0))">
                        <span class="cat-icon cat-icon--2">2</span><span>{{ beautifyTime(routeData.cat2.tiempo)}}</span>
                      </span>
                      <span v-if="routeData.cat3 && (routeData.cat3.tiempo > 120 || (centro.osm.details.duration < 900 && routeData.cat3.tiempo > 0))">
                        <span class="cat-icon cat-icon--3">3</span><span>{{ beautifyTime(routeData.cat3.tiempo)}}</span>
                      </span>
                    </span>
                  </span>

                  <span class="travel-info__item" v-if="centro.osm.details">
                    <i class="fas fa-road"></i>
                    {{centro.osm.details.legs[0].summary}}
                  </span>
                </div>
            </div>
        </div>
        <div class="botones">
            <div class="btn-group pull-right btn-group-vertical" role="group" aria-label="Basic example">
              <button type="button"
                      class="btn btn-sm btn-primary"
                      v-clipboard:copy="centro.cod">
                      <i class="fa fa-clipboard"></i>
              </button>
              <button type="button" class="btn btn-sm btn-primary" @click="trash()"><i class="fa fa-trash"></i></button>
              <button type="button" class="btn btn-xs btn-primary" @click="getOSMDetails()" :class="{disabled: detailsCounter}"><i class="fas fa-map-signs"></i></button>
              <button class="btn btn-sm btn-primary" type="button" data-toggle="collapse" :data-target="'#info-cen-' + centro.cod" aria-expanded="false" :aria-controls="'info-cen-' + centro.cod"><i class="fa fa-info"></i></button>
            </div>
        </div>
        <div class="more-info collapse" :id="'info-cen-' + centro.cod">
            <dl>
              <div class="">
                <dt>{{ $t('enderezo') }}</dt>
                <dd>{{centro.enderezo}}
                  <a  target="_blank"
                      :href="'http://www.openstreetmap.org/?mlat=' + centro.coordenadas.lat + '&mlon=' + centro.coordenadas.lon + '&zoom=17'">
                    <i class="fa fa-map-marker-alt"></i>
                  </a>
                </dd>

              </div>
                <div v-if="centro.web.length > 0">
                  <dt>{{ $t('web') }}</dt>
                  <dd><a :href="centro.web">{{centro.web}}</a></dd>
                </div>
                <div>
                  <dt>{{ $t('email') }}</dt>
                  <dd><img :src="'/static/emails/' + centro.cod + '.png'" alt=""></dd>
                </div>
                <div v-if="centro.servizos.length > 0">
                    <dt>{{ $t('servizos') }}</dt>
                    <dd>{{ centro.servizos.join(', ') }}</dd>
                </div>
                <div>
                  <dt> {{$t('telefono')}}</dt>
                  <dd>{{ centro.tlf }}</dd>
                </div>
                <div v-if="centro.xornada.inf">
                  <dt> {{$t('xornada-inf')}}</dt>
                  <dd>{{ centro.xornada.inf }}</dd>
                </div>
                <div v-if="centro.xornada.prim">
                  <dt> {{$t('xornada-prim')}}</dt>
                  <dd>{{ centro.xornada.prim }}</dd>
                </div>
                <div v-if="centro.ensinanzas.bac">
                  <dt> {{$t('ramas-bac')}}</dt>
                  <dd>{{ centro.ensinanzas.bac | prettyRamas}}</dd>
                </div>
            </dl>
        </div>
    </article>
</template>

<script>
import { eventBus } from '../main.js'

export default {
  props: {
    centro: Object,
    detailsCounter: Date
  },
  computed: {
    prettyDistance() {
      if (! this.centro.osm) return "---";
      var distance = this.centro.osm.distancia;
      if (this.centro.osm.details) distance = this.centro.osm.details.distance/1000;
      return this.beautifyDistance(distance);
    },
    prettyTime () {
      if (! this.centro.osm) return "---";
      var seconds = this.centro.osm.tiempo;
      if (this.centro.osm.details) seconds = this.centro.osm.details.duration;
      return this.beautifyTime(seconds);
    },
    routeData() {
      if (! this.centro.osm.details) return {};

      var ret = {},
          steps = this.centro.osm.details.legs[0].steps.map(
            function(step) {
              return {
                distancia: step.distance,
                tiempo: step.duration,
                speed: step.distance / step.duration,
                ref: step.ref
              };
            });

      //CAT1 Autovías -> ref empeza por A
      var stepscat1 = steps.filter((step) => (step.ref && step.ref.startsWith('A')));
      ret.cat1 = this.reduceSteps(stepscat1);

      //CAT2 Non autovías e velocidade superior a 20m/s ~ 72Km/h
      var stepscat2 = steps.filter((step) => (! (step.ref && step.ref.startsWith('A')) && step.speed >= 20));
      ret.cat2 = this.reduceSteps(stepscat2);

      //CAT3 O Resto
      var stepscat3 = steps.filter((step) => (! (step.ref && step.ref.startsWith('A')) && step.speed < 20));
      ret.cat3 = this.reduceSteps(stepscat3);

      return ret;
    }
  },
  filters: {
      prettyRamas (obj) {
          var keys = (function(o){var ks=[]; for(var k in o) ks.push(k); return ks})(obj);
          return keys.join(", ");
      }
  },
  methods: {
    trash(){
      this.centro.trashed = ! this.centro.trashed;
      eventBus.$emit('trashcenter', this.centro);
    },
    getOSMDetails() {
      eventBus.$emit('centerdetails', this.centro);
    },
    beautifyDistance(distance) {
      if (distance < 1) {
          return (Math.floor(distance * 1000)).toString() + "m.";
      }
      return Math.floor(distance).toString() + "km.";
    },
    beautifyTime (seconds) {
      var ret = "",
          secondsInt = Math.floor(seconds),
          hours = Math.floor(secondsInt / 3600),
          minutes = Math.floor((secondsInt % 3600) / 60),
          secs = (secondsInt % 3600) % 60;

          if (hours) {
              ret = hours.toString() + "h.";
          }

          if (minutes) {
              ret = ret + minutes.toString() + "min.";
          }

          if (secondsInt && ! ret) {
              ret = ret + secs.toString() + "s.";
          }

      return ret;
    },
    reduceSteps (steps) {
      if (steps.length == 0) return {distancia: 0, tiempo: 0};
      return steps.reduce((step1, step2) => ({distancia: step1.distancia + step2.distancia, tiempo: step1.tiempo + step2.tiempo}));
    }
  }
}
</script>

<style lang="scss">
@import "./../assets/styles/mixins.scss";

article {
  @include make-box;
  margin-bottom: 1em;

  display: flex;
  flex-wrap: wrap;

  .botones {
      flex: 1 1 50px;
      display: flex;
      justify-content: center;
      .btn { font-size: 1.25em;}

  }

  @media (min-width: 760px) {
    .botones {
      .btn { font-size: 1em;}
    }
  }

  .info {
      flex: 1 1 calc(100% - 50px);

      header {
        border-bottom: 1px solid rgba(0, 0, 0, 0.125);
        margin-bottom: 1em;

        .city {
          font-style: italic;
          font-size: 0.9em;
        }

        .city::before {
          content: "(";
        }

        .city::after {
          content: ")";
        }
      }

      .travel-info {
        padding-left: 1em;

        &__title {
            font-weight: bold;
            margin-right: 0.5em;
        }

        &__content {
            display: inline-grid;
        }

        &__item {
          font-style: italic;

          svg {
              margin-right: 0.2em;
          }
        }

        &__itemmore {
          font-size:0.8em;
        }
      }

      .cat-icon {
        display: inline-block;
        height: 15px;
        width: 15px;

        margin-right: 1px;
        padding: 0;
        padding-bottom: 1px;
        border-radius: 100%;

        text-align: center;
        font-style: normal;
        font-size: 0.8em;
        font-weight: bold;
        color: white;

        &--1 {background-color: green}
        &--2 {background-color: orange}
        &--3 {background-color: red}
      }
  }

  .more-info {
    flex: 1 1 100%;

    margin-top: 1em;
    border-top: 1px solid rgba(0, 0, 0, 0.125);
    padding: 1em;


    dl {
      display: flex;
      flex-wrap: wrap;
      margin-bottom: 0;

      div {
        flex: 1 1 300px;
      }
    }
  }

  @media (min-width: 1000px) {
    grid-template-rows: [start-center] 95px [start-info] 1fr [end-center];

    .info {
      header>h3,
      header>.city {
        display: inline-block;
        margin-left: 0.5em;
      }
    }
  }

}

.mainCenterList article.trashed {
  display:none;
}
</style>

<i18n>
  {
    "gl": {
      "info-travel": "Info Viaxe:",
      "num-linhas": "Liñas",
      "xornada-inf": "Xornada de Educación Infantil",
      "xornada-prim": "Xornada de Educación Primaria",
      "telefono": "Teléfono",
      "fax": "Fax",
      "web": "Web",
      "email": "Enderezo email",
      "ramas-bac": "Ramas Bacharelato",
      "enderezo": "Enderezo",
      "servizos": "Servizos"
    },
    "es": {
      "info-travel": "Info Viaje:",
      "xornada-inf": "Jornada de Educación Infantil",
      "xornada-prim": "Jornada de Educación Primaria",
      "telefono": "Teléfono",
      "fax": "Fax",
      "web": "Web",
      "email": "Dirección email",
      "ramas-bac": "Ramas Bachillerato",
      "enderezo": "Direccioń",
      "servizos": "Servicios"
    }
  }
</i18n>
