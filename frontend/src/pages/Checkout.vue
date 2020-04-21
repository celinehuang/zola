<template>
  <q-layout>
    <div class="text-h2">hello</div>
    <q-page-container>
      <q-card class="cart-cards">
        <q-toolbar style="background-color:primary">
          <q-toolbar-title>Shopping Cart</q-toolbar-title>
          <q-btn flat round dense icon="close" v-close-popup />
        </q-toolbar>

        <q-card-section>
          <q-list style="min-width: 350px">
            <q-item class="list-items" v-for="(item, index) in inCart" v-bind:key="item.id">
              <q-item-section>
                <q-avatar rounded>
                  <img v-bind:src="item.photo" />
                </q-avatar>
              </q-item-section>

              <q-item-section>
                <q-item-label lines="1">{{item.title}}</q-item-label>
                <q-item-label caption>{{item.artist}}</q-item-label>
              </q-item-section>
              <q-item-section>{{item.price | formatPrice}}</q-item-section>

              <q-item-section>
                <q-btn flat icon="delete" @click="removeFromCart(index)"></q-btn>
              </q-item-section>
            </q-item>
          </q-list>
        </q-card-section>

        <div v-if="inCart.length > 0">
          <q-card-section align="right">
            <div class="text-subtitle">Total: {{totalPrice | formatPrice}}</div>
          </q-card-section>
        </div>
      </q-card>
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: "checkout",
  data() {
    return {
      forSale: null
    };
  },
  filters: {
    formatPrice: function(value) {
      return "$" + value.toString();
    }
  },
  computed: {
    inCart() {
      return this.$store.getters.inCart;
    },
    totalPrice() {
      return this.inCart.reduce(
        (acc, cur) => parseFloat(acc) + parseFloat(cur.price),
        0
      );
    }
  },
  methods: {
    removeFromCart(index) {
      this.$store.dispatch("removeFromCart", index);
    }
  }
};
</script>