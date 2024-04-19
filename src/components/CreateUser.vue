<template>
    <div>
        <div>
            <v-dialog v-model="dialog" max-width="600" persistent>
                <template v-slot:activator="{  on, attrs }">
                    <v-btn small text outlined dense color="primary" v-bind="attrs" v-on="on"><v-icon>mdi-plus</v-icon>Create User</v-btn>
                </template>
                <v-card :disabled="loader">
                    <v-card-title class="text-h5">Create User</v-card-title>
                    <v-card-text>
                        <v-row>
                            <v-col cols="12" sm="6">Name :</v-col>
                            <v-col cols="12" sm="6">
                                <v-text-field dense outlined label="" type="number" v-model="phonenumber"></v-text-field>
                            </v-col>
                            <v-col cols="12" sm="6">Wallet Type</v-col>
                            <v-col cols="12" sm="6">
                                <v-autocomplete dense outlined label="" v-model="wallettype" :items="wallettypeitems" item-text="name" item-value="id"></v-autocomplete>
                            </v-col>
                        </v-row>
                    </v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn color="grey darken-1" text @click="dialog = false;phonenumber='';wallettype=''">cancel</v-btn>
                      <v-btn color="green darken-1" :disabled="phonenumber=='' || wallettype==''" :loading="loader" text @click="adduser()">Add User</v-btn>
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
            phonenumber : '',
            wallettype : '',
            loader : false,
            wallettypeitems : [],
            wallettypeloader : false,
        }
    },
    mounted(){
        this.get_wallet_type()
    },
    methods : {
        get_wallet_type(){
            this.wallettypeloader = true 
            this.GET_API('/wallettype/')
            .then(data => {
                this.wallettypeitems = data.data
                this.wallettypeloader = false

            })

        },
        adduser(){
            this.loader = true
            var rdata = {}
            rdata['query'] = '/users/'
            rdata['phonenumber'] = this.phonenumber
            rdata['wallettype'] = this.wallettype
            this.POST_API(rdata)
            .then(data => {
                console.log(data)
                this.loader = false
                this.dialog = false
                this.phonenumber = ''
                this.wallettype = ''
                this.$emit('refresh')
            })
            .catch(err => {
                console.log(err)
                this.loader = false
            })
        },
    },

}
</script>