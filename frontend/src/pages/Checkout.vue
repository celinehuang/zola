<template>
  <q-layout>
    <q-page-container>
      <q-page>
        <div class="q-pa-md row justify-center items-start q-gutter-md">
          <div class="col-grow col-sm-7 col-xs-12">
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
          <div class="col-grow col-sm-6 col-xs-12">
            <q-card class="payment">
              <q-toolbar style="background-color:primary">
                <q-toolbar-title>Payment</q-toolbar-title>
              </q-toolbar>
              <q-card-section>
                <q-form @submit="checkout" class="q-gutter-md q-ma-md">
                  <q-input
                    filled
                    v-model="name"
                    label="Name"
                    lazy-rules
                    :rules="[val => !!val || 'Field is required']"
                  />
                  <q-input
                    filled
                    v-model="shipping_addr"
                    label="Shipping Address"
                    lazy-rules
                    :rules="[val => !!val || 'Field is required']"
                  />
                  <q-input
                    filled
                    v-model="cardNum"
                    label="Card Number"
                    lazy-rules
                    :rules="[val => !!val || 'Field is required']"
                  />

                  <q-input
                    filled
                    v-model="expDate"
                    label="MM/YY"
                    lazy-rules
                    :rules="[val => !!val || 'Field is required']"
                  />
                  <q-input
                    filled
                    v-model="cvc"
                    label="CVC"
                    lazy-rules
                    :rules="[val => !!val || 'Field is required']"
                  />
                  <div>
                    <q-btn flat color="primary" type="submit" label="Checkout" />
                  </div>
                </q-form>
              </q-card-section>
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
    return {
      name: null,
      shipping_addr: this.shipping_addr,
      cardNum: this.cardNum,
      expDate: this.expDate,
      cvc: this.cvc,
      userId: this.$store.state.currentUser.id
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
    },
    emptyCart() {
      this.$store.dispatch("emptyCart");
    },
    getUniqueIds(inCart) {
      var uniqueIds = {};

      Object.keys(inCart).forEach(key => {
        var id = inCart[key].id;
        var inventory_count = inCart[key].inventory_count;
        if (!(id in uniqueIds)) {
          uniqueIds[id] = {};
          uniqueIds[id].numInCart = 1;
          uniqueIds[id].inventory_count = inventory_count;
        } else if (id in uniqueIds) {
          uniqueIds[id].numInCart += 1;
        }
      });
      return uniqueIds;
    },
    checkout() {
      var inCart = this.inCart;
      var uniqueIds = this.getUniqueIds(inCart);

      Object.keys(uniqueIds).forEach(id => {
        var itemData = new FormData();
        itemData.append(
          "inventory_count",
          uniqueIds[id].inventory_count - uniqueIds[id].numInCart
        );

        this.$axios
          .patch("/api/items/" + id + "/", itemData, {
            headers: {
              "Content-Type": "multipart/form-data"
            }
          })
          .catch(err => {
            this.$q.notify({
              color: "red-4",
              position: "top",
              textColor: "white",
              icon: "error",
              message: "Something went wrong, please try again"
            });
          });
      });

      for (var i = 0; i < inCart.length; i++) {
        var purchaseData = new FormData();

        purchaseData.append("username", this.userId);
        purchaseData.append("iId", inCart[i].id);
        purchaseData.append("shipping_addr", this.shipping_addr);
        purchaseData.append("total_amt", inCart[i].price);

        this.$axios
          .post("/api/payments/", purchaseData, {
            headers: {
              "Content-Type": "multipart/form-data"
            }
          })
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
      this.$router.push({ path: "/home" });
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