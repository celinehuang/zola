<template>
  <q-layout>
    <q-page-container>
      <q-page class="q-mx-xl q-mb-md q-mt-md">
        <q-toolbar>
          <q-toolbar-title class="text-bold q-px-lg q-pt-lg">
            Change Your Password
          </q-toolbar-title>
        </q-toolbar>
        <q-form @submit="changePassword" class="q-gutter-lg q-ma-xl input">
          <q-input
            label="New Password"
            v-model="new_pwd"
            filled
            :type="isPwd1 ? 'password' : 'text'"
            :rules="[val => !!val || 'Field is required']"
          >
            <template v-slot:append>
              <q-icon
                :name="isPwd1 ? 'visibility_off' : 'visibility'"
                class="cursor-pointer"
                @click="isPwd1 = !isPwd1"
              />
            </template>
          </q-input>
          <q-input
            label="Confirm Password"
            v-model="confirm_pwd"
            filled
            :type="isPwd2 ? 'password' : 'text'"
            :rules="[
              val =>
                (val !== null && val !== '') || 'Please confirm your password',
              val => val === new_pwd || 'Passwords do not match'
            ]"
          >
            <template v-slot:append>
              <q-icon
                :name="isPwd2 ? 'visibility_off' : 'visibility'"
                class="cursor-pointer"
                @click="isPwd2 = !isPwd2"
              />
            </template>
          </q-input>
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
  name: "ChangePassword",

  components: {},

  data() {
    return {
      isPwd1: true,
      isPwd2: true,
      new_pwd: "",
      confirm_pwd: "",
      username: this.$store.state.currentUser.username,
      name: this.$store.state.currentUser.name,
      token: this.$store.state.token
    };
  },
  methods: {
    changePassword() {
      var token = this.$store.state.token;
      var new_password1 = this.new_pwd;
      var new_password2 = this.confirm_pwd;
      var body = { new_password1, new_password2 };
      this.$axios
        .post("/api/rest-auth/password/change/", body, {
          headers: {
            Authorization: `Token ${token}`
          }
        })
        .then(resp => {
          this.$q.notify({
            color: "green-4",
            position: "top",
            textColor: "white",
            icon: "cloud_done",
            message: "Successfully Changed Password"
          });
          this.$router.push({ path: "/home" });
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
.input {
  width: 700px;
}
</style>
