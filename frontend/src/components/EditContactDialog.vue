<template>
    <v-dialog
      transition="dialog-bottom-transition"
      max-width="300">
      <template v-slot:activator="{ on, attrs }">
        <div
          class='text-caption'
          v-if="mode == 'hyperlink'"
          v-bind="attrs"
          v-on="on">
          {{ contact.name }}
        </div>
        <v-btn
          v-else
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
             Edit contact
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
                 <v-text-field
                   v-model='fields_data[index]'
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
  name: 'EditContactDialog',
  props: ['contact', 'mode'],
  data() {
    return {
      fields_data: [
        this.contact.name,
        this.contact.number,
        this.contact.comment,
      ],
    }
  },


  methods: {
    edit() {
      axiosAuth.patch(`/api/contacts/${this.contact.id}/`, {
        'name': this.fields_data[0],
        'number': this.fields_data[1],
        'comment': this.fields_data[2]
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
