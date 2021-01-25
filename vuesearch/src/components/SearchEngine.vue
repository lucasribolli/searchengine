<template>
  <div>
    <b-container fluid>
      <b-row class="my-1">
        <b-col sm="10">
          <b-form-input
            id="q"
            type="search"
            v-model="query"
            placeholder="Search"
            @keyup.enter="search">
          </b-form-input>
        </b-col>
      </b-row>

      <div class="d-flex justify-content-center mb-5">
        <b-spinner 
          v-if="loading"
        ></b-spinner>
      </div>

      <Result v-for="result in results"
        :key="result.url"
        v-bind:url="result.url"
        v-bind:title="result.title"
        v-bind:lastmod="result.lastmod"
        v-bind:text="result.text"
        v-bind:accessdate="result.accessdate"
      ></Result>

      <b-row>
        <b-col md="6" class="my-1">
          <b-pagination
            v-if="showPagination"
            @change="changePagination"
            :total-rows="rows"
            :per-page="perPage"
            v-model="currentPage"
            align="center"
            class="customPagination"
          />
        </b-col>
      </b-row>
      
    </b-container>
  </div>
</template>

<script>
import Result from "@/components/Result.vue";
import axios from 'axios';

export default {
  components: {
    Result
  },
  data() {
    return {
      results: [],
      rows: 5,
      query: '',
      showPagination: false,
      perPage: 1,
      currentPage: 1,
      loading: false
    }
  },
  methods: {
    search() {
      this.loading = true;
      axios
        .get(this.$api_search, {
          params: {
            search: this.query
          }
        })
        .then(response => {
          this.loading = false;
          if(response.data.total > 0) {
            this.results = response.data.data.slice();
            // for (let index = 0; index < this.results.length; index++) {
            //   console.log(this.results[index].url);
            // }
            this.showPagination = true;
          }
          else {
            console.log("No response.");
          }
        })
        .catch(error => console.error(error));
    },
    changePagination() {
      console.log(this.currentPage);
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
  
  /* .pagination {
    width: 50%;
    padding: 15px 22px;
    margin: 8px 0;
    box-sizing: border-box;
    font-size: 20px;
    font-family: fantasy;
  } */
</style>