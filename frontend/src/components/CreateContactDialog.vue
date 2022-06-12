<template>
    <v-dialog
      transition="dialog-bottom-transition"
      max-width="300">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="success"
          fab
          style='position:absolute; right:10px; bottom: 100px'
          @click='creation_dialog=true'
          v-bind="attrs"
          v-on="on">
           <v-icon>
             mdi-plus
           </v-icon>
         </v-btn>
       </template>
       <template v-slot:default="dialog">
          <v-card>
            <v-toolbar
              color="primary"
              dark
            >Create new contact</v-toolbar>
            <v-row>
              <v-col
                cols="8"
                class="pl-10"
              >
                <v-text-field
                  v-model="name_storage"
                  label="Name"
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
                  label="Number"
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
                  label="Comment"
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
                @click="dialog.value = false; save()"
              >Save</v-btn>
            </v-card-actions>
          </v-card>
        </template>
     </v-dialog>
</template>

<script>
import axiosInstance from '../../utils/auth'

export default {
  name: 'CreateContactDialog',
  data() {
    return {
      name_storage: '',
      number_storage: '',
      comment_storage: '',

    }
  },
  methods: {
    save() {
      axiosInstance.post('/contacts/', {
        'name': this.name_storage,
        'number': this.number_storage,
        'comment': this.comment_storage,
      })
         .then(response => {
           console.log(response.data);
           document.location.reload();
         })
         .catch(function (error) {
           console.log(error)
         })
    }
  }
}
</script>
