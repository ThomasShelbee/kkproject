import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.min.js'
import './assets/main.css'
import { createWebHistory, createRouter } from 'vue-router'
import ItemList from './components/ItemList.vue'
import ItemPage from './components/ItemPage.vue'
import {getItems} from "@/api";

const routes = [
    { path: '/', component: ItemList },
    { path: '/item/:url', component: ItemPage },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})
import {createApp, reactive} from 'vue'
import App from './App.vue'

const app = createApp(App)
app.config.globalProperties.items = await getItems();
app.config.globalProperties.promoUsed = reactive({title: "", price: 0});
app.config.globalProperties.message = reactive({text: ""});
app.config.globalProperties.cartItems = reactive([]);
app.config.globalProperties.category = reactive({
    page: "all"
});
app.use(router).mount('#app')
