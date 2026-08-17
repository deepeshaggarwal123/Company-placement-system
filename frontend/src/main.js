// frontend/src/main.js

import { createApp } from "vue"
import App from "./App.vue"
import router from "./router"
import auth from "./store/auth"

// Bootstrap CSS
import "bootstrap/dist/css/bootstrap.min.css"

// Bootstrap JS
import "bootstrap/dist/js/bootstrap.bundle.min.js"

// Create Vue Application
const app = createApp(App)

// Expose auth store for components
app.config.globalProperties.$auth = auth

// Use Router
app.use(router)

// Mount Application
app.mount("#app")

