<template>
  <div>
    <img class="logo" src="../assets/logo.png"/>
    <div class="search">
      <b-form-input
        id="q"
        type="search"
        v-model="query"
        @keyup.enter="search">
      </b-form-input>
    </div>

    
    <Warning
      v-if="showWarning"
      v-bind:code="warningMessage.code"
      v-bind:message="warningMessage.message"
    ></Warning>

    <div class="spinner">
      <b-spinner 
        v-if="loading"
      ></b-spinner>
    </div>

    <div
      v-if="showComponent"
    >
      <Result id="result-component" 
        v-for="result in results"
        :key="result.id"
        v-bind:url="result.url"
        v-bind:title="result.title"
        v-bind:lastmod="result.lastmod"
        v-bind:text="result.text"
        v-bind:accessdate="result.accessdate"
      ></Result>
    </div>

    <!-- <div class="total" v-if="true">{{ this.total }} results</div> -->
    
    <div 
      class="pagination"
      v-if="pagination">
        <b-button
          size="lg"
          pill 
          variant="outline-dark"
          @click="changePagination('previous')"> ❮
        </b-button>
        <b-button
          size="lg"
          pill 
          variant="outline-dark"
          @click="changePagination('next')"> ❯
        </b-button>
    </div>
  </div>
</template>

<script>
import Const from "../const/config";
import Result from "@/components/Result.vue";
import Warning from "@/views/Warning";
import axios from 'axios';

export default {
  components: {
    Result,
    Warning
  },
  data() {
    return {
      results: [],
      total: 0,
      query: '',
      showPagination: false,
      showComponent: false,
      page: 0,
      loading: false,
      showWarning: false,
      warningMessage: {}
    }
  },
  methods: {
    search() {
      this.showComponent = false;
      this.showWarning = false;
      this.loading = true;
      axios
        .get(this.$api_search + `?q=` + this.query +`&page=` + this.page)
        .then(response => {
          this.showComponent = true;
          this.loading = false;
          if(response.data.total > 0) {
            this.showPagination = true;
            this.results = response.data.data.slice();
            this.total =  response.data.total;
          }
        })
        .catch(error => {
          this.loading = false;
          this.warning(error.response.status);
        });
    },
    changePagination(action) {
      if (action == "next" && this.page + Const.PER_PAGE < this.total) {
        console.log(this.total);
        console.log(this.page);
        this.page++;
        scrollTo(100, 0);
        this.search();
      }
      else if (action == "previous" && this.page > 0) {
        this.page--;
        scrollTo(100, 0);
        this.search();
      }
    },
    warning(status) {
      if (status === 404) {
        this.warningMessage.code = Const.WARNING.code;
        this.warningMessage.message = Const.WARNING.message;
        this.showComponent = false;
        this.showPagination = false;
        this.showWarning = true;
      }
    }
  },
  computed: {
    pagination() {
      if (this.total > Const.PER_PAGE) {
        return true;
      }
      return false;
    }
  }
}
</script>

<style scoped>
  .logo {
    width:200px;
    margin:14px 555px;
    /* text-align: center; */
    margin-top: 40px;
  }

  input[type=search] {
    width: 80%;
    padding: 15px 18px;
    margin: -30px 70px;
    box-sizing: border-box;
    font-size: 16px;
    font-family: Roboto;
    
    max-width: 800px;
    margin: 0rem auto;
  }

  .total {
    /* width: 192%; */
    font-size: 12px;
    font-family: Roboto;
  }

  .spinner {
    /* position: relative; */
    padding: 80px 560px;
    margin: -30px 70px;
  }

  .pagination {
    margin: 2rem auto;
    width: 10%;
    padding: 10px;
  }
  
  .pagination button{
    margin: 0px 5px;
    /* width: 50%; */
    box-sizing: border-box;
    font-size: 15px;
    /* font-family: Roboto; */
  }

  .warningCode{
    font-size: 50px;
    font-weight: 850;
    font-family: Roboto;
  }

  .warningMessage{
    font-size: 20px;
    font-weight: 500;
    font-family: Roboto;
  }
</style>