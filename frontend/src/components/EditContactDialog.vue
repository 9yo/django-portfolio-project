<template>
    <v-dialog
      transition="dialog-bottom-transition"
      max-width="300">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          icon
          style='position:absolute; right:0px; bottom: 0px'
          @click='creation_dialog=true'
          v-bind="attrs"
          v-on="on">
           <v-icon>
             mdi-pencil
           </v-icon>
         </v-btn>
       </template>
       <template v-slot:default="dialog">
          <v-card>
            <v-toolbar
              color="primary"
              dark
            >Edit contact</v-toolbar>
            <v-row>
              <v-col
                cols="8"
                class="pl-10"
              >
                <v-text-field
                  v-model="name_storage"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col
                cols="8"
                class="pl-10"
              >
                <v-text-field
                  v-model="number_storage"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <v-col
                cols="8"
                class="pl-10"
              >
                <v-text-field
                  v-model="comment_storage"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
            <v-card-actions class="justify-end">
              <v-btn
                text
                @click="dialog.value = false"
              >Exit</v-btn>
              <v-btn
                text
                @click="dialog.value = false; edit()"
              >Edit</v-btn>
            </v-card-actions>
          </v-card>
        </template>
     </v-dialog>
</template>

<script>
import axiosAuth from '../../utils/auth'

export default {
  name: 'EditContactDialog',
  props: ['contact'],
  data() {
    return {
      name_storage: this.contact.name,
      number_storage: this.contact.number,
      comment_storage: this.contact.comment,
    }
  },

  methods: {
    edit() {
      axiosAuth.patch(`/contacts/${this.contact.id}/`, {
        'name': this.name_storage,
        'number': this.number_storage,
        'comment': this.comment_storage
      })
         .then(response => {
           console.log(response.data);
           document.location.reload();
         })
         .catch(function (error) {
           console.log(error)
         })
       }
  },
}
</script>
