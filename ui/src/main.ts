import PrimeVue from 'primevue/config'
import { createApp } from 'vue'

import App from './App.vue'
import './assets/base.css'
import router from './router'

const app = createApp(App)

app.use(router)
app.use(PrimeVue, {
  theme: 'none',
})

app.mount('#app')
