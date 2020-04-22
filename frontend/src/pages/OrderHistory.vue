<template>
  <div class="container">
    <div class="q-pa-md row justify-center items-start q-gutter-md">
      <HistoryItem
        style="margin: 10px"
        v-for="item in userItemsOrdered"
        v-bind:key="item.id"
        :item="item"
        :artist="item.artist"
        :title="item.title"
        :id="item.id"
        :description="item.description"
        :price="item.price"
        :photo="item.photo"
        :pDate="item.pDate"
      />
    </div>
  </div>
</template>

<script>
import HistoryItem from "../components/HistoryItem.vue";

export default {
  data() {
    return {
      userOrders: null,
      userItemsOrdered: null,
      userId: this.$store.state.currentUser.id
    };
  },
  methods: {
    getUserPayments() {
      this.$axios
        .get("/api/payments/")
        .then(response => {
          var orders = response.data;
          //   console.log(orders);
          this.userOrders = {};
          Object.keys(orders).forEach(key => {
            if (orders[key].username == this.userId) {
              this.userOrders[key] = orders[key];
            }
          });
          this.getUserItemsOrdered();
        })
        .catch(() => {
          this.$q.notify({
            color: "negative",
            position: "top",
            message: "Loading failed",
            icon: "report_problem"
          });
        });
    },
    getUserItemsOrdered() {
      var userOrders = this.userOrders;
      this.$axios
        .get("/api/items/")
        .then(response => {
          var items = response.data;

          this.userItemsOrdered = {};

          Object.keys(items).forEach(itemKey => {
            Object.keys(userOrders).forEach(orderKey => {
              if (items[itemKey].id == userOrders[orderKey].iId) {
                items[itemKey].pDate = userOrders[orderKey].pDate;
                this.userItemsOrdered[itemKey] = items[itemKey];
              }
            });
          });
        })
        .catch(() => {
          this.$q.notify({
            color: "negative",
            position: "top",
            message: "Loading failed",
            icon: "report_problem"
          });
        });
      //   console.log(this.userItemsOrdered);
    }
  },
  components: {
    HistoryItem
  },
  created() {
    this.getUserPayments();
  }
};
</script>

<style scoped>
.container {
  padding: 20px;
  justify-content: center;
}
</style>