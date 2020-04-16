<template>
  <q-layout>
    <q-page-container>
      <q-page class="q-mx-xl q-mb-md q-mt-md">
        <q-toolbar>
          <q-toolbar-title class="text-bold q-px-lg q-pt-lg">
            Add A New Item
          </q-toolbar-title>
        </q-toolbar>
        <q-form @submit="createitem" class="q-gutter-lg q-ma-xl">
          <q-input filled v-model="title" label="Title" />
          <q-input filled v-model="artist" label="Artist" />
          <q-select
            filled
            v-model="genre"
            :options="genreOptions"
            label="Genre"
          />
          <q-input filled v-model="description" label="Description" />
          <q-select
            filled
            v-model="mediatype"
            :options="mediatypeOptions"
            label="Media Type"
          />
          <q-input
            filled
            stack-label
            v-model="release_year"
            type="date"
            label="Release Date"
          />
          <q-input
            filled
            v-model="price"
            mask="#.##"
            fill-mask="0"
            reverse-fill-mask
            label="Price"
          />
          <q-input
            filled
            v-model="inventory_count"
            type="number"
            label="Inventory"
          />
          <q-input
            filled
            stack-label
            v-model="photo"
            type="file"
            @change="onFileChanged"
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
        <q-separator inset />
        <q-toolbar>
          <q-toolbar-title class="text-bold q-px-lg q-pt-lg">
            Your Listings
          </q-toolbar-title>
        </q-toolbar>
        <div class="q-pa-md row items-start q-gutter-md thing">
          <div v-for="item in curr_users_items" v-bind:key="item.id">
            <YourItem
              :id="item.id"
              :description="item.description"
              :price="item.price"
              :photo="item.photo"
              :title="item.title"
              :artist="item.artist"
              :genre="item.genre"
              :mediatype="item.mediatype"
              :inventory_count="item.inventory_count"
              :release_year="item.release_year"
              @item-updated="getUserItems"
            />
          </div>
        </div>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>
import YourItem from "../components/YourItem.vue";

export default {
  data() {
    return {
      mediatypeOptions: ["Vinyl", "CD", "Cassette", "DVD", "Box Set"],
      genreOptions: [
        "Alternative",
        "Blues",
        "Classical",
        "Country",
        "Electronic",
        "Folk",
        "Hip Hop",
        "Jazz",
        "Metal",
        "Pop",
        "Punk",
        "Rock",
        "R&B"
      ],
      inventory_count: null,
      price: null,
      artist: null,
      genre: null,
      title: null,
      description: null,
      mediatype: null,
      release_year: null,
      photo: null,

      items: null,
      curr_users_items: null,

      username: this.$store.state.currentUser.username,
      name: this.$store.state.currentUser.name,
      shipping_addr: this.$store.state.currentUser.shipping_addr,
      email: this.$store.state.currentUser.email,
      oldPic: this.$store.state.currentUser.oldPic,
      id: this.$store.state.currentUser.id,
      token: this.$store.state.token
    };
  },
  components: {
    YourItem
  },
  methods: {
    methodThatForcesUpdate() {
      this.$forceUpdate(); // Notice we have to use a $ here
    },
    onFileChanged: function(event) {
      //   console.log(event.target.files[0].type);
      this.newPic = event.target.files[0];
      this.oldPic = URL.createObjectURL(event.target.files[0]);
    },
    createitem() {
      const formData = new FormData();
      formData.append("inventory_count", this.inventory_count);
      formData.append("price", this.price);
      formData.append("artist", this.artist);
      formData.append("genre", this.genre);
      formData.append("description", this.description);
      formData.append("mediatype", this.mediatype);
      formData.append("release_year", this.release_year);
      formData.append("photo", this.newPic);
      formData.append("username", this.id);
      formData.append("title", this.title);

      this.$axios
        .post("/api/items/", formData, {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        })
        .then(resp => {
          this.$q.notify({
            color: "green-4",
            position: "top",
            textColor: "white",
            icon: "cloud_done",
            message: "Successfully Created Listing"
          });
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
    },
    getUserItems() {
      this.$axios
        .get("http://localhost:8000/api/items/")
        .then(response => {
          this.items = response.data;
          console.log(this.items);
          this.curr_users_items = {};
          Object.keys(this.items).forEach(key => {
            if (this.items[key].username == this.id) {
              this.curr_users_items[key] = this.items[key];
            }
          });
          console.log(this.curr_users_items);
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
  },

  created() {
    this.getUserItems();
  }
};
</script>

<style scoped>
.thing {
  padding-top: 20px;
}
</style>
