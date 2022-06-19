<template>
  <v-app>
    <v-row style='max-height:100px'>
    </v-row>
    <v-row style="max-height:100px">
        <v-img
          class="mx-auto"
          max-height="75"
          max-width="75"
          src="http://localhost:8000/static/logo.png"
        ></v-img>

    </v-row>
    <v-row style="max-height:50px" class='mt-0'>
      <span class="mx-auto"> Contact Book </span>
    </v-row>
    <v-row style="max-height:300px" justify="center">
      <v-col style='max-width:350px'>
        <v-card outlined
                class='mb-4'
                style='min-height:40px; background-color: rgba(248,81,73,0.15); border-color: rgba(248,81,73,0.4);'
                v-show="wrong_data">
          <v-card-title class="justify-center"
            style='font-size:14px'>
            Incorrect username or password.
            <v-spacer/>
            <v-btn icon @click='wrong_data=false'>
              <v-icon style='color:rgba(248,81,73,0.4)'>
                mdi-close
              </v-icon>
            </v-btn>
          </v-card-title>
        </v-card>
        <v-card outlined>
            <v-container>
              <v-row>
                <v-col
                  cols="12"
                >
                  <label>Email</label>
                  <v-text-field
                  hide-details
                    v-model="email_storage"
                    outlined
                    dense
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col
                  cols="12"
                >
                  <label>Username</label>
                  <v-text-field
                  hide-details
                    v-model="username_storage"
                    outlined
                    dense
                    required
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col
                  cols="12"
                >
                  <label>Password</label>
                  <v-text-field
                    hide-details
                    v-model="password_storage"
                    :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                    :type="show ? 'text' : 'password'"
                    outlined
                    dense
                    required
                    @click:append="show = !show"
                  ></v-text-field>
                </v-col>
              </v-row>
              <v-row>
                <v-col
                  cols="12"
                >
                  <label>Repeat password</label>
                  <v-text-field
                    hide-details
                    v-model="password_repeat_storage"
                    :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                    :type="show2 ? 'text' : 'password'"
                    outlined
                    dense
                    required
                    @click:append="show2 = !show2"
                  ></v-text-field>
                </v-col>
              </v-row>
            </v-container>
          <v-card-actions>
            <v-btn
              block
              class="text-capitalize"
              color="success"
              @click="register()"
            >
              Register
            </v-btn>
          </v-card-actions>
        </v-card>
        <v-card outlined class='mt-4' style='min-height:40px'>
          <v-card-title class="justify-center"
            style='font-size:14px'>
            Already have an accout?
            <a href="/login" class="pl-1" style='color:#58a6ff'> Login. </a>
          </v-card-title>
        </v-card>
      </v-col>
    </v-row>
  </v-app>
</template>

<script>
import { axiosDefault, login} from '../../utils/auth'

export default {
  name: 'LoginDialog',

  data() {
    return {
      show: false,
      show2: false,
      wrong_data: false,
      username_storage: '',
      email_storage: '',
      password_storage: '',
      password_repeat_storage: '',
    }
  },
  methods: {
    register() {
      if (!this.username_storage | !this.password_storage | !this.email_storage |
        !this.password_repeat_storage |
        this.password_storage != this.password_repeat_storage) {
          this.wrong_data = true;
          return
      }

      this.wrong_data = false;
      axiosDefault.post('/auth/register/', {
        username: this.username_storage,
        email: this.email_storage,
        password: this.password_storage
      }).then(response => {
        login(this.username_storage, this.password_storage)
      }).catch(error => {
        console.log(error)
      })
    }
  }

}
</script>
