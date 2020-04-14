<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <div class="col-grow" v-for="item in items" v-bind:key="item.id">
      <Item :id="item.id" :description="item.description" :price="item.price" :photo="item.photo" />
    </div>
  </div>
</template>

<script>
import Item from "../components/Item.vue";

export default {
  data() {
    return {
      items: null
    };
  },
  methods: {},
  components: {
    Item
  },
  created() {
    this.$axios
      .get("http://localhost:8000/api/items/")
      .then(response => {
        this.items = response.data;
      })
      .catch(() => {
        this.$q.notify({
          color: "negative",
          position: "top",
          message: "Loading failed",
          icon: "report_problem"
        });
      });
  }
};
</script>

<style lang="sass" scoped>
</style>
