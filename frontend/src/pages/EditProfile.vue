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
            <q-btn
              class="button"
              @click="changeProfile"
              flat
              type="submit"
              label="Done"
            />
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
      encoded_file: "",
      changePicture: false
    };
  },
  methods: {
    onFileChanged: function(event) {
      this.profile_pic = URL.createObjectURL(event.target.files[0]);
      this.changePicture = true;
      this.encoded_file = this.profile_pic.encoded_file;
      //   this.name = name;
      //   this.shipping_addr = shipping_addr;
      //   this.email = email;
    },
    changeProfile() {
      const id = this.id;
      //   const newProfilePic = new FormData(this.profile_pic);
      //   newProfilePic.append("profile_pic", this.profile_pic);
      //   console.log(newProfilePic);

      const data = {
        name: this.name,
        email: this.email,
        shipping_addr: this.shipping_addr
        // profile_pic: newProfilePic
      };

      this.$axios
        .put("/api/partialupdate/" + this.id + "/", data, {
          headers: { "Content-Type": "application/json" }
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
          console.log(err.resp);
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
