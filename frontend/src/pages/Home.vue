<template>
  <div class="container">
    <div class="q-pa-md row justify-center items-start q-gutter-md">
      <Item
        style="margin: 10px"
        v-for="item in items"
        v-bind:key="item.id"
        :item="item"
        :artist="item.artist"
        :title="item.title"
        :id="item.id"
        :description="item.description"
        :price="item.price"
        :photo="item.photo"
      />
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
      .get("api/items/")
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

<style scoped>
.container {
  padding: 20px;
  justify-content: center;
}
</style>
