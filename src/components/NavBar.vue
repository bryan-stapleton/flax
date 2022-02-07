<template>
  <b-navbar type="dark">
    <b-navbar-brand id='brand' href="https://github.com/gljusty" target="_blank">_Flax</b-navbar-brand>
    <div id='dropdown-wrapper'>
      <div>
        <b-dropdown id="dropdown-form" text="Dropdown with form" ref="dropdown" variant="info" class="m-2" right>
          <b-dropdown-form>
            <b-form-group label="Email" label-for="dropdown-form-email" @submit.stop.prevent>
              <b-form-input
                id="dropdown-form-email"
                size="sm"
                placeholder="email@example.com"
              ></b-form-input>
            </b-form-group>
            <b-form-group label="Password" label-for="dropdown-form-password">
              <b-form-input
                id="dropdown-form-password"
                type="password"
                size="sm"
                placeholder="Password"
              ></b-form-input>
            </b-form-group>

            <b-form-checkbox class="mb-3">Remember me</b-form-checkbox>
            <b-button variant="primary" size="sm" @click="onClick">Sign In</b-button>
          </b-dropdown-form>
          <b-dropdown-divider></b-dropdown-divider>
          <b-dropdown-item-button>New around here? Sign up</b-dropdown-item-button>
          <b-dropdown-item-button>Forgot Password?</b-dropdown-item-button>
        </b-dropdown>
      </div>
    </div>
  </b-navbar>
</template>

<script>
export default {
  name: 'NavBar',
  components: {},
  methods: {
    onClick(el) {
      el.style.backgroundColor = 'coral'
    }
  },
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