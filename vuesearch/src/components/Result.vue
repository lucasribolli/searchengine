<template>
  <div class="result-content">
    <div class="result-info">
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
  }
}

</script>

<style scoped>
  .result-content {
    /* display:flex; */
    width: 80%;
    text-align: left;
    max-width: 800px;
    margin: 2rem auto;
    font-family: Roboto;
  }

  .result-url {
    position: relative;
    /* width: 50%; */
    bottom: 1px;
  }

  .result-text {
    font-size: 15px;
    text-align:justify;
    margin: -12px 0 0 0;
  }

  .result-date {
    font-size: 12px;
    padding-top: 5px;
    /* line-height: 100%; */
  }
</style>
