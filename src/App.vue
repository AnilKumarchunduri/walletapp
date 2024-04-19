<template>
  <v-app color="rgba(5, 5, 5, 0.68)">
    <v-snackbar :value="GetterSnackBarData.snackbar" :color="GetterSnackBarData.snackbarcolor" right rounded="pill" outlined top>
      {{GetterSnackBarData.snackbartext}}
      <!-- <template v-slot:action="{ attrs }">
          <v-icon :color="GetterSnackBarData.snackbarcolor" v-bind="attrs" @click="GetterSnackBarData.snackbar = false">mdi-close</v-icon>
      </template> -->
  </v-snackbar>
    <v-main class="grey lighten-3">
      <v-container style="max-width:1500px">
        <v-sheet min-height="100vh" rounded="lg">
          <LandingPage/>
        </v-sheet>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import LandingPage from './components/LandingPage.vue';
import {WalletMixin} from '@/mixins/walletmixins'
export default {
  name: 'App',
  mixins : [WalletMixin],
  components: {
    LandingPage,
  },

  data: () => ({
    //
  }),
};
</script>
