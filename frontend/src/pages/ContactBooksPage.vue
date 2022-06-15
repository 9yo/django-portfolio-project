<template>
  <v-app>
    <v-container fluid style="height: 100vh;" data-app>
      <v-row style="height:100%">
        <SearchBlock/>
        <v-col cols='10' style='background-color: #010409'>
            <v-col cols="2" v-for="contact_book in contact_books" :key='contact_book.id'>
              <v-card color='#0D1117' style='border: 2px solid #30363D'>
                <v-btn @click='deleteContact(contact_book.id)' icon style='position:absolute; right: 0px'>
                  <v-icon>
                    mdi-delete
                  </v-icon>
                </v-btn>
                <EditContactBookDialog  :contact_book="contact_book"/>
                <v-card-title > {{ contact_book.name }} </v-card-title>
                <v-card-text > {{ contact_book.desc }} </v-card-text>
              </v-card>
            </v-col>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import axiosAuth from '../../utils/auth'
import EditContactBookDialog from '../components/EditContactBookDialog'
import SearchBlock from '../components/SearchBlock'


export default {
  name: 'ContactsPage',
  components: {
    EditContactBookDialog: EditContactBookDialog,
    SearchBlock: SearchBlock,
  },

  data() {
    return {
      contact_books: [],
    }
  },
  methods: {
    deleteContact(id) {
      axiosAuth.delete(`/contact_books/${id}/`)
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
