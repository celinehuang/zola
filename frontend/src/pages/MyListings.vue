<template>
<div>
  <div class="column thing">
    <div class="text-h5 text-weight-bold text-center text-primary" >
    ADD A NEW ITEM
    </div>
    <q-form @submit="test()" class="q-gutter-md" style="padding-right:20px;padding-left:20px;">
      <q-input
        filled
        label="Title"
      />
      <q-input
        filled
        label="Artist"
      />
      <q-input
        filled
        label="Genre"
      />
      <q-input
        filled
        label="Description"
      />
      <q-input
        filled
        label="Media Type"
      />
      <q-input
        filled
        type="date"
        label="Release Date"
      />
      <q-input
        filled
        v-model.number="model"
        type="number"
        label="Price"
      />
      <q-input
        filled
        v-model.number="model"
        type="number"
        label="Inventory"
      />
      <q-input
        filled
        type="file"
        label="Cover Art"
      />
      <div style="text-align:center;">
      <q-btn
        label="Create listing"
        type="submit"
        style="background:#cad5db;"
      />
      </div>
      </q-form>
  </div>

  <div class="text-h5 text-weight-bold text-center text-primary" style="padding-top:20px">
    YOUR LISTINGS
  </div>

  <div class="q-pa-md row items-start q-gutter-md thing">
    <div v-for="item in curr_users_items" v-bind:key="item.id">
      <YourItem :id="item.id" :description="item.description" :price="item.price" :photo="item.photo" :title="item.title" 
                :artist="item.artist" :genre="item.genre" :mediatype="item.mediatype"/>
    </div>
  </div>

</div>
</template>

<script>
import YourItem from "../components/YourItem.vue";

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
    YourItem
  },
  test() {

  },
  created() {
    console.log(this.id);
    var self = this;
    this.$axios
      .get("http://localhost:8000/api/items/")
      .then(response => {
        this.items = response.data;
        console.log(this.items)
        this.curr_users_items = {};
        Object.keys(this.items).forEach((key) => {
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

<style scoped>
.thing {
  padding-top: 20px
}
</style>
