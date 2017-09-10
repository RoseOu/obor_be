import Vue from 'vue'
import VueRouter from 'vue-router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import './scss/reset.css'
import Index from './component/management/list'
import User from './component/management/user'
import Erwei from './component/management/erWei'
import UploadPic from './component/management/uploadPic'
import Words from './component/management/words'
import Tech from './component/management/technology'
import UploadBanner from './component/management/uploadBanner'
import AddArticle from './component/management/addArticle'

Vue.use(VueRouter)
Vue.use(ElementUI)

const Bike = Vue.extend({
    name: "Bike",
    mixins: [Words]
})

const Aerospace = Vue.extend({
    name: "Aerospace",
    mixins: [Words]
})

const Navigation = Vue.extend({
    name: "Navigation",
    mixins: [Words]
})
const Bridge = Vue.extend({
    name: "Bridge",
    mixins: [Words]
})
const Confucius = Vue.extend({
    name: "Confucius",
    mixins: [Words]
})
const Railway = Vue.extend({
    name: "Railway",
    mixins: [Words]
})
const Robot = Vue.extend({
    name: "Robot",
    mixins: [Words]
})
const Uav = Vue.extend({
    name: "UAV",
    mixins: [Words]
})
const Shopping = Vue.extend({
    name: "Shopping",
    mixins: [Words]
})
const Energy = Vue.extend({
    name: "Energy",
    mixins: [Words]
})
const Alipay = Vue.extend({
    name: "Alipay",
    mixins: [Words]
})
const Acupuncture = Vue.extend({
    name: "Acupuncture",
    mixins: [Words]
})

const router = new VueRouter({
    mode: 'history',
    base: __dirname,
    routes: [
        { path: '/manage', component: User },
        { path: '/2', component: UploadPic },
        { path: '/4', component: UploadPic },
        { path: '/3', component: Erwei },
        { path: '/5', component: UploadBanner },
        { path: '/6', component: AddArticle },
        { path: '/7', component: Tech },
        { path: '/1-1', component: Bike },
        { path: '/1-2', component: Aerospace },
        { path: '/1-3', component: Navigation },
        { path: '/1-4', component: Bridge },
        { path: '/1-5', component: Confucius },
        { path: '/1-6', component: Railway },
        { path: '/1-7', component: Robot },
        { path: '/1-8', component: Uav },
        { path: '/1-9', component: Shopping },
        { path: '/1-10', component: Energy },
        { path: '/1-11', component: Alipay },
        { path: '/1-12', component: Acupuncture }
    ]
})

new Vue({
    router,
    el: '#manage',
    render: h => h(Index)
})
