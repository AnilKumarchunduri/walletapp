import { mapGetters,  mapActions} from 'vuex'

export const WalletMixin = {
    computed : {
        ...mapGetters('WalletStore',['GetterSnackBarData'])
    },
    methods:{
        ...mapActions('WalletStore', ['get_users','GET_API','POST_API']),
    }
}