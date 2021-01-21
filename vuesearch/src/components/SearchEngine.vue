<template>
  <div>
    <b-container fluid>
      <b-row class="my-1">
        <b-col sm="10">
          <b-form-input
            id="searchtext"
            type="search"
            v-model="text"
            placeholder="Search">
          </b-form-input>
        </b-col>
      </b-row>
    </b-container>
    <Result></Result>
  </div>
</template>

<script>
import Result from "@/components/Result.vue";


export default {
  components: {
    Result
  },
  data() {
    return {
      text: ''
    }
  }
}
</script>

<style scoped>
  input[type=search] {
    width: 50%;
    padding: 15px 22px;
    margin: 8px 0;
    box-sizing: border-box;
    font-size: 20px;
    font-family: fantasy;
  }
</style>