<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <div v-for="item in curr_users_items" v-bind:key="item.id">
      <Item :id="item.id" :description="item.description" :price="item.price" :photo="item.photo" :title="item.title" :artist="item.artist"/>
    </div>
  </div>
</template>

<script>
import Item from "../components/Item.vue";

export default {
  data() {
    return {
      items: null,
      curr_users_items: null,
      username: this.$store.state.currentUser.username,
      name: this.$store.state.currentUser.name,
      shipping_addr: this.$store.state.currentUser.shipping_addr,
      email: this.$store.state.currentUser.email,
      profile_pic: this.$store.state.currentUser.profile_pic,
      id: this.$store.state.currentUser.id,
      token: this.$store.state.token
    };
  },
  methods: {},
  components: {
    Item
  },
  created() {
    console.log(this.id);
    var self = this;
    this.$axios
      .get("http://localhost:8000/api/items/")
      .then(response => {
        this.items = response.data;
        console.log(self.id);
        console.log(this.username)
        this.curr_users_items = {};
        Object.keys(this.items).forEach((key) => {
            console.log(this.items[key].username, this.id)
            if (this.items[key].username == this.id) {
                this.curr_users_items[key] = this.items[key]
            }
        })
        console.log(this.curr_users_items)
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

<style lang="sass" scoped>
</style>
