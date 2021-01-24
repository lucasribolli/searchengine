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

      <Result></Result>

      <b-row>
        <b-col md="6" class="my-1">
          <b-pagination
            @change="changePagination"
            :total-rows="rows"
            :per-page="perPage"
            v-model="currentPage"
            class="customPagination"
            align="center"
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
      perPage: 1,
      currentPage: 1
    }
  },
  methods: {
    search() {
      // alert("Searching for " + this.query);
      console.log("searching");
      axios
        .get(this.$api_search, {
          params: {
            search: this.query
          }
        })
        .then(response => {
          if(response.data.total > 0) {
            this.results = response.data.data.slice();
            console.log(this.results);
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