import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
import './scss/reset.css'
import Login from './component/management/login'


Vue.use(ElementUI)

new Vue({
    el: '#login',
    render: h => h(Login)
})