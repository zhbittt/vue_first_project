<template>
  <div >
    <h1>这里商品是标题子页面</h1>
    <router-link to="/news?news=查看新闻">查看新闻</router-link>
    <button @click="jump">button - 跳转到新闻页面</button>
  </div>
</template>

<script>
export default {
  name: 'Title',
  data () {
    return {
    }
  },
  methods:{
      jump(){
          this.$router.push({path:'/news?news=button - 跳转到新闻页面'})
//        this.$route.go(-2) //倒退两步
      }
  }

}
</script>



<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
