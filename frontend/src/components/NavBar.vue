<template>
  <v-app-bar style='z-index: 1' v-show="isLoggedIn()">
    <a> Contact book </a>
    <v-spacer/>
    <v-btn v-on:click="handleLogout">
      Log Out
    </v-btn>
  </v-app-bar>
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
