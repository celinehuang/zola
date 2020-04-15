<template>
  <q-card class="my-card">
    <q-img v-bind:src="photo" :ratio="1">
      <div class="price-caption">{{ price | formatPrice }}</div>
    </q-img>

    <q-card-section>
      <div class="text-h6">{{ title}}</div>
      <div class="text-subtitle2">{{ artist }}</div>
    </q-card-section>

    <q-card-actions>
      <q-btn flat color="primary" icon="add_shopping_cart" @click="addToCart(id)" />
      <q-btn flat color="primary" label="Buy Now" />
      <q-space />
      <q-btn
        color="primary"
        round
        flat
        dense
        :icon="expanded ? 'keyboard_arrow_up' : 'keyboard_arrow_down'"
        @click="expanded = !expanded"
      />
    </q-card-actions>

    <q-slide-transition>
      <div v-show="expanded">
        <q-separator />
        <q-card-section class="text-subitle2">{{ description }}</q-card-section>
      </div>
    </q-slide-transition>
  </q-card>
</template>

<script>
export default {
  name: "Item",

  data() {
    return {
      expanded: false
    };
  },
  props: ["id", "description", "price", "photo", "title", "artist"],
  methods: {
    addToCart(id) {
      this.$store.dispatch("addToCart", id);
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