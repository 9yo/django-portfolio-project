<template>
  <v-app>
    <v-container fluid style="height: 100vh;" data-app>
      <v-row style="height:100%">
        <SearchBlock/>
        <v-col style='background-color: #010409;'>
          <v-row no-gutters>
              <v-col class='pa-4' cols='2' v-for="contact in contacts" :key='contact.id'>
                <v-card color='#0D1117' style='border: 2px solid #30363D'>
                  <v-btn @click='deleteContact(contact.id)' icon style='position:absolute; right: 0px'>
                    <v-icon>
                      mdi-delete
                    </v-icon>
                  </v-btn>
                  <EditContactDialog mode='button' :contact="contact"/>
                  <v-card-title > {{ contact.name }} </v-card-title>
                  <v-card-text > {{ contact.number }} </v-card-text>
                  <v-card-text > {{ contact.comment }} </v-card-text>
                </v-card>
              </v-col>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import axiosAuth from '../../utils/auth'
import EditContactDialog from '../components/EditContactDialog'
import SearchBlock from '../components/SearchBlock'


export default {
  name: 'ContactsPage',
  components: {
    EditContactDialog: EditContactDialog,
    SearchBlock: SearchBlock,
  },

  data() {
    return {
      contacts: [],
    }
  },
  methods: {
    deleteContact(id) {
      axiosAuth.delete(`/contacts/${id}/`)
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
     axiosAuth.get('/contacts/')
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
