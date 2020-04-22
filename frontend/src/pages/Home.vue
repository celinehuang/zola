<template>
  <q-layout>
    <form @submit.prevent="onSearch" class="q-pa-md">
      <q-input rounded outlined v-model="text" label="Search" class="q-pa-lg q-mx-sm q-mt-sm">
        <template v-slot:append>
          <q-btn name="cancel" @click="clearSearch" class="cursor-pointer" />
        </template>
        <template v-slot:append>
          <q-icon name="search" />
        </template>
      </q-input>
    </form>
    <q-select
      borderless
      clearable
      v-model="sortBy"
      :options="options"
      type="text"
      label="Sort By:"
      @input="findSort"
      style="width:15%"
      class="float-right q-mx-lg"
    >
      <template v-if="clearData" v-slot:append>
        <q-icon name="cancel" @click.stop="clearData = null" class="cursor-pointer" />
      </template>
    </q-select>

    <div class="container">
      <div class="q-pa-md row justify-center items-start q-gutter-md">
        <Item
          style="margin: 10px"
          v-for="item in items"
          v-bind:key="item.id"
          :artist="item.artist"
          :title="item.title"
          :id="item.id"
          :description="item.description"
          :price="item.price"
          :photo="item.photo"
          :item="item"
        />
      </div>
    </div>
  </q-layout>
</template>

<script>
import Item from "../components/Item.vue";

var ws = new WebSocket("ws://localhost:8000/ws/chat");

export default {
  data() {
    return {
      clearData: null,
      items: null,
      text: null,
      sortBy: null,
      options: [
        "Lowest Price",
        "Highest Price",
        "Latest Release Date",
        "Oldest Release Date"
      ],
      username: this.$store.state.currentUser.username
    };
  },

  methods: {
    getItems() {
      this.$axios
        .get("api/items/")
        .then(response => {
          const data = response.data;
          this.items = [];
          Object.keys(data).forEach(key => {
            if (data[key].inventory_count > 0) {
              this.items[key] = data[key];
            }
            this.items[key];
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
    },
    findSort: function(event) {
      console.log(this.sortBy);
      if (this.sortBy == "Lowest Price") {
        this.onLowestPriceClick();
      } else if (this.sortBy == "Highest Price") {
        this.onHighestPriceClick();
      } else if (this.sortBy == "Latest Release Date") {
        this.onLatestClick();
      } else {
        this.onOldestClick();
      }
    },
    onLowestPriceClick() {
      this.sortBy = "Lowest Price";
      this.items.sort(function(x, y) {
        if (x.price < y.price) {
          return -1;
        }
        if (x.price > y.price) {
          return 1;
        }
        return 0;
      });
      this.items.forEach(item => {
        console.log(item.price);
      });
    },
    onHighestPriceClick() {
      this.items.sort(function(x, y) {
        if (x.price < y.price) {
          return 1;
        }
        if (x.price > y.price) {
          return -1;
        }
        return 0;
      });
      this.items.forEach(item => {
        console.log(item.price);
      });
    },
    onLatestClick() {
      this.items.sort(function(x, y) {
        if (x.release_year < y.release_year) {
          return 1;
        }
        if (x.release_year > y.release_year) {
          return -1;
        }
        return 0;
      });
      this.items.forEach(item => {
        console.log(item.release_year);
      });
    },
    onOldestClick() {
      this.items.sort(function(x, y) {
        if (x.release_year < y.release_year) {
          return -1;
        }
        if (x.release_year > y.release_year) {
          return 1;
        }
        return 0;
      });
      this.items.forEach(item => {
        console.log(item.release_year);
      });
    },
    onSearch() {
      console.log("helllloooo");
      var searchText = this.text;
      this.$axios
        .get("/api/itemsearch/", {
          params: {
            search: searchText
          }
        })
        .then(resp => {
          console.log("search is called");
          this.items = resp.data;
          console.log(resp.data);
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
  },
  components: {
    Item
  },
  created() {
    this.getItems();
  }
};
</script>

<style scoped>
.container {
  padding: 20px;
  justify-content: center;
}
</style>
