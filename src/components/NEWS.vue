<template>
  <div class="hello">
    <h1>这是新闻页面</h1>

    <span>这个是？后的值{{$route.query.news}}</span> <!--$route.query查询？后的值， news是？后面的key -->
  </div>
</template>

<script>
export default {
  name: 'NEWS',
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
