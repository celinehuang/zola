<template>
  <q-layout>
    <q-page-container>
      <q-page>
        <div class="q-pa-md row justify-center items-start q-gutter-md">
          <div class="col-md-4 col-sm-7 col-xs-12">
            <q-card>
              <q-toolbar style="background-color:primary">
                <q-toolbar-title>Checkout</q-toolbar-title>
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
          </div>
          <div class="col-md-5 col-sm-6 col-xs-12">
            <q-card class="payment">
              <q-toolbar style="background-color:primary">
                <q-toolbar-title>Payment</q-toolbar-title>
              </q-toolbar>
              <q-card-section>
                <q-form class="q-gutter-md q-ma-md">
                  <q-input filled v-model="name" label="Name" />
                  <q-input filled v-model="shipping_addr" label="Shipping Address" />
                  <q-input filled v-model="cardNum" label="Card Number" />

                  <q-input filled v-model="expDate" label="MM/YY" />
                  <q-input filled v-model="cvc" label="CVC" />
                </q-form>
              </q-card-section>
              <q-card-actions align="right">
                <q-btn flat color="primary" @click="checkout(inCart)" to="/home">Checkout</q-btn>
              </q-card-actions>
            </q-card>
          </div>
        </div>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: "checkout",
  data() {
    return {};
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
    },
    emptyCart() {
      this.$store.dispatch("emptyCart");
    },
    checkout(inCart) {
      let requests = [];

      for (var i = 0; i < inCart.length; i++) {
        var formData = new FormData();
        formData.append("inventory_count", inCart[i].inventory_count - 1);
        this.$axios
          .patch("/api/items/" + inCart[i].id + "/", formData)
          .catch(err => {
            this.$q.notify({
              color: "red-4",
              position: "top",
              textColor: "white",
              icon: "error",
              message: "Something went wrong, please try again"
            });
          });
      }
      this.emptyCart();
    }
  }
};
</script>

<style lang="stylus" scoped>
.payment {
  height: 100%;
  padding: 20px;
}
</style>