<template>
  <div class="home">
      <form>
        <input placeholder="item" v-model="value">
        <button type="submit" @click.prevent="addfunction">add</button>
      </form>
        <div v-for="item in mylist" :key="item">
          <listitem :item='item' ></listitem>
      </div>
  </div>
</template>

<script>
import listitem from '../components/listitem.vue'
// @ is an alias to /src

export default {
    components: { listitem },
  name: 'Home',
  data(){
      return {
          mylist: ['orange 1','banana 2'],
          value:''
      };
  },

  methods:{
        addfunction(){
            this.mylist.push(this.value);
            this.value =''
        }
      }


}
</script>
<style scoped>
.hide {
    visibility: hidden !important;
}

</style>
