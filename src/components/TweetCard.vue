<template>
  <transition-group tag='div' name='list' class='tweet-grid'>
    <div class="tweet-card" :id="tweet.id" tabindex="0" v-for="tweet in this.tweets" :key="tweet.id" v-on:dblclick="selected">
      <div class="profile-link-wrapper">
        <b-link class="profile-link" target="_blank" tabindex="-1" :href="tweet.link">
          @{{ tweet.username }}
        </b-link>
        <a class='score-wrapper'>
          <b-badge variant="">{{ tweet.scores['compound'] }}</b-badge>
        </a>
        <span><br/><br/></span>
      </div>
      <div class='text-wrapper'>
        <span> {{ tweet.tweet }} </span>
      </div>
    </div>
  </transition-group>
</template>

<script>
export default {
    name: 'TweetCard',
    props: {
      tweets: Array
    },
    methods: {
      selected: function(event) {
        let n = event.currentTarget 
        this.$emit('tweet-selected', n)
      }
    },
    data() {
      return {}
    },
}
</script>

<style scoped>
.tweet-card {
  overflow: scroll;
  scrollbar-width: none;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  color: black;
  border-radius: 1rem;
  margin: 0.2rem;
  padding: 1rem;
  text-align: left;
  box-shadow: 0.15rem 0.15rem 0.125rem rgba(0, 0, 0, 0.35);
  max-width: 300px;
  max-height: 160px;
  background-color: #0c0c0c;
  color: lightgray;
  animation: created 2s ease-in;
}
.tweet-grid {
  margin: auto;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  grid-auto-flow: row dense;
}
.profile-link-wrapper {
  float: right;
}
.score-wrapper {
  float: right;
}
.profile-link:link {
  text-decoration: none;
  color: #2ca4c9;
}
.profile-link:visited, ::after {
  text-decoration: none;
  color: grey;
}

@keyframes created {
  
}
</style>