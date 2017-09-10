import Vue from 'vue'
import './scss/reset.css'
import Index from './component/home/index'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-default/index.css'

Vue.use(ElementUI)

new Vue({
  el: '#index',
  render: h => h(Index)
})