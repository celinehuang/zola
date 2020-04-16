<template>
  <q-dialog ref="dialog" @hide="onDialogHide">
    <q-card class="item-edit">
      <q-card-section class="row items-center">
        <div class="text-h6">Edit item</div>
        <q-space />
        <q-btn icon="close" flat round dense v-close-popup />
      </q-card-section>
      <q-card-section>
        <q-form class="q-gutter-sm" @submit="addItem">
          <q-input filled v-model="title_" label="Title" />
          <q-input filled v-model="artist_" label="Artist" />
          <q-input filled v-model="genre_" label="Genre" />
          <q-input filled v-model="description_" label="Description" />
          <q-input filled v-model="mediatype_" label="Media Type" />
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
  </q-dialog>
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
    // following method is REQUIRED
    show() {
      this.$refs.dialog.show();
    },

    // following method is REQUIRED
    hide() {
      this.$refs.dialog.hide();
    },

    addItem: function() {
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

      this.hide();
      this.$emit("created");
    },

    test() {
      console.log("here 2222222");
    },

    onDialogHide() {
      this.$emit("hide");
    },

    onOKClick() {
      this.$emit("ok");
      // or with payload: this.$emit('ok', { ... })

      // then hiding dialog
      this.hide();
    },

    onCancelClick() {
      this.hide();
    },

    onFileChanged: function(event) {
      //   console.log(event.target.files[0].type);
      this.newPic = event.target.files[0];
      this.oldPic = URL.createObjectURL(event.target.files[0]);
      this.pic_changed = true;
    }
  }
};
</script>
<style lang="scss" scoped>
.item-edit {
  min-width: 500px;
}
</style>
