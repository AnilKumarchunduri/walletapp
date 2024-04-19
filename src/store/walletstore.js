import wallet_axios from "@/repo";


const state = {
    snackbardata : {
        'snackbar' : false,
        'snackbartext' : '',
        'snackbarcolor' : ''
    }
}

const getters = {
    GetterSnackBarData: (state) => state.snackbardata,
}
const actions = {
    get_users({commit}){
        return new Promise((resolve, reject) => {
            wallet_axios.get('/users/')
            .then(data => {
                resolve(data)
            })
            .catch(err => {
                reject(err)
            })
        })
    },

    GET_API({commit}, query){
        return new Promise((resolve, reject) => {
            wallet_axios.get(query)
            .then(data => {
                resolve(data)
            })
            .catch(err => {
                reject(err)
            })
        })
    },

    POST_API({commit}, data){
        return new Promise((resolve, reject) => {
            wallet_axios.post(data['query'], data)
            .then(data => {
                resolve(data)
            })
            .catch(err => {
                reject(err)
            })
        })
    },

    dispatch_snackbar({ commit }, value) {
        commit('mutationsnackbar', value)
    },
}

const mutations = {  
    mutationsnackbar(state, data){
        state.snackbardata = Object.assign(state.snackbardata,data)
    },
}

export const WalletStore = {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};