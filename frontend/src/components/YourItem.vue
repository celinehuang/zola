<template>
  <q-card class="my-card">
    <q-img v-bind:src="photo" :ratio="1" height="240px" width="240px" >
      <div class="price-caption">{{ price | formatPrice }}</div>
    </q-img>

    <q-card-section>
      <div class="text-h6">Title: {{ title }}</div>
      <div class="text-subtitle2">Artist: {{ artist }}</div>
      <div class="text-subtitle2">Media Type: {{ mediatype }}</div>
      <div class="text-subtitle2">Genre: {{ genre }}</div>
      <div class="text-subtitle2">Stock: {{ inventory_count }}</div>
      <div class="text-subtitle2">Price: {{ price | formatPrice }}</div>
      <q-btn flat color="primary" label="Edit" @click="showEditItemPopup" style="float:right;margin-left: -50%;margin-bottom : 35px;white-space: normal"/>
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
    <EditItemPopup @created="msgReceived()" />
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
      expanded: false
    };
  },
  components: {
    EditItemPopup
  },
  props: ["id", "description", "price", "photo", "title", "artist", "mediatype", "genre", "inventory_count", "release_year"],
  methods: {
    showEditItemPopup() {
      this.$q.dialog({
        component: EditItemPopup,

        parent: this,

        title: this.title,
        id: this.id,
        description:this.description,
        price:this.price,
        photo: this.photo,
        artist: this.artist,
        mediatype:this.mediatype,
        genre: this.genre,
        inventory_count: this.inventory_count,
        release_year:this.release_year
      })
    },
    msgReceived() {
      console.log('here!!!!!!!!!!!!!!!!!')
    }
  },
  filters: {
    formatPrice: function(value) {
      return "$" + value.toString();
    }
  }
};
</script>

<style lang="sass" scoped>
.my-card
    width: 100%
    max-width: 400px

.price-caption
    position: absolute
    bottom: 10px
    left: 10px
    background-color: black
    border-radius: 5px
    height: auto
    width: auto
    padding: 5px
</style>

<style scoped>
.buttonformat {
    float: right;
    margin-left: -50%;
    margin-bottom : 35px;
    white-space: normal;
    top:-6px
}
</style>