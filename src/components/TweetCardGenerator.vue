<template>

  <transition-group
    appear
    tag="div"
    class="tweet-grid"
    v-bind:css="false"
    v-on:before-enter="beforeEnter"
    v-on:enter="enter"
    v-on:leave="leave"
  >

    <div
      class="tweet-card"
      :id="tweet.id"
      tabindex="0"
      v-for="tweet in this.tweets"
      :key="tweet.id"
      v-on:dblclick="selected"
    >

      <div class="profile-link-wrapper">

        <b-link
          class="profile-link"
          target="_blank"
          tabindex="-1"
          :href="tweet.link"
        >
           @{{ tweet.username }}
        </b-link>

        <a class="score-wrapper">

          <b-badge variant="success" v-if="tweet.scores['compound'] > 0">
             {{tweet.scores['compound']}}
          </b-badge>

          <b-badge variant="danger" v-else-if="tweet.scores['compound'] < 0">
             {{tweet.scores['compound']}}
          </b-badge>

          <b-badge variant="" v-else>{{tweet.scores['compound']}}</b-badge>

        </a>

      </div>

      <div class="text-wrapper">

        <span>{{tweet.tweet}}</span>

      </div>

    </div>

  </transition-group>

</template>

<script>
 import Velocity from 'velocity-animate'; export default { name: 'TweetCard', props:
{ tweets: Array, }, methods: { selected: function(event) { let n = event.currentTarget
this.$emit('tweet-selected', n) }, beforeEnter: function(el) { el.style.opacity =
0 }, enter: function(el, done) { let delay = Math.random() ** 2 * 750; setTimeout(function()
{ Velocity( el, { opacity: 1 }, { complete: done } ) }, delay) }, leave: function
(el, done) { let delay = Math.random() ** 3 * 3000; setTimeout(function () { Velocity(
el, { opacity: 0 }, { complete: done } ) }, delay) } }, computed: {}, data() { return
{} }, }
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
.text-wrapper {
  margin: 20px 5px 2px 5px;
}
.score-wrapper {
  float: right;
}
.profile-link:link {
  text-decoration: none;
  color: #2ca4c9;
}
.profile-link:visited,
::after {
  text-decoration: none;
  color: grey;
}
</style>

