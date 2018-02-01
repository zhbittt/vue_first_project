import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import NEWS from '@/components/news'
import ALL from '@/components/all'
import MOVIE from '@/components/movie'
import GoodsList from '@/views/GoodsList'
import Title from '@/views/Title'
import Image from '@/views/Image'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/goods',
      name: 'GoodsList',
      component: GoodsList,
      children: [
        {
          path: 'title', //   title   点击拼接上层url   例如   https://127.0.0.1:5000/goods
          name: 'title',                           //    点击title     https://127.0.0.1:5000/goods/title
          component: Title
        },
        {
          path: 'image',
          name: 'image',
          component: Image
        }
      ]
    },
    {
      path: '/hw',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/news',
      name: 'NEWS',
      component: NEWS
    },
    {
      path: '/all/:id1/:id2',  //url后动态的值 ：id
      name: 'ALL',
      component: ALL
    },
    {
      path: '/movie/:movieId',
      name: 'MOVIE',
      component: MOVIE
    }
  ],
  mode: 'history'  //    加上history，去除vue的url上的 #
})
