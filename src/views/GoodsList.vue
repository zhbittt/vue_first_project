<template>
  <div >
    <h1>这是GoodsList页面</h1>
    <span>{{$route.params.goodsId}}</span><br>
    <span>{{$route.params.name}}</span>
    <router-link class="main" :to="{name:'MOVIE',params:{'movieId':123}}">查看电影页面</router-link><br>  <!-- 其实是生成a标签 -->
    <router-link class="left" to="/goods/title">显示商品标题</router-link>
    <router-link class="right" to="/goods/image">显示图片</router-link>


    <div>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: 'GoodsList',
  data () {
    return {
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .left,.right{
    float: left;
    width: 49%;
    border: 1px solid gray;
  }
</style>
