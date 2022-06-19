<template>
  <v-app>
    <v-container fluid style="height: 100vh;" data-app>
      <v-row style="height:100%">
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
                v-model='contacts_filter'
                label="Find a contact...">
              </v-text-field>
            </v-row>
            <v-row no-gutters v-for='(contact, index) in filteredContacts()' :key='contact.id'>
              <EditContactDialog mode='hyperlink' :contact="contact" v-if='index < 11'/>
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
                v-model='contacts_books_filter'
                label="Find a book...">
              </v-text-field>
            </v-row>
            <v-row no-gutters v-for='(book, index) in filteredContactBooks()' :key='book.id'>
              <a v-if='index < 11' style='color: inherit;' class='text-caption' @click='showContactsFromBook(book)'>
                {{ book.name }}
              </a>
            </v-row>
          </div>
        </v-col>
        <v-col style='background-color: #010409;'>
          <v-row v-if='selected_book'
            no-gutters
            class='rounded'
            align='center'
            justify='center'
            style='min-height: 50px; border: 2px solid #30363D; background-color: #0D1117'>
            Showing contacs from book ' {{ selected_book.name.toUpperCase() }} '
            <v-btn
              icon
              small
              style='position: absolute; right:20px'
              @click='showContactsFromBook(null)'>
              <v-icon> mdi-close </v-icon>
            </v-btn>

          </v-row>
          <ContactsList
            :key='contacts_list_key'
            :contacts='contacts'
            :contact_books='contact_books'/>
        </v-col>
    </v-row>
    </v-container>
  </v-app>
</template>
<script>
import CreateContactBookDialog from '../components/CreateContactBookDialog'
import CreateContactDialog from '../components/CreateContactDialog'
import ContactsList from '../components/ContactsList'
import EditContactDialog from '../components/EditContactDialog'
import axiosAuth from '../../utils/auth'


export default {
  name: 'SearchBlock',
  components: {
    CreateContactDialog: CreateContactDialog,
    CreateContactBookDialog: CreateContactBookDialog,
    EditContactDialog: EditContactDialog,
    ContactsList: ContactsList,
  },
  data() {
    return {
      contacts: [],
      contacts_filter: '',
      contact_books: [],
      contacts_books_filter: '',
      contacts_list_key: 0,
      selected_book: null,
    }
  },
  methods: {
    filteredContactBooks() {
      return this.contact_books.filter((contact_book) =>
        contact_book.name.toLowerCase().includes(this.contacts_books_filter.toLowerCase())
      );
    },

    filteredContacts() {
      return this.contacts.filter((contact) =>
        contact.name.toLowerCase().includes(this.contacts_filter.toLowerCase())
      );
    },
    showContactsFromBook(book) {
      this.selected_book = book;
      function idIn(contactsList) {
        return function(element) {
          return contactsList.indexOf(element.id) !== -1;
        }
      }
      this.getContacts()
        .then(promise => {
          if (this.selected_book) {
            this.contacts = this.contacts.filter(idIn(book.contacts));
          }
          this.contacts_list_key +=1;
        })
    },
    getContacts() {
      let res = axiosAuth.get('/api/contacts/')
         .then(response => {
           this.contacts = response.data.results
         })
         .catch(function (error) {
           console.log(error)
         })
      return res;
    },
    getContactBooks() {
      axiosAuth.get('/api/contact_books/')
         .then(response => {
           this.contact_books = response.data.results
         })
         .catch(function (error) {
           console.log(error)
         })
    }
  },
  beforeMount() {
    this.getContacts();
    this.getContactBooks();
  }
}

</script>
