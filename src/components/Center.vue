<template lang="html">
  <article :data-cod="centro.cod">
        <div class="info">
            <header>
                <h3 class="name">{{centro.nome}}</h3>
                <h5 class="city">{{centro.concello}}, {{centro.provincia}}</h5>
            </header>
            <div class="travel-info">
                <span class="title">{{ $t('info-travel') }}</span>
                <span class="distancia" v-if="centro.osm"><i class="fas fa-route"></i>{{centro.osm.distancia | prettyDistance}}</span>
                <span class="tiempo" v-if="centro.osm"><i class="fas fa-clock"></i>{{centro.osm.tiempo | prettyTime}}</span>
            </div>
        </div>
        <div class="botones">
            <div class="btn-group pull-right btn-group-vertical" role="group" aria-label="Basic example">
              <button type="button"
                      class="btn btn-sm btn-primary"
                      v-clipboard:copy="centro.cod"
                      v-clipboard:success="onCopy">
                      <i class="fa fa-clipboard"></i>
              </button>
              <button type="button" class="btn btn-sm btn-primary" @click="trash()"><i class="fa fa-trash"></i></button>
              <button class="btn btn-sm btn-primary" type="button" data-toggle="collapse" :data-target="'#info-cen-' + centro.cod" aria-expanded="false" :aria-controls="'info-cen-' + centro.cod"><i class="fa fa-info"></i></button>
            </div>
        </div>
        <div class="more-info collapse" :id="'info-cen-' + centro.cod">
            <dl>
                <dt>{{ $t('enderezo') }}</dt>
                <dd>{{centro.enderezo}}</dd>
                <template v-if="centro.web.length > 0">
                  <dt>{{ $t('web') }}</dt>
                  <dd><a :href="centro.web">{{centro.web}}</a></dd>
                </template>
                <dt>{{ $t('email') }}</dt>
                <dd><img :src="'/static/emails/' + centro.cod + '.png'" alt=""></dd>
                <template v-if="centro.servizos.length > 0">
                    <dt>{{ $t('servizos') }}</dt>
                    <dd>{{ centro.servizos.join(', ') }}</dd>
                </template>
                <dt> {{$t('telefono')}}</dt>
                <dd>{{ centro.tlf }}</dd>
                <template v-if="centro.xornada.inf">
                  <dt> {{$t('xornada-inf')}}</dt>
                  <dd>{{ centro.xornada.inf }}</dd>
                </template>
                <template v-if="centro.xornada.prim">
                  <dt> {{$t('xornada-inf')}}</dt>
                  <dd>{{ centro.xornada.prim }}</dd>
                </template>
                <template v-if="centro.ensinanzas.bac">
                  <dt> {{$t('ramas-bac')}}</dt>
                  <dd>{{ centro.ensinanzas.bac | prettyRamas}}</dd>
                </template>
            </dl>
        </div>
    </article>
</template>

<script>
import { eventBus } from '../main.js'

export default {
  props: {
    centro: Object
  },
  filters: {
    prettyDistance(distance) {
      if (distance < 1) {
          return (Math.floor(distance * 1000)).toString() + " m.";
      }
      return Math.floor(distance).toString() + " km.";
    },
    prettyTime (seconds) {
      var ret = "",
          secondsInt = Math.floor(seconds),
          hours = Math.floor(secondsInt / 3600),
          minutes = Math.floor((secondsInt % 3600) / 60),
          secs = (secondsInt % 3600) % 60;

          if (hours) {
              ret = hours.toString() + "h. ";
          }

          if (minutes) {
              ret = ret + minutes.toString() + "min. ";
          }

          if (secondsInt && ! ret) {
              ret = ret + secs.toString() + "s. ";
          }

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
    onCopy(){
      console.log(this.centro.cod);
    },
    trash(){
      eventBus.$emit('trashcenter', this.centro);
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

        .title {
            font-weight: bold;
            margin-right: 0.5em;
        }

        .distancia,.tiempo {
            font-style: italic;

            svg {
                margin-right: 0.2em;
            }
        }
      }
  }

  .more-info {
    flex: 1 1 100%;

    margin-top: 1em;
    border-top: 1px solid rgba(0, 0, 0, 0.125);
    padding: 1em;

    dl {
        columns: 2;
        margin-bottom: 0;
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
    }
    }
  }
</i18n>
