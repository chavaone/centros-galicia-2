<template lang="html">
  <article :data-cod="centro.cod">
        <div class="info">
            <header>
                <h3 class="name">{{centro.nombre}}</h3>
                <h5 class="city">{{centro.concello}}, {{centro.provincia}}</h5>
            </header>
            <div class="travel-info">
                <span class="title">{{ $t('info-travel') }}</span>
                <span class="distancia"><i class="fas fa-route"></i>{{centro.osm.distancia | prettyDistance}}</span>
                <span class="tiempo"><i class="fas fa-clock"></i>{{centro.osm.tiempo | prettyTime}}</span>
            </div>
        </div>
        <div class="botones">
            <div class="btn-group pull-right btn-group-vertical" role="group" aria-label="Basic example">
              <button type="button" class="btn btn-sm btn-primary" @click="clipboard()"><i class="fa fa-clipboard"></i></button>
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
          hours = Math.floor(seconds / 3600),
          minutes = Math.floor((seconds % 3600) / 60),
          secs = (seconds % 3600) % 60;

          if (hours) {
              ret = hours.toString() + "h. ";
          }

          if (minutes) {
              ret = ret + minutes.toString() + "min. ";
          }

          if (seconds && ! ret) {
              ret = ret + secs.toString() + "s. ";
          }

      return ret;
    }
  },
  methods: {
    clipboard(){
      console.log(this.centro.cod);
    },
    trash(){
    }
  }
}
</script>

<style lang="scss">
@import "./../assets/styles/mixins.scss";
@import "~bootstrap/scss/bootstrap.scss";
article {
        @include make-box;
        @include make-row;
        margin: 0 0 0.75em 0;

        @include media-breakpoint-down(xs) {
            margin: 0 -10px;
        }

        .info {
            @include make-col-ready();
            @include make-col(11);

            @include media-breakpoint-down(xs) {
                @include make-col(10);
            }

            header {
                border-bottom: 1px solid rgba(0, 0, 0, 0.125);
                margin-bottom: 1em;

                @include media-breakpoint-up(sm) {
                    .name,.city {
                        display: inline;
                    }
                }

                .city {
                    font-style: italic;
                    font-size: 0.9em;
                    margin-left: 0.5em;
                }

                .city::before {
                    content: "(";
                }

                .city::after {
                    content: ")";
                }
            }

            .travel-info {

                padding-left: 30px;

                .title {
                    font-weight: bold;
                    margin-right: 0.5em;

                    @include media-breakpoint-down(xs) {
                        display: block;
                    }
                }

                .title::before {
                  //@include icon($icon-car);
                    margin-right: 0.3em;
                }

                .distancia,.tiempo {
                    font-style: italic;

                    svg {
                        margin-right: 0.2em;
                    }
                }
            }
        }

        .botones {
            @include make-col-ready();
            @include make-col(1);

            @include media-breakpoint-down(xs) {
                @include make-col(2);

                button {
                    padding: 0.4rem 0.8rem;
                    font-size: 1.1rem;
                    line-height: 1.5;
                    border-radius: 0.3rem;
                }
            }

        }

        .more-info {
            @include make-col-ready();
            @include make-col(12);
            margin-top: 1em;
            border-top: 1px solid rgba(0, 0, 0, 0.125);
            padding-top: 1em;

            dl {
                columns: 2;
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
