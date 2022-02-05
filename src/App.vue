<template>
  <div id="app">
    <portal to="destination">
      <img alt="3 circles logo" src="./assets/logo-white-icon-sm.png">
    </portal>
    <div class="app-wrapper">
      <div class="navbar-wrapper">
        <NavBar />
      </div>
      <portal-target name="destination"></portal-target>
      <b-form-input class="inputfield" v-model.lazy="search_term" placeholder="ex: @BarackObama"></b-form-input>
      <br/>
      <b-button variant="outline-primary" @click="searchDifferentiator(search_term)">Search</b-button> <span> </span>
      <b-button variant="outline-success" @click="downloadtoFile(tweets)">Download</b-button> <span> </span>
      <b-button variant="outline-success" @click="downloadSelected()">Download Selected</b-button> <span> </span>
      <b-button variant="outline-primary" @click="retrieveStockData()">Market</b-button>
      <div class="tweet-wrapper">
        <TweetCard :tweets="this.tweets" v-on:tweet-selected="updateSelected" />
      </div>
      <div class="grapher-wrapper"> <!-- TODO: finish graphing section and related features. Place inside conditionally rendered modal; implement correlation & wordcloud -->
          <Grapher :dataset="this.sap" :chart_options="this.chart_options" />
      </div>
    </div>
  </div>
</template>

<script>
import NavBar from './components/NavBar'
import TweetCard from './components/TweetCard'
import Grapher from './components/Grapher'
import axios from 'axios';
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

export default {
  name: 'App',
  components: {
    Grapher,
    NavBar,
    TweetCard
  },
  data() {                       // initializes important variables
    return {
      chart_options: {
        chart: {
          title: "Test title",
          subtitle: "test subtitle"
        }
      },
      sap: [["ID", "Open", "Close", "Volume", "Sentiment"],["AAPL", 178, 181, 200, 0.50],["AMD", 181, 182, 100, 0.55],["BTC", 182, 180, 150, 0.69],["ABC", 180, 183, 90, 0.58]], //placeholder values for testing GCharts
      search_term: '',
      selected: [],
      tweets: []
    }
  },
  computed: {},
  methods: {
    updateSelected (value_from_child) {
      if (this.selected.includes(value_from_child)) {
        let t = this.selected.indexOf(value_from_child)
        this.selected[t].classList.remove('selected')
        this.selected.splice(t, 1)
      }
      else {
        this.selected.push(value_from_child)
      }
    },
    downloadSelected: function() {
      let arr = []
      for (let n in this.selected) {
        let c = document.getElementById(this.selected[n].id)
        if (!(arr.includes(c.id))) {
          arr.push(c.id)
        }
      }
      let filtered_tweets = this.tweets.filter(tweet => arr.includes(JSON.stringify(tweet.id)))
      this.downloadtoFile(filtered_tweets)
    },
    downloadtoFile: function(content) {
      if (content) {
        let a = document.createElement('a')
        let b = new Blob([JSON.stringify(content, null, 4)], {type: 'application/json'})
        let u = URL.createObjectURL(b)            
        a.href = u                               // attaches url to the href of the element that we created
        a.download = 'data.json' || 'download'; // defines download behavior
        a.click()                              // virtually clicks on the element to initiate downlaod
        a.remove()                            // deletes element as soon as we're done
      }
    },
    searchDifferentiator: function(search) {
      let de = search.trim().split(',')                      
      if (de[0].startsWith('@')) {        // Differentiates between a username (starts with @) and a generic search term. 
        let u = de.shift().substring(1)  // Username searches are considered advanced searches. Advanced searches can also contain search terms but should start with the username.
        this.advancedSearch(u, de)      // Simple searches can contain one or more search terms.
      } else {
        this.simpleSearch(de)
      }
    },
    simpleSearch: function(search_term) {
      axios.get("http://localhost:5000/search/"+search_term+"", {headers: {"crossorigin": true}})
      .then(response => this.tweets = response.data)
    },
    advancedSearch: function(username, search_term) {
      axios.get("http://localhost:5000/advanced/"+username+"/"+search_term+"", {headers: {"crossorigin": true}})
      .then(response => this.tweets = response.data)
    },
    retrieveStockData: function() {
      axios.get("https://finnhub.io/api/v1/quote?symbol=AAPL&token=c7fcj52ad3if3fodts7g")
      .then(response => {
        this.sap = response.data, console.log(this.sap)
      })
    }
  },
  watch: {
    selected: function() {
        for (let n in this.selected) {
          let c = document.getElementById(this.selected[n].id)
          c.classList.add('selected');
        }
      }
    }
  }
</script>

<style>
body {
  background-color: #082b3f;
}
#app {
  font-family: Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
.grapher-wrapper {
  display: inline-block;
  margin: auto;
  margin-top: 20px;
  place-items: center;
}
.tweet-wrapper {
  margin-left: 10px;
  margin-top: 40px;
}
.inputfield {
  display: grid;
  margin: auto;
  border-radius: .4em;
  max-width: 250px;
}
.selected {
  border: white solid 2px;
}
</style>