<template lang="html">
  <div class="filter">
    <h5>{{ $t('provinces') }}</h5>
    <div class="form-check" v-for="(provincia, key) in provincias">
      <input type="checkbox" class="form-check-input" :value="provincia" :id="key + '-checkbox'" v-model="checkedProvincias" @change="">
      <label class="form-check-label" :for="key + '-checkbox'">{{provincia}}</label>
    </div>
  </div>
</template>

<script>
export default {
  data : function() {
    return {
      provincias: {
        'acoruna': 'A Coruña',
        'lugo': 'Lugo',
        'ourense': 'Ourense',
        'pontevedra': 'Pontevedra'
      },
      checkedProvincias: [
        'A Coruña',
        'Lugo',
        'Ourense',
        'Pontevedra'
      ]
    };
  },
  methods: {
    filter(centro) {
      return centro.provincia in this.checkedProvincias;
    }
  }
}
</script>

<style lang="scss">

</style>

<i18n>
  {
    "gl": {
      "provinces": "Provincias:"
    }
  }
</i18n>
