
import axios from "axios"
const wallet_axios_url=process.env.VUE_APP_Backed_API_URL
var wallet_axios = axios.create({
    baseURL: wallet_axios_url,
    withCredentials: false
})
function getCookie(name) {
    if (!document.cookie) {
        return null;
    }
    const xsrfCookies = document.cookie.split(';')
        .map(c => c.trim())
        .filter(c => c.startsWith(name + '='));

    if (xsrfCookies.length === 0) {
        return null;
    }
    return decodeURIComponent(xsrfCookies[0].split('=')[1]);
}
wallet_axios.interceptors.request.use(function (config) {
    var csrfToken = getCookie('csrftoken');
    if (csrfToken) {
        config.headers['X-CSRFToken'] = csrfToken;
    }
    return config;
});

export default wallet_axios