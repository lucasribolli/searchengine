<template>
  <!-- <b-container fluid class="justify-content-center mb-5">
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
  </b-container> -->
  <div class="result-content">
    <div class="result-info" @click="openSource()">
        <h4 class="result-title"> {{ this.title }} </h4>
        <p class="result-url"> <b-link :href="url" target="_blank">{{ this.url }}</b-link> </p>
        <p class="result-text"> {{ this.text }} </p>
        <p class="result-date"> last mod: {{ this.lastmod }} | access date: {{ this.accessdate }} </p>
    </div>
  </div>
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

  methods: {
    openSource() {
      window.open(this.url, "_blank"); 
    }
  },

  mounted() {
    console.log(this.url);
  }
}

</script>

<style scoped>
  .result-content {
    /* display:flex; */
    width: 60%;
    text-align: left;
    max-width: 600px;
    margin: 2rem auto;
    font-family: Roboto;
  }

  .result-url {
    position: relative;
    /* width: 50%; */
    bottom: 1px;
  }

  .result-text {
    text-align:justify;
    margin: -12px 0 0 0;
  }

  .result-date {
    font-size: 12px;
    padding-top: 5px;
    /* line-height: 100%; */
  }
</style>
