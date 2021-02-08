<template>
  <div>
    <img @click="goToRoot" class="logo" src="../assets/logo.png"/>
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

    <div v-if="loading" class="spinner">
      <b-spinner 
      ></b-spinner>
    </div>

    <div
      v-if="showResult"
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
      <div 
      class="pagination">
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
  props: {
    q: { type: String}
  },
  data() {
    return {
      results: [],
      total: 0,
      query: null,
      showResult: false,
      page: 0,
      loading: false,
      showWarning: false,
      warningMessage: {}
    }
  },
  mounted(){
    this.query = this.q;
    this.search();
  },
  methods: {
    search() {
      if (this.query) {
        this.showResult = false;
        this.showWarning = false;
        this.loading = true;
        axios
          .get(this.$api_search + `?q=` + this.query +`&page=` + this.page)
          .then(response => {
            this.showResult = true;
            this.loading = false;
            if(response.data.total > 0) {
              this.results = response.data.data.slice();
              this.total =  response.data.total;
              this.$router.push({ name: 'search', params: { q: this.query } });
            }
          })
          .catch(error => {
            this.loading = false;
            console.log(error.response);
            if (error.response) {
              this.warning(error.response.status);             
            }
            else {
              this.warning();
            }
        });
      }
    },
    changePagination(action) {
      if (action == "next" && (this.page + Const.PER_PAGE + 1) < this.total) {
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
    warning(code) {
      this.showResult = false;
      this.showWarning = true;
      if (code) {
        if (code === 404) {
          this.warningMessage.code = code;
          this.warningMessage.message = "I'm sorry, the query was not found.";
          this.$router.push({ name: 'warning', params: { code: code } });
        }
      } else {
        this.warningMessage.code = 500;
        this.warningMessage.message = "I'm sorry, something unexpected has happened.";
        this.$router.push({ name: 'warning', params: { code: this.warningMessage.code } });
      }
    },
    goToRoot() {
      this.$router.push({ name: 'vuesearch'});
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
</style>