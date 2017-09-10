import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import './scss/reset.css'
import About from './component/home/about'


Vue.use(ElementUI)

new Vue({
    el: '#about',
    render: h => h(About)
})