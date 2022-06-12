<template>
  <v-app>
    <v-container fluid style="height: 100vh;" data-app>
      <v-row class="pt-10">
        <v-col cols="2" v-for="contact in contacts" :key='contact.id'>
          <v-card>
            <v-btn @click='deleteContact(contact.id)' icon style='position:absolute; right: 0px'>
              <v-icon>
                mdi-delete
              </v-icon>
            </v-btn>
            <EditContactDialog  :contact="contact"/>
            <v-card-title > {{ contact.name }} </v-card-title>
            <v-card-text > {{ contact.number }} </v-card-text>
            <v-card-text > {{ contact.comment }} </v-card-text>
          </v-card>
        </v-col>
        <CreateContactDialog/>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import axiosInstance from '../../utils/auth'
import CreateContactDialog from './CreateContactDialog'
import EditContactDialog from './EditContactDialog'


export default {
  name: 'ContactsPage',
  components: {
    CreateContactDialog: CreateContactDialog,
    EditContactDialog: EditContactDialog,
  },

  data() {
    return {
      contacts: [],
    }
  },
  methods: {
    deleteContact(id) {
      axiosInstance.delete(`/contacts/${id}/`)
         .then(response => {
           console.log(response.data);
           document.location.reload();
         })
         .catch(function (error) {
           console.log(error)
         })
       }
  },

  beforeMount() {
     axiosInstance.get('/contacts/')
        .then(response => {
          console.log(response.data.results);
          this.contacts = response.data.results
        })
        .catch(function (error) {
          console.log(error)
        })
    }
}
</script>
