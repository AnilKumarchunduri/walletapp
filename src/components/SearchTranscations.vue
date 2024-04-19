<template>
    <!-- eslint-disable -->
    <div>
        <div>
            <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition" persistent>
                <template v-slot:activator="{ on, attrs }">
                    <v-icon color="primary" dark v-bind="attrs" v-on="on" dense title="Search">mdi-magnify</v-icon>
                </template>
                <v-card>
                    <v-toolbar dark color="primary">
                        <v-btn icon dark @click="dialog = false">
                            <v-icon>mdi-close</v-icon>
                        </v-btn>
                        <v-toolbar-title>Search Transaction</v-toolbar-title>
                        <v-spacer></v-spacer>
                    </v-toolbar>
                    <div>
                        <br>
                        <v-row>
                            <v-col cols="12" sm="12">
                                <v-card class="inline d-flex ma-4 pa-4 elevation-0">
                                    <v-menu v-model="menu1" :close-on-content-click="false" :nudge-right="40" transition="scale-transition" offset-y min-width="auto">
                                        <template v-slot:activator="{ on, attrs }">
                                            <v-text-field v-model="startdate" label="Start Date" prepend-icon="mdi-calendar" readonly v-bind="attrs" v-on="on"></v-text-field>
                                        </template>
                                        <v-date-picker v-model="startdate" :max="enddate" @input="menu1 = false"></v-date-picker>
                                    </v-menu>&nbsp; &nbsp;
                                    <v-menu v-model="menu2" :close-on-content-click="false" :nudge-right="40" transition="scale-transition" offset-y min-width="auto">
                                        <template v-slot:activator="{ on, attrs }">
                                            <v-text-field v-model="enddate" label="End Date" prepend-icon="mdi-calendar" readonly v-bind="attrs" v-on="on"></v-text-field>
                                        </template>
                                        <v-date-picker v-model="enddate" :min="startdate" @input="menu2 = false"></v-date-picker>
                                    </v-menu>&nbsp;&nbsp;
                                    <v-btn color="primary" dark dense @click="Searchtranscations()" :loading="loader">Search</v-btn>
                                </v-card>
                            </v-col>
                        </v-row>
                        <br>
                        <v-data-table :items="tlist" :headers="headers" class="elevation-1 ma-4 pa-4" :loading="loader">
                            <template v-slot:item.credit="{ item }">
                                <p v-if="item.transactiontype == 'credit'">{{ item.amount }}</p>
                            </template>
                            <template v-slot:item.debit="{ item }">
                                <p v-if="item.transactiontype == 'debit'">{{ item.amount }}</p>
                            </template>
                        </v-data-table>
                    </div>
                </v-card>
          </v-dialog>
        </div>
    </div>
</template>

<script>
import {WalletMixin} from '@/mixins/walletmixins'
export default {
    mixins : [WalletMixin],
    data () {
        return {
            dialog: false,
            headers: [
                { text: 'User', sortable:false ,value: 'user.phonenumber' },
                { text: 'Date', sortable:false ,value: 'date_format' },
                { text: 'Credit',sortable:false, value: 'credit' },
                { text: 'Debit',sortable:false, value: 'debit' },
            ],
            tlist : [],
            loader : false,
            menu1 : false,
            startdate : '',
            menu2 : false,
            enddate : '',
        }
    },

    mounted(){
        this.getDefaultDates()  
    },

    methods : {
        getDefaultDates() {
            const currentDate = new Date()
            const year = currentDate.getFullYear()
            const month = currentDate.getMonth()
            const firstDay = new Date(year, month, 2).toISOString().substr(0, 10)
            const lastDay = new Date(year, month + 1, 1).toISOString().substr(0, 10)
            this.startdate = firstDay
            this.enddate = lastDay
            this.Searchtranscations()
        },
        Searchtranscations(){
            if(!this.startdate){
                this.$store.dispatch('WalletStore/dispatch_snackbar',{ 'snackbar' : true, 'snackbartext' : 'Start Date is required','snackbarcolor' : 'error'})
                return false
            }
            if(!this.enddate){
                this.$store.dispatch('WalletStore/dispatch_snackbar',{ 'snackbar' : true, 'snackbartext' : 'Start Date is required','snackbarcolor' : 'error'})
                return false
            }
            this.loader = true
            this.GET_API('/transaction/?startdate='+this.startdate+'&enddate='+this.enddate)
            .then(data => {
                this.tlist = data.data
                this.loader = false
            })
            .catch(err => {
                console.log(err)
                this.loader = false
            })
        },
    }
}
</script>