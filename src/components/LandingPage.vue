<template>
    <div>
        <div>
            <v-card class="elevation-0 mt-0">
                <router-view></router-view>
            </v-card>
        </div>
    </div>
</template>

<script>
import {WalletMixin} from '@/mixins/walletmixins'
export default {
    mixins : [WalletMixin],
    data() {
        return {
            snackbar : true,
            snackbartext : '',
            snackbarcolor : 'success'
        }
    },
}
</script>