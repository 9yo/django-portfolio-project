<template>
  <v-toolbar color="#0D1117" style='z-index: 1; border-bottom: 2px solid #30363D' v-show="isLoggedIn()">
    <v-img
      class="mx-auto"
      max-height="40"
      max-width="40"
      src="http://localhost:8000/static/logo.png"
    ></v-img>
    <v-spacer/>
    <v-btn icon dark v-on:click="handleLogout">
      <v-icon>
        mdi-logout
      </v-icon>
    </v-btn>
  </v-toolbar>
</template>

<script>
import { logout } from '../../utils/auth'
import { isLoggedIn } from 'axios-jwt'
export default {
  name: 'NavBar',

  methods: {
    isLoggedIn () {
      return isLoggedIn()
    },
    handleLogout () {
      logout();
    },
  }
}
</script>
