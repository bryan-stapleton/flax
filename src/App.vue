<template>
  <div id="app">
    <div class="app-wrapper">
      <div class="navbar-wrapper">
        <NavBar :tweets="this.tweets" v-on:download-event="downloadtoFile(tweets)" v-on:selected-event="downloadSelected()" />
      </div>
      <div class='logo-wrapper'>
        <img id='logo' alt="3 circles logo" src="./assets/logo.svg">
      </div>
      <div class='ui-wrapper'>
        <b-form-input class="m-0 inputfield" v-model.lazy="search_term" placeholder="ex: @BarackObama"></b-form-input>
        <b-button-toolbar size="sm">
          <b-button class="ml-1 sm-0 search-button" variant="info" @click="searchDifferentiator(search_term)"> Search </b-button>
          <b-button class="ml-1 sm-0 button" variant="primary" @click="queryDatabase()"> Query DB </b-button>
        </b-button-toolbar>
      </div>
      <div class="tweet-wrapper">
        <TweetCard :tweets="this.tweets" v-on:tweet-selected="updateSelected" />
      </div>
      <!-- TODO: redo graphing section and related features. Place inside conditionally rendered modal; implement correlation & wordcloud -->
    </div>

    <portal to="destination">
        <div class='logo-wrapper'>
          <img id='logo' alt="3 circles logo" src="./assets/logo.svg">
        </div>
    </portal>
  </div>
</template>

<script>
import NavBar from './components/NavBar'
import TweetCard from './components/TweetCard'
import axios from 'axios';
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap-vue/dist/bootstrap-vue.css";

export default {
  name: 'App',
  components: {
    NavBar,
    TweetCard
  },
  data() {
    return {
      search_term: '',
      selected: [],
      tweets: [],
      loading: false
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
        if (!(arr.includes(c.id))) { arr.push(c.id) }
      }
      let filtered_tweets = this.tweets.filter(tweet => arr.includes(JSON.stringify(tweet.id)))
      this.downloadtoFile(filtered_tweets)
    },
    downloadtoFile: function(content) {
      if (content) {
        let a = document.createElement('a')
        let b = new Blob([JSON.stringify(content, null, 4)], {type: 'application/json'})
        let u = URL.createObjectURL(b)            
        a.href = u                                  // attaches url to the href of the element that we created
        a.download = 'data' || 'download';         // defines download behavior
        a.click()                                 // virtually clicks on the element to initiate downlaod
        a.remove()                               // deletes element as soon as we're done
      }
    },
    searchDifferentiator: function(search) {
      this.selected = []                       // sets selected to empty array to avoid trying to download no longer existant tweets
      this.tweets = []                        // sets tweets to empty array to clear old results
      let de = search.trim().split(',')                      
      if (de[0].startsWith('@')) {          // Differentiates between a username (starts with @) and a generic search term. 
        let u = de.shift().substring(1)    // Username searches are considered advanced searches. Advanced searches can also contain search terms but should start with the username.
        this.advancedSearch(u, de)        // Simple searches can contain one or more search terms.
      } else {
        this.simpleSearch(de)
      }
    },
    simpleSearch: function(search_term) {                              
      this.loading = true                                             // sets loading to true so that watch function will apply loading animation to logo
      axios.get("http://localhost:5000/search/"+search_term+"")      // performs get request with user input search term
      .then(response => this.tweets = response.data)                // response converted to this.tweets which is passed to TweetCard to generate the cards that display each tweet
      .catch(error => (console.log(error)))                        // catches errors in console
      .finally(() => { this.loading = false })                    // set loading to false to end loading animation
    },
    advancedSearch: function(username, search_term) {           // same as above but also implements username
      this.loading = true
      axios.get("http://localhost:5000/advanced/"+username+"/"+search_term+"")
      .then(response => this.tweets = response.data)
      .catch(error => (console.log(error)))
      .finally(() => { this.loading = false })
    },
    queryDatabase: function() {
      axios.get("http://localhost:5000/db/query/")
      .then(response => {console.log(response.data)})
      .catch(error => {console.log(error)})
    }
  },
  watch: {
    selected: function() {
        for (let n in this.selected) {
          let c = document.getElementById(this.selected[n].id)
          c.classList.add('selected');
        }
      },
    loading: function() {
      let logo = document.getElementById('logo')
      if (this.loading == true) {
        logo.classList.add('logo-anim')
      }
      else {
          logo.animate([{transform: 'rotate(360deg)'}],{
            duration: 350,
            iterations: 1
          })
          logo.classList.remove('logo-anim')
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
}

#logo {
  margin: auto;
  justify-self: center;
}

.inputfield {
  margin-top: 10px;
  margin-bottom: 10px;
  margin-right: 0;
  max-width: 300px;
}

.logo-anim {
  animation: loading 5s infinite;
}

.selected {
  border: white solid 1px;
  box-shadow: whitesmoke 1px 1px;
}

.logo-wrapper {
  display: flex;
  place-content: center;
  position: sticky;
  top: 0px;
  z-index: -1;
}

.navbar-wrapper {
  position: sticky;
  top: 0px;
}

.tweet-wrapper {
  margin-left: 10px;
  margin-top: 40px;
}

.ui-wrapper {
  display: flex;
  justify-content: center;
}

@keyframes loading {
  50% { transform: rotate(360deg); }
}
</style>