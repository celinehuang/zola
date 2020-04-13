<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <q-card class="my-card" v-for="item in items" :key="item.id">
      <q-img v-bind:src="item.photo" :ratio="1">
        <div class="price-caption">{{ item.price | formatPrice }}</div>
      </q-img>
      <q-card-section>
        <div class="text-h6">Title</div>
        <div class="text-subtitle2">Artist</div>
      </q-card-section>

      <q-card-actions>
        <q-btn flat color="primary" icon="add_shopping_cart" />
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
          <q-card-section class="text-subitle2">{{ item.description }}</q-card-section>
        </div>
      </q-slide-transition>
    </q-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: null,
      expanded: false
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
