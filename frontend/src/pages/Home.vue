<template>
  <div>
    <q-select
      rounded
      outlined
      v-model="model"
      :options="options"
      label="Search"
      maxlength="12"
      class="q-ma-md"
    >
      <!-- <template v-slot:before>
        <q-icon name="search" />
      </template> -->

      <template v-slot:append>
        <q-icon
          v-if="model !== ''"
          name="close"
          @click.stop="model = ''"
          class="cursor-pointer"
        />
        <q-icon name="search" @click.stop />
      </template>

      <template v-slot:hint>
        Field hint
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
      items: null
    };
  },
  methods: {},
  components: {
    Item
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
