<template>
  <div >
      <ul>
      <li   v-show="isActive">{{ returnData }} <button @click="toggle">X</button></li>
      </ul>
  </div>
</template>

<script>
export default {
  name: 'listitem',
  props: ['item'],

  data() {
    return {
      isActive: true
    }
  },
  computed:{
      returnData(){
          return this.item
      }
  },
    methods: {
    toggle() {
      this.isActive = !this.isActive;
    }

  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
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
