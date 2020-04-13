<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <q-card class="my-card" v-for="item in items" :key="item.id">
      <q-img v-bind:src="item.photo" :ratio="1">
        <div class="price-caption">{{ item.price | formatPrice }}</div>
      </q-img>
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
  methods: {},
  filters: {
    formatPrice: function(value) {
      return "$" + value.toString();
    }
  },
  created() {
    this.$axios.get("http://localhost:8000/api/items/").then(response => {
      this.items = response.data;
    });
  }
};
</script>

<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 400px

.price-caption
  position: absolute
  bottom: 10px
  left: 10px
  background-color: black
  border-radius: 5px
  height: auto
  width: auto
  padding: 5px
</style>
