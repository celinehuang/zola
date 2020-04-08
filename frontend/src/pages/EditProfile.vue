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
          <q-avatar size="150px">
            <!-- must render current user profile pic -->
            <!-- <img src="~assets/avatar-person.svg" /> -->
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
          <q-input filled v-model="addr" label="Address" />
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
      //   file: null,
      //   encoded_file: "",
      username: this.$store.state.currentUser.username,
      name: this.$store.state.currentUser.name,
      addr: this.$store.state.currentUser.shipping_addr,
      email: this.$store.state.currentUser.email,
      profile_pic: null,
      //   id doesn't work
      id: this.$store.state.currentUser.id
    };
  },
  created() {
    console.log("getting profile pics called");
    this.$axios
      .get(
        "http://localhost:8000/media/profilepics/Screen_Shot_2020-03-23_at_12.58.21_PM.png"
      )
      .then(response => {
        this.profile_pic = response.data;
      });
  },
  methods: {
    onFileChanged: function(event) {
      this.file = event.target.files[0];
      this.name = name;
      this.addr = addr;
      this.email = email;
    },
    changeProfile() {
      let name = this.name;
      let email = this.email;
      let addr = this.addr;
      let pp = this.profile_pic;
      //   console.log("here" + pp);
      //   id is undefined
      //   let id = this.id;
      //   console.log(this.id);
      //   const profilePic = new FormData();
      //   formData.append("file", this.file);

      //   this.$axios.put("/api/partialupdate/" + this.id, {
      //           headers: {
      //             Authorization: `Token ${token}`
      //           }
      //         })
      //           .then(resp => {
      //             const user = resp.data;
      //             localStorage.setItem("token", token);
      //             axios.defaults.headers.common["Authorization"] = token;
      //             commit("auth_success", { token, user });
      //             resolve(resp);
      //           })
      //           .catch(err => {
      //             commit("auth_error");
      //             localStorage.removeItem("token");
      //             reject(err);
      //           });
    }
  }
};
</script>

<style scoped>
.button {
  background-color: #fce9d5;
}
</style>
