<template lang="html">
  <article :data-cod="centro.cod">
        <div class="info">
            <header>
                <h3 class="name">{{centro.nombre}}</h3>
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
                <dt>{{ $t('num-linhas') }}</dt>
                <dd>3</dd>
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

<style lang="scss" scoped>
@import "./../assets/styles/mixins.scss";

article {
  @include make-box;
  margin-bottom: 1em;

  display: grid;
  grid-column-gap: 20px;
  grid-template-columns: [start-center] 1fr [start-button] 30px [end-center];
  grid-template-rows: [start-center] 110px [start-info] 1fr [end-center];

  .botones {
      grid-column: start-button / end-center;
      grid-row: start-center / start-info;
  }

  .info {
      grid-column: start-center / start-button;
      grid-row: start-center / start-info;

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
    grid-column: start-center / end-center;
    grid-row: start-info / end-center;

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
      "num-linhas": "Liñas"
    }
  }
</i18n>
