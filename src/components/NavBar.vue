<template>
  <b-navbar type="dark">
    <b-navbar-brand id='brand' href="https://github.com/gljusty" target="_blank">_Flax</b-navbar-brand>
    <div id='dropdown-wrapper'>
      <b-nav-item-dropdown :text="this.user" right>
        <b-dropdown-item href="#">Account</b-dropdown-item>
        <b-dropdown-item href="#">Settings</b-dropdown-item>
      </b-nav-item-dropdown>
    </div>
  </b-navbar>
</template>

<script>
export default {
  name: 'NavBar',
  components: {},
  props: {
    user: String,
    query: String
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
</style>