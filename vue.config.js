const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  "assetsDir": "wallet/static/",
  transpileDependencies: [
    'vuetify'
  ]
})
