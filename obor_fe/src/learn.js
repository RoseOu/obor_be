import Vue from 'vue'
import VueRouter from 'vue-router'
import './scss/reset.css'
import Words from './component/management/words'
import Learn from './component/home/learn'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'

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
        { path: '/learn/1-1', component: Bike },
        { path: '/learn/1-2', component: Aerospace },
        { path: '/learn/1-3', component: Navigation },
        { path: '/learn/1-4', component: Bridge },
        { path: '/learn/1-5', component: Confucius },
        { path: '/learn/1-6', component: Railway },
        { path: '/learn/1-7', component: Robot },
        { path: '/learn/1-8', component: Uav },
        { path: '/learn/1-9', component: Shopping },
        { path: '/learn/1-10', component: Energy },
        { path: '/learn/1-11', component: Alipay },
        { path: '/learn/1-12', component: Acupuncture }
    ]
})


new Vue({
  router,
  el: '#learn',
  render: h => h(Learn)
})