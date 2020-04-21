<template>
  <div>
    <q-input
      rounded
      outlined
      v-model="text"
      label="Search"
      maxlength="12"
      class="q-pa-lg q-mx-sm q-mt-sm"
    >
      <template v-slot:append>
        <q-icon name="search" />
      </template>
    </q-input>

    <q-select
      borderless
      v-model="sortBy"
      :options="options"
      type="text"
      label="Sort By:"
      @input="findSort"
      style="width:15%"
      class="float-right q-mx-lg"
    />

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
        />
      </div>
    </div>
  </div>
</template>

<script>
import Item from "../components/Item.vue";

export default {
  data() {
    return {
      items: null,
      text: null,
      sortBy: null,
      options: [
        "Lowest Price",
        "Highest Price",
        "Latest Release Date",
        "Oldest Release Date"
      ]
    };
  },
  components: {
    Item
  },
  methods: {
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
    }
  },
  created() {
    this.$axios
      .get("api/items/")
      .then(response => {
        this.items = response.data;
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
.container {
  padding: 20px;
  justify-content: center;
}
</style>
