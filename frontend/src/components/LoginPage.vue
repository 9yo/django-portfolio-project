<template>
  <v-app>
    <v-card class='ma-auto my-auto"'>
      <v-card-title>
        <v-spacer/>
          <span>Login</span>
        <v-spacer/>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-row>
            <v-col
              cols="12"
            >
              <v-text-field
                v-model="login_storage"
                label="login"
                required
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col
              cols="12"
            >
              <v-text-field
                v-model="password_storage"
                label="password"
                required
              ></v-text-field>
            </v-col>
          </v-row>
        </v-container>
        <v-row class="pr-md-10" v-if="missing_data">
          <v-spacer/>
          <span style="color:red"> Please, fill both fields </span>
        </v-row>
        <v-row class="pr-md-5" v-if="wrong_data">
          <v-spacer/>
          <span style="color:red"> Password or login is not correct </span>
        </v-row>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="blue darken-1"
          text
          @click="dialog = false"
        >
          Exit
        </v-btn>
        <v-btn
          color="blue darken-1"
          text
          @click="handleLogin()"
        >
          Login
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-app>
</template>

<script>
import { login, logout, isLoggedIn } from '../../utils/auth'

export default {
  name: 'LoginDialog',

  data() {
    return {
      dialog: true,
      wrong_data: false,
      missing_data: false,
      login_storage: '',
      password_storage: '',
    }
  },
  methods: {
    handleLogin() {
      if (!this.login_storage | !this.password_storage) {
        this.missing_data = true;
        return;
      } else {
        this.missing_data = false;
      }
      if (!login(this.login_storage, this.password_storage)) {
        this.wrong_data = true;
      }
    }
  }

}
</script>
