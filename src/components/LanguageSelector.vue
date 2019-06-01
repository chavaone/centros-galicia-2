<template lang="html">
  <div class="">
    <h4 v-html="$t('title')"></h4>
    <div class="customSelect">
      <span v-for="lang in existentLanguages"
      @click="changeLang(lang.cod)"
      :class="{active: selectedLanguage == lang.cod}"
      v-t="lang.name"></span>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      existentLanguages: [
        {
          cod: 'gl',
          name: this.$i18n.t('galician')
        },
        {
          cod: 'es',
          name: this.$i18n.t('spanish')
        }
      ],
      selectedLanguage: this.$i18n.locale
    };
  },
  computed: {
    notCurrentLanguages() {
      return this.existentLanguages.filter((lang) => {return lang.cod != this.$i18n.locale});
    }
  },
  methods: {
    changeLang(cod) {
      this.$locale = cod;
    }
  }
}
</script>

<style lang="scss" scoped>
  $selected-color: darken(#007bff, 5%);
  $unselected-color: lighten($selected-color, 10%);
  $custom-selected-color: lighten($selected-color, 10%);
  $custom-unselected-color: lighten($unselected-color, 10%);

  div.customSelect {
    display: inline-flex;

    span {
      padding: 0.2em 1em;
      border: #007bff solid 1px;
      background: $unselected-color;
      cursor: pointer;
      text-transform: uppercase;
      font-size: 0.8em;
      color:white;
      font-weight: bold;
    }

    span.active {
      background: $selected-color;
    }

    span:first-child {
      border-top-left-radius: 0.2rem;
      border-bottom-left-radius: 0.2rem;
    }

    span:last-child {
      border-top-right-radius: 0.2rem;
      border-bottom-right-radius: 0.2rem;
    }
  }
</style>

<i18n>
  {
    "gl": {
      "title": "Idioma",
      "galician": "Galego",
      "spanish": "Castelán"
    },
    "es": {
      "title": "Idioma",
      "galician": "Gallego",
      "spanish": "Castellano"
    }
  }
</i18n>
