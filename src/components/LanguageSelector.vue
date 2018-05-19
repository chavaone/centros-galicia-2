<template lang="html">
  <li class="nav-item languages">
    <a v-for="lang in notCurrentLanguages" class="nav-link" @click="changeLang(lang.cod)">{{lang.cod}}</a>
  </li>
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
      ]
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

<style lang="css">
</style>

<i18n>
  {
    "gl": {
      "galician": "Galego",
      "spanish": "Castelán"
    },
    "es": {
      "galician": "Gallego",
      "spanish": "Castellano"
    }
  }
</i18n>
