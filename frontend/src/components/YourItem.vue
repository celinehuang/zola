<template>
  <q-card class="my-card">
    <q-img v-bind:src="photo" :ratio="1" height="240px" width="240px">
      <div class="price-caption">{{ price | formatPrice }}</div>
    </q-img>

    <q-card-section class="">
      <div class="text-h6">{{ title }}</div>
      <div class="text-subtitle2">Artist: {{ artist }}</div>
      <div class="text-subtitle2">Media Type: {{ mediatype }}</div>
      <div class="text-subtitle2">Genre: {{ genre }}</div>
      <div class="text-subtitle2">Stock: {{ inventory_count }}</div>
      <div class="text-subtitle2">Price: {{ price | formatPrice }}</div>
      <q-btn
        flat
        color="primary"
        label="Edit"
        @click="showEditItemPopup = true"
        class="float-right"
      />
    </q-card-section>

    <q-card-actions>
      <q-space />
      <q-btn
        color="primary"
        round
        flat
        dense
        :icon="expanded ? 'keyboard_arrow_up' : 'keyboard_arrow_down'"
        @click="expanded = !expanded"
      />
    </q-card-actions>

    <q-dialog v-model="showEditItemPopup">
      <EditItemPopup
        @item-updated="notifyParent"
        :id="this.id"
        :title="this.title"
        :artist="this.artist"
        :genre="this.genre"
        :description="this.description"
        :mediatype="this.mediatype"
        :release_year="this.release_year"
        :price="this.price"
        :inventory_count="this.inventory_count"
        :photo="this.photo"
      />
    </q-dialog>

    <q-slide-transition>
      <div v-show="expanded">
        <q-separator />
        <q-card-section class="text-subitle2">{{ description }}</q-card-section>
      </div>
    </q-slide-transition>
  </q-card>
</template>

<script>
import EditItemPopup from "../components/EditItemPopup.vue";

export default {
  name: "YourItem",

  data() {
    return {
      showEditItemPopup: false,
      expanded: false
    };
  },
  components: {
    EditItemPopup
  },
  props: [
    "id",
    "description",
    "price",
    "photo",
    "title",
    "artist",
    "mediatype",
    "genre",
    "inventory_count",
    "release_year"
  ],
  methods: {
    notifyParent() {
      this.showEditItemPopup = false;

      this.$emit("item-updated");
    }
  },
  filters: {
    formatPrice: function(value) {
      return "$" + value.toString();
    }
  }
};
</script>

<style scoped>
.my-card {
  width: 240px;
  height: 450px;
  overflow: scroll;
}
.price-caption {
  position: absolute;
  bottom: 10px;
  left: 10px;
  background-color: black;
  border-radius: 5px;
  height: auto;
  width: auto;
  padding: 5px;
}
</style>
