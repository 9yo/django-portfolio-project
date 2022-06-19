<template>
  <v-toolbar color="#0D1117" style='z-index: 1; border-bottom: 2px solid #30363D' v-show="isLoggedIn()">
    <v-col cols='2' style='padding-right:0px'>
      <v-img
        class="mx-auto"
        max-height="40"
        max-width="40"
        src="http://localhost:8000/static/logo.png"
      ></v-img>
    </v-col>
    <v-col style='padding-left:0px; max-width:100px'>
       <a class='font-weight-medium' style='color:white; text-decoration: none;' href="/contacts">
         Contacts
       </a>
    </v-col>
    <v-spacer/>
    <v-col style='max-width:50px'>
      <v-btn icon dark v-on:click="handleLogout">
        <v-icon>
          mdi-logout
        </v-icon>
      </v-btn>
    </v-col>
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
