<template>
  <q-layout>
    <q-page-container>
      <q-page class="q-mx-xl q-mb-md q-mt-md">
        <q-toolbar>
          <q-toolbar-title class="text-bold q-px-lg q-pt-lg">
            Edit Profile
          </q-toolbar-title>
        </q-toolbar>
        <div class="q-pa-md">
          <div class="q-py-md">Photo</div>
          <q-avatar v-if="profile_pic === null" size="150px">
            <img src="../assets/avatar-person.svg" />
          </q-avatar>
          <q-avatar v-else size="150px">
            <img v-bind:src="profile_pic" />
          </q-avatar>
        </div>

        <q-form @submit="changeProfile" class="q-gutter-md q-ma-md">
          <input type="file" @change="onFileChanged" />
          <q-input
            filled
            v-model="username"
            hint="Cannot change username"
            disable
          />
          <q-input filled v-model="name" label="Name" />
          <q-input filled v-model="email" label="Email" />
          <q-input filled v-model="shipping_addr" label="Address" />
          <div class="float-right">
            <q-btn class="button q-ma-lg" to="/home" flat label="Cancel" />
            <q-btn class="button" flat type="submit" label="Done" />
          </div>
        </q-form>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: "EditProfile",

  components: {},

  data() {
    return {
      //   leftDrawerOpen: false,
      username: this.$store.state.currentUser.username,
      name: this.$store.state.currentUser.name,
      shipping_addr: this.$store.state.currentUser.shipping_addr,
      email: this.$store.state.currentUser.email,
      profile_pic: this.$store.state.currentUser.profile_pic,
      id: this.$store.state.currentUser.id,
      newProfilePic: null
    };
  },
  methods: {
    onFileChanged: function(event) {
      //   console.log(event.target.files[0].type);
      this.newProfilePic = event.target.files[0];
      this.profile_pic = URL.createObjectURL(event.target.files[0]);
    },
    changeProfile() {
      const id = this.id;
      const formData = new FormData();
      formData.append("profile_pic", this.newProfilePic);
      formData.append("name", this.name);
      formData.append("shipping_addr", this.shipping_addr);
      formData.append("email", this.email);

      this.$axios
        .put("/api/partialupdate/" + this.id + "/", formData, {
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
            message: "Successfully Updated Profile"
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
    }
  }
};
</script>

<style scoped>
.button {
  background-color: #fce9d5;
}
</style>
