import { createApp } from "vue";
import { createPinia } from "pinia";
import App from "./App.vue";
import router from "./router";
import { setupPrimeVue } from "./plugins/primevue";
import "./assets/styles/main.css";

const app = createApp(App);

app.use(createPinia());
app.use(router);
setupPrimeVue(app);

app.mount("#app");
