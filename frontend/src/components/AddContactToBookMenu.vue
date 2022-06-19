<template>
  <v-row no-gutters align='center'>
    <v-col class='text-caption pl-4'>
      Book
    </v-col>
    <v-col style='border-left: 1px solid #30363D'>
      <div class="text-center">
        <v-menu
          v-model="menu"
          offset-y
          :close-on-content-click='false'>
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              icon
              small
              v-bind="attrs"
              v-on="on"
            >
              <v-icon>
                mdi-menu-down
              </v-icon>
            </v-btn>
          </template>
          <v-list class='pa-0'  style='background-color: #0D1117; border: 1px solid #30363D; min-width:300px'>
            <v-list-item dense style='border: 0.5px solid #30363D;'>
              <v-list-item-title>
                <v-row no-gutters align='center'>
                  <div class='subtitle-2'>
                    Books
                  </div>
                  <v-spacer/>
                  <v-btn icon @click="menu = false">
                    <v-icon small>
                      mdi-close
                    </v-icon>
                  </v-btn>
              </v-row>
              </v-list-item-title>
            </v-list-item>
            <v-list-item
              dense
              style='border: 0.5px solid #30363D;'
              v-for="(book, index) in contact_books"
              :key="index"
            >
              <v-list-item-title class='text-caption'>
                <v-row no-gutters align='center'>
                  <v-checkbox
                    dense
                    class='px-2'
                    :id='book.name'
                    v-model='selection[index]'/>
                  {{ book.name }}
                </v-row>
              </v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </div>
    </v-col>
  </v-row>
</template>
<script>
import axiosAuth from '../../utils/auth'

export default {
  name: 'AddContactToBookMenu',
  props: ['contact', 'contact_books'],
  data() {
    return {
      menu: false,
      selection_start: [],
      selection: [],
    };
  },
  beforeMount() {
    this.contact_books.forEach((item, i) => {
      if (item.contacts.includes(this.contact.id)) {
        this.selection_start[i] = true
      } else {
        this.selection_start[i] = false
      }
    });
    this.selection = [...this.selection_start];
  },

  watch: {
    menu: function() {
      if (this.menu) return;
      this.selection_start.forEach((item, i) => {
        if (item != this.selection[i]) {
          var cb = this.contact_books[i];
          var c_id = this.contact.id;
          if (item == true && this.selection[i] == false) {
            cb.contacts.splice(cb.contacts.indexOf(this.contact.id), 1);
          } else {
            cb.contacts.push(this.contact.id);
          }
          axiosAuth.patch(`/api/contact_books/${cb.id}/`, {
            'name': cb.name,
            'desc': cb.desc,
            'contacts': cb.contacts,
            })
             .then(response => {
               console.log(response.data);
             })
             .catch(function (error) {
               console.log(error)
            })
        }
      });
      this.selection_start = [...this.selection];
    }
  }
}
</script>
