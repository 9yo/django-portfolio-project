<template>
  <v-row no-gutters
    style='overflow-y: scroll; max-height: 100vh; overflow: auto;'>
      <v-col class='pa-1' cols='12' v-for="contact in contacts" :key='contact.id'>
        <v-row
          no-gutters
          class='rounded'
          align='center'
          style='min-height: 50px; border: 2px solid #30363D; background-color: #0D1117'>
          <v-col class='pl-10'>
            {{ contact.name }}
          </v-col>
          <v-col>
            {{ contact.number }}
          </v-col>
          <v-col>
            {{ contact.comment }}
          </v-col>
          <v-col cols='1' class='rounded-pill' style='background-color: #21262D'>
            <AddContactToBookMenu :contact='contact' :contact_books='contact_books'/>
          </v-col>
          <v-spacer/>
          <EditContactDialog mode='button' :contact="contact"/>
          <v-btn @click='deleteContact(contact.id)' icon>
            <v-icon>
              mdi-delete
            </v-icon>
          </v-btn>
        </v-row>
      </v-col>
  </v-row>
</template>

<script>
import axiosAuth from '../../utils/auth'
import EditContactDialog from '../components/EditContactDialog'
import AddContactToBookMenu from '../components/AddContactToBookMenu'



export default {
  name: 'ContactsPage',
  components: {
    EditContactDialog: EditContactDialog,
    AddContactToBookMenu: AddContactToBookMenu,
  },
  props: ['contacts', 'contact_books'],


  methods: {
    deleteContact(id) {
      axiosAuth.delete(`/api/contacts/${id}/`)
         .then(response => {
           console.log(response.data);
           document.location.reload();
         })
         .catch(function (error) {
           console.log(error)
         })
       }
  },

  // beforeMount() {
  //    axiosAuth.get('/contacts/')
  //       .then(response => {
  //         console.log(response.data.results);
  //         this.contacts = response.data.results
  //       })
  //       .catch(function (error) {
  //         console.log(error)
  //       })
  //   }
}
</script>
