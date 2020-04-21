<template>
  <div class="col-md-3 col-sm-6 col-xs-12">
    <q-card class="my-card">
      <q-img v-bind:src="photo" :ratio="1">
        <div class="price-caption">{{ price | formatPrice }}</div>
      </q-img>

      <q-card-section class="title-artist">
        <div class="text-h6">{{ title }}</div>
        <div class="text-subtitle2">{{ artist }}</div>
      </q-card-section>
      <q-card-section>
        <div class="text-subtitle2">Order date: {{ pDate }}</div>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
export default {
  name: "HistoryItem",

  data() {
    return {
      expanded: false
    };
  },
  props: [
    "item",
    "id",
    "description",
    "price",
    "photo",
    "title",
    "artist",
    "pDate"
  ],
  methods: {
    addToCart(item) {
      this.$store.dispatch("addToCart", item);
    }
  },
  filters: {
    formatPrice: function(value) {
      return "$" + value.toString();
    }
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
