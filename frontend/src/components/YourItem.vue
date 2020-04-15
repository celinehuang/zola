<template>

  <q-card class="my-card">
    <q-img v-bind:src="photo" :ratio="1">
      <div class="price-caption">{{ price | formatPrice }}</div>
    </q-img>

    <q-card-section>
      <div class="text-h6">Title: {{ title }}<q-btn flat color="primary" label="Edit" @click="editPopUp('title')" style="float:right;margin-left: -50%;margin-bottom : 35px;white-space: normal"/></div>
      <br>
      <div class="text-subtitle2">Artist: {{ artist }}<q-btn class="buttonformat" flat color="primary" label="Edit" @click="editPopUp('artist')"/></div>
      <br>
      <div class="text-subtitle2">Media Type: {{ mediatype }}<q-btn class="buttonformat" flat color="primary" label="Edit" @click="editPopUp('mediatype')"/></div>
      <br>
      <div class="text-subtitle2">Genre: {{ genre }}<q-btn flat class="buttonformat" color="primary" label="Edit" @click="editPopUp('genre')"/></div>
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

    <q-slide-transition>
      <div v-show="expanded">
        <q-separator />
        <q-card-section class="text-subitle2">{{ description }}<q-btn flat color="primary" label="Edit" @click="editPopUp" /></q-card-section>
      </div>
    </q-slide-transition>
  </q-card>
</template>

<script>
export default {
  name: "YourItem",

  data() {
    return {
      expanded: false
    };
  },
  props: ["id", "description", "price", "photo", "title", "artist", "mediatype", "genre"],
  methods: {
    editPopUp(title) {
        var self = this
      console.log('here')
      this.$q.dialog({
              title: "Edit " + title,
              prompt: {
                model: this[title],
                type: 'text',
                label: title
              },
              cancel: true,
              color: 'secondary'
            }).then(data => {})
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