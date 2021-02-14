<template>
  <div>
    <img
      class="logo" 
      src="../assets/logo.png"/>
    <div class="search">
      <b-form-input
        id="q"
        type="search"
        v-model="query"
        @keyup.enter="search">
      </b-form-input>
    </div>
  </div>
</template>

<script>
export default {
    name: 'VueSearch',
    data() {
      return {
        query: ''
      }
    },
    methods: {
      search() {
        if (this.query) {
          this.$router.push(
            { name: 'search', params: { q: this.query } }
          );
        }
      }
    },
    mounted() {
      this.$router.replace({ path: '*', redirect: '/' });
    }
}
</script>

<style scoped>
  .logo{
    display: block;
    width:360px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 0px;
    margin-top: 60px;
  }

  input[type=search] {
    display: block;
    width: 360px;

    padding: 15px 18px;
    width: 100%;
    font-size: 20px;
    font-family: Roboto;
  }

  .search {
    max-width: 800px;
    margin-top: 10px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 0px;
  }
</style>