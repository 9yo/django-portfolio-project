<template>
    <v-dialog
      transition="dialog-bottom-transition"
      max-width="300">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          icon
          v-bind="attrs"
          v-on="on">
           <v-icon>
             mdi-pencil
           </v-icon>
         </v-btn>
       </template>
       <template v-slot:default="dialog">
         <v-card style='overflow: hidden'>
           <v-toolbar
             dark>
             Edit contact book
             <v-spacer/>
             <v-btn
               icon
               @click='dialog.value = false;'>
               <v-icon>
                 mdi-close
               </v-icon>
             </v-btn>
           </v-toolbar>
           <div class='py-5'>
             <v-row justify="center" v-for="(field, index) in fields_data" :key='index'>
               <v-col
                 cols="11"
               >
                <label>{{ fields_data[index][0] }}</label>
                 <v-text-field
                   v-model='fields_data[index][1]'
                   hide-details
                   outlined
                   dense
                   required
                 ></v-text-field>
               </v-col>
             </v-row>
           </div>
           <v-card-actions class="justify-end">
             <v-btn
               block
               class="text-capitalize"
               color="success"
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
  name: 'EditContactBookDialog',
  props: ['contact_book'],
  data() {
    return {
      fields_data: [
        ['Name', this.contact_book.name],
        ['Description', this.contact_book.desc],
      ],
    }
  },


  methods: {
    edit() {
      axiosAuth.patch(`/api/contact_books/${this.contact_book.id}/`, {
        'name': this.fields_data[0][1],
        'desc': this.fields_data[1][1],
        'contacts': []
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
