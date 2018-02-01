<template>
  <div >
  <router-link to='/'>首页</router-link>
  <router-link to='/hw'>hellowork</router-link>
  <router-link to='/news'>新闻</router-link>
  <router-link to='/movie/23'>电影</router-link>
  <router-link to='/goods'>购物</router-link>

  <!--<router-view/>-->

  </div>
</template>

<script>
export default {
  name: 'Navbar',
  data () {
    return {
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
