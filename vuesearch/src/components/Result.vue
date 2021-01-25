<template>
  <b-container fluid class="justify-content-center mb-5">
    <b-form-row class="my-1">
      {{ this.title }}
    </b-form-row>


    <b-form-row class="my-1">
      <b-link :href="url">{{ this.url }}</b-link>
    </b-form-row>
    
    <b-form-row class="my-1">
      {{ this.text }}
    </b-form-row>

    <b-form-row class="my-1">
      Last Mod: {{ this.lastmod }}
    </b-form-row>

    <b-form-row class="my-1">
      Access Date: {{ this.accessdate }}
    </b-form-row>
  </b-container>
</template>

<script>
export default {
  name:"Result",

  props: {
    url: { type: String, required: true},
    title: { type: String, required: true },
    lastmod: { type: Date },
    text: { type: String },
    accessdate: { type: Date }
  },

  mounted() {
    console.log(this.url);
  }
}

</script>

<style scoped>
</style>
