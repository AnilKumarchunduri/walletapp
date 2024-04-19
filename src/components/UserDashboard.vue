<template>
    <!-- eslint-disable -->
    <div>
        <div class="pa-2 ma-2">
            <div class="inline d-flex ma-4 justify-end">
                    <createuser @refresh="get__users"></createuser>&nbsp;&nbsp;
                    <search></search>&nbsp;&nbsp;&nbsp;&nbsp;
            </div><br>
            <v-data-table :items="ulist" :headers="headers" class="elevation-1 ma-4 pa-4" :loading="loader">
                <template v-slot:top>
                    <h3>User List</h3>
                </template>
                <template v-slot:item.credit="{ item }">
                    <credit :item="item" @refresh="get__users"></credit>
                </template>
                <template v-slot:item.debit="{ item }">
                    <debit :item="item" @refresh="get__users"></debit>
                </template>
                <template v-slot:item.balance="{ item }">
                    <v-progress-circular v-if="item.balanceloader" indeterminate value="10"></v-progress-circular>
                    <template v-else-if="item.balance">
                        {{ item.balance[item.wallettype_name] }}

                    </template>
                    <a v-else @click="getbalance(item)">Balance</a>
                </template>
            </v-data-table>
        </div>
    </div>
</template>

<script>
import {WalletMixin} from '@/mixins/walletmixins'
import createuser from '@/components/CreateUser.vue'
import credit from '@/components/Credit-Dialog.vue'
import debit from '@/components/Debit-Dialog.vue'
import search from '@/components/SearchTranscations.vue'
export default {
    mixins : [WalletMixin],
    components : { credit, debit, createuser, search },
    data () {
        return {
            ulist : [],
            headers: [
                { text: 'User', sortable:false ,value: 'phonenumber' },
                { text: 'Wallet Type',sortable:false, value: 'wallettype_name' },
                { text: 'Credit',sortable:false, value: 'credit' },
                { text: 'Debit', sortable:false, value: 'debit' },
                { text: 'Balance',sortable:false, value: 'balance' },
            ],
            loader : false,

        }
    },

    mounted(){
        this.get__users()
    },

    methods : {
        get__users(){
            this.loader = true
            this.get_users()
            .then(data => {
                console.log(data)
                this.ulist = data.data
                this.loader = false
            })
        },

        getbalance(item){
            this.loader = true
            var editedIndex = this.ulist.indexOf(item)
            item.balanceloader = true
            this.GET_API('/users/'+item.phonenumber+'/balance/')
            .then(data => {
                item.balance = data.data
                item.balanceloader = false
                this.ulist[editedIndex] = item
                this.loader = false
            })
        }
    }
}
</script>