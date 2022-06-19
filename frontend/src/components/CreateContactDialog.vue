<template>
    <v-dialog
      transition="dialog-bottom-transition"
      max-width="300">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          small
          color="#238636"
          v-bind="attrs"
          v-on="on">
           <v-icon small>
             mdi-account-plus
           </v-icon>
           <span class="pl-1 font-weight-light text-capitalize"> New </span>
         </v-btn>
       </template>
       <template v-slot:default="dialog">
          <v-card style='overflow: hidden'>
            <v-toolbar
              dark>
              Create new contact
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
              <v-row justify="center" v-for="(field, index) in fields" :key='field'>
                <v-col
                  cols="11"
                >
                  <v-text-field
                    v-model='fields_data[index]'
                    :label='field'
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
                @click="dialog.value = false; save()"
              >Save</v-btn>
            </v-card-actions>
          </v-card>
        </template>
     </v-dialog>
</template>

<script>
import axiosAuth from '../../utils/auth'

export default {
  name: 'CreateContactDialog',
  data() {
    return {
      fields_data: [],
      fields: ['Name', 'Number', 'Comment']

    }
  },
  methods: {
    save() {
      axiosAuth.post('/api/contacts/', {
        'name': this.fields_data[0],
        'number': this.fields_data[1],
        'comment': this.fields_data[2],
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
