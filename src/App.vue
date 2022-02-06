<template>
  <div id="app">
    <div class="app-wrapper">
      <div class="navbar-wrapper">
        <NavBar />
      </div>
      <portal-target name="destination"></portal-target>
      <div class='ui-wrapper'>
        <b-form-input class="inputfield" v-model.lazy="search_term" placeholder="ex: @BarackObama"></b-form-input>
        <b-dropdown
        split
        split-variant="outline-primary"
        variant="primary"
        text="Search"
        @click="searchDifferentiator(search_term)"
        >
        </b-dropdown>
      </div>
      <div class="tweet-wrapper">
        <TweetCard :tweets="this.tweets" v-on:tweet-selected="updateSelected" />
      </div>
      <!-- TODO: finish graphing section and related features. Place inside conditionally rendered modal; implement correlation & wordcloud -->
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
  data() {                       // initializes important variables
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
        a.download = 'data' || 'download';      // defines download behavior
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
      this.loading = true
      axios.get("http://localhost:5000/search/"+search_term+"")
      .then(response => this.tweets = response.data)
      .catch(error => (console.log(error)))
      .finally(() => { this.loading = false })
    },
    advancedSearch: function(username, search_term) {
      this.loading = true
      axios.get("http://localhost:5000/advanced/"+username+"/"+search_term+"")
      .then(response => this.tweets = response.data)
      .catch(error => (console.log(error)))
      .finally(() => { this.loading = false })
    },
    retrieveStockData: function() {
      axios.get("https://finnhub.io/api/v1/quote?symbol=AAPL&token=c7fcj52ad3if3fodts7g")
      .then(response => {console.log(response.data)
      })
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
      let l = document.getElementById('logo')
      if (this.loading == true) {
        l.classList.add('logo-anim')
      }
      else {
        l.classList.remove('logo-anim')
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
  display: grid;
  margin: 10px;
  max-width: 250px;
}

.logo-anim {
  animation: loading 5s infinite;
}

.selected {
  border: white solid 2px;
}

.logo-wrapper {
  display: flex;
  place-content: center;
}

.tweet-wrapper {
  margin-left: 10px;
  margin-top: 40px;
}

.ui-wrapper {
  display: flex;
  place-content: center;
}

@keyframes loading {
  50% { transform: rotate(180deg); }
}
</style>