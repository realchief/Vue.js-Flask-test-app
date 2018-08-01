import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Variations from '@/components/Variations'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/variations',
      name: 'Variations',
      component: Variations
    }
  ]
})
