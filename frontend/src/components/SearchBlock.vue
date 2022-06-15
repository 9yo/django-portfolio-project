<template>
  <v-col class='pa-8' cols='2' style='background-color: #0D1117; border-right: 2px solid #30363D'>
    <div class='pb-10'>
      <v-row no-gutters class="pb-2">
        Recent contacts
        <v-spacer/>
        <CreateContactDialog/>
      </v-row>
      <v-row no-gutters class='pb-10'>
        <v-text-field
          class='font-weight-light;'
          outlined
          dense
          hide-details
          label="Find a contact...">
        </v-text-field>
      </v-row>
      <v-row no-gutters v-for='contact in contacts' :key='contact.id'>
        <EditContactDialog mode='hyperlink' :contact="contact"/>
      </v-row>
    </div>
    <div>
      <v-row no-gutters class="pt-10 pb-2" style='border-top: 2px solid #30363D'>
        Recent books
        <v-spacer/>
        <CreateContactBookDialog/>
      </v-row>
      <v-row no-gutters class='pb-10'>
        <v-text-field
          class='font-weight-light;'
          outlined
          dense
          hide-details
          label="Find a book...">
        </v-text-field>
      </v-row>
    </div>
  </v-col>
</template>

<script>
import CreateContactBookDialog from '../components/CreateContactBookDialog'
import CreateContactDialog from '../components/CreateContactDialog'
import EditContactDialog from '../components/EditContactDialog'
import axiosAuth from '../../utils/auth'


export default {
  name: 'SearchBlock',
  components: {
    CreateContactDialog: CreateContactDialog,
    CreateContactBookDialog: CreateContactBookDialog,
    EditContactDialog: EditContactDialog,
  },
  data() {
    return {
      contacts: [],
      contact_books: []
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

   axiosAuth.get('/contact_books/')
      .then(response => {
        console.log(response.data.results);
        this.contact_books = response.data.results
      })
      .catch(function (error) {
        console.log(error)
      })
  }
}

</script>
