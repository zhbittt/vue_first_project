<template>
  <div class="hello">
    <h1>这是电影页面</h1>
    <span>{{$route.params.movieId}}</span> <!-- $route.params获取url的动态值        movieId在index.js的路由里设置的名字   -->
  </div>
</template>

<script>
export default {
  name: 'MOVIE',
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
