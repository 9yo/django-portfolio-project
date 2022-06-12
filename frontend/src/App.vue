<template>
    <v-main>
      <NavBar/>
      <router-view/>
    </v-main>
</template>

<script>
import NavBar from './components/NavBar';

export default {
  name: 'App',

  components: {
    NavBar,
  },

  data: () => ({
    //
  }),
};
</script>
