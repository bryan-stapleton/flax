<template>
  <b-navbar type="dark">
    <b-navbar-brand id='brand' href="https://github.com/gljusty" target="_blank">_Flax</b-navbar-brand>
    <b-navbar-nav>
      <b-nav-item-dropdown :text="this.u" right>
        <b-dropdown-item href="#">Login</b-dropdown-item>
        <b-dropdown-item href="#">Account</b-dropdown-item>
        <b-dropdown-item href="#">Settings</b-dropdown-item>
      </b-nav-item-dropdown>
    </b-navbar-nav>
  </b-navbar>
</template>

<script>
export default {
  name: 'NavBar',
  components: {},
  props: {
    user: String,
    password: String,
    query: String
  },
  data () {
    return {
      u: 'Username'
    }
  }
}
</script>

<style scoped>
#brand {
  margin-left: 20px;
}

</style>