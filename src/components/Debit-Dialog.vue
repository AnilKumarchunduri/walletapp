<template>
    <div>
        <div>
            <v-dialog v-model="dialog" max-width="400" persistent>
                <template v-slot:activator="{  on, attrs }">
                    <a v-bind="attrs" v-on="on">debit</a>
                </template>
                <v-card :disabled="loader">
                    <v-card-title class="text-h5">Debit</v-card-title>
                    <v-card-text>
                        <v-row>
                            <v-col cols="12" sm="6">Name :</v-col>
                            <v-col cols="12" sm="6">{{ item.phonenumber }}</v-col>
                            <v-col cols="12" sm="6">Wallet Type</v-col>
                            <v-col cols="12" sm="6">{{ item.wallettype_name }}</v-col>
                            <v-col cols="12" sm="6">Current Balance</v-col>
                            <v-col cols="12" sm="6">{{ item.amount }}</v-col>
                            <v-col cols="12" sm="6">Amount</v-col>
                            <v-col cols="12" sm="6">
                                <v-text-field dense outlined label="" type="number" v-model="amount"></v-text-field>
                            </v-col>
                        </v-row>
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="grey darken-1" text @click="dialog = false;amount=0.00">cancel</v-btn>
                      <v-btn color="green darken-1" :disabled="amount<=0 || item.amount <= 0" :loading="loader" text @click="debitamount()">debit</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </div>
    </div>
</template>

<script>
import {WalletMixin} from '@/mixins/walletmixins'
export default {
    mixins : [WalletMixin],
    data() {
        return {
            dialog : false,
            amount : 0.00,
            loader : false,
        }
    },
    props : {
        item : { default : {} },
    },
    methods : {
        debitamount(){
            console.log(this.item)
            this.loader = true
            var rdata = {}
            rdata['query'] = '/transaction/debit/'
            rdata['user'] = this.item.id
            rdata['transactiontype'] = 'debit'
            rdata['amount'] = this.amount
            this.POST_API(rdata)
            .then(data => {
                console.log(data)
                this.loader = false
                this.dialog = false
                this.amount = 0.00
                this.$emit('refresh')
            })
            .catch(err => {
                console.log(err)
                console.log(err.response)
                var errmessg = ''
                this.loader = false
                for(var k in err.response.data) {
                    console.log(k, err.response.data[k]);
                    errmessg += k+ ' : ' + err.response.data[k][0]+'\n'
                }
                this.$store.dispatch('WalletStore/dispatch_snackbar',{ 'snackbar' : true, 'snackbartext' : errmessg,'snackbarcolor' : 'error'})
                this.loader = false
            })
        },
    },

}
</script>