<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <q-card v-for="item in items" :key="item.id">
      <img v-bind:src="item.photo" />
      <q-card-section>
        <div class="text-h6">{{ item.mediatype }}</div>
        <div class="text-subtitle2">{{ item.description }}</div>
      </q-card-section>

      <q-card-actions>
        <q-btn color="primary" label="Add to Cart" />
        <q-btn color="secondary" label="Buy Now" />
      </q-card-actions>
    </q-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: null
    };
  },
  created() {
    console.log("getItems called");
    this.$axios.get("http://localhost:8000/api/items/").then(response => {
      this.items = response.data;
    });
  }
};
</script>

<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 500px
</style>
