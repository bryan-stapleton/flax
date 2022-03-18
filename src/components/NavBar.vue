<template>
  <b-navbar type="dark" class="m-2 mynav">
    <b-navbar-brand id='brand' href="https://github.com/gljusty/flax" target="_blank">_Flax</b-navbar-brand>
    <div id='dropdown-wrapper'>
      <b-dropdown id="dropdown-form" ref="dropdown" variant="info" class="m-2" right>
        <b-dropdown-divider></b-dropdown-divider>
        <b-dropdown-item-button @click="emitDownload()">Download All</b-dropdown-item-button>
        <b-dropdown-item-button @click="emitSelected()">Download Selected</b-dropdown-item-button>
        <b-dropdown-divider></b-dropdown-divider>
      </b-dropdown>
      </div>
  </b-navbar>
</template>

<script>
export default {
  name: 'NavBar',
  components: {},
  methods: {
    onClick: function() {
      console.log('clicked')
    },
    emitDownload: function(event) {
      console.log('emitting download event')
      this.$emit('download-event', event)
    },
    
    emitSelected: function(event) {
      console.log('emitting selected event')
      this.$emit('selected-event', event)
    }
  },
  props: {
    user: String,
    tweets: Array
  },
  data () {
    return {}
  }
}
</script>

<style scoped>
#brand {
  margin-left: 20px;
}
#dropdown-wrapper {
  margin-left: auto;
  margin-right: 40px;
  text-align: right;
  justify-content: end;
}
#dropdown-form > {
  height: 500px;
  width: 200px;
}
.mynav {
  background-color: #082b3f;
}
</style>