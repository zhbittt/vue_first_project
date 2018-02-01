<template>
  <div >
    <h1>这是首页</h1>
    <span>这个是url的值{{$route.params.id1}}</span><br>
    <span>这个是url的值{{$route.params.id2}}</span><br>
    <span>这个是url的值{{$route.query.news}}</span><br>

  </div>
</template>

<script>
export default {
  name: 'ALL',
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
