<template>
  <div>
    <img style="width:360px; margin:14px 500px; text-align: center; margin-top: 60px;" src="../assets/logo.png"/>
    <div class="search">
      <b-form-input
        id="q"
        type="search"
        v-model="query"
        @keyup.enter="search">
      </b-form-input>
    </div>
    <a>http://localhost:8080/search:Python</a>
  </div>
</template>

<script>
export default {
    name: 'Home'
}
</script>

<style scoped>
  input[type=search] {
    width: 100%;
    padding: 15px 18px;
    margin: -30px 0 0 0;
    box-sizing: border-box;
    font-size: 20px;
    font-family: Roboto;
  }

  .search {
    max-width: 800px;
    margin: 2rem auto;
  }
</style>