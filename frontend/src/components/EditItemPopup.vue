<template>
  <q-card>
    <q-card-section class="row ">
      <div class="text-h6">Edit item</div>
      <q-space />
      <q-btn icon="close" flat round dense v-close-popup />
    </q-card-section>
    <q-card-section>
      <q-form class="q-gutter-sm" @submit="updateItem">
        <q-input filled v-model="title_" label="Title" />
        <q-input filled v-model="artist_" label="Artist" />
        <q-select
          filled
          v-model="genre_"
          :options="genreOptions"
          label="Genre"
        />
        <q-input filled v-model="description_" label="Description" />
        <q-select
          filled
          v-model="mediatype_"
          :options="mediatypeOptions"
          label="Media Type"
        />
        <q-input
          filled
          stack-label
          v-model="release_year_"
          type="date"
          label="Release Date"
        />
        <q-input
          filled
          v-model="price_"
          mask="#.##"
          fill-mask="0"
          reverse-fill-mask
          label="Price"
        />
        <q-input
          filled
          v-model="inventory_count_"
          type="number"
          label="Inventory"
        />
        <q-input
          filled
          stack-label
          v-model="photo_"
          type="file"
          @change="onFileChanged"
          label="Cover Art"
        />
        <q-btn
          class="q-ma-sm"
          color="primary"
          type="submit"
          label="Update Item"
        />
      </q-form>
    </q-card-section>
  </q-card>
</template>

<script>
export default {
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
  name: "EditItemPopup",
  data: function() {
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
      id_: this.id,
      description_: this.description,
      price_: this.price,
      photo_: this.photo,
      title_: this.title,
      artist_: this.artist,
      mediatype_: this.mediatype,
      genre_: this.genre,
      inventory_count_: this.inventory_count,
      release_year_: this.release_year,
      pic_changed: false
    };
  },

  methods: {
    updateItem: function() {
      const id = this.id;
      const formData = new FormData();
      if (this.pic_changed == true) {
        console.log("here", this.newPic);
        formData.append("photo", this.newPic);
      }
      formData.append("artist", this.artist_);
      formData.append("title", this.title_);
      formData.append("genre", this.genre_);
      formData.append("description", this.description_);
      formData.append("mediatype", this.mediatype_);
      formData.append("release_year", this.release_year_);
      formData.append("price", this.price_);
      formData.append("inventory_count", this.inventory_count_);

      this.$axios
        .patch("/api/items/" + this.id + "/", formData, {
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
            message: "Successfully Updated Item"
          });

          this.$emit("item-updated");
        })
        .catch(err => {
          this.$q.notify({
            color: "red-4",
            position: "top",
            textColor: "white",
            icon: "error",
            message: "Something went wrong, please try again."
          });
        });
    },
    onFileChanged: function(event) {
      this.newPic = event.target.files[0];
      this.oldPic = URL.createObjectURL(event.target.files[0]);
      this.pic_changed = true;
    }
  }
};
</script>
<style lang="scss" scoped></style>
