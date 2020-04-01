<template>
  <q-layout>
    <q-page-container>
      <q-toolbar style="background-color: #445c3c">
        <q-toolbar-title class="login-banner q-pa-md">ZOLA</q-toolbar-title>
      </q-toolbar>

      <q-page class="flex column flex-center login_page">
        <div class="q-gutter-y-md" style="min-width: 400px">
          <q-card>
            <q-tabs
              v-model="tab"
              dense
              class="text-grey"
              active-color="primary"
              indicator-color="primary"
              align="justify"
              narrow-indicator
            >
              <q-tab name="login" label="Log In" />
              <q-tab name="signup" label="Sign Up" />
            </q-tabs>

            <q-separator />

            <q-tab-panels v-model="tab" animated>
              <q-tab-panel name="login">
                <q-form @submit="onLogIn" class="q-gutter-md">
                  <q-input
                    filled
                    v-model="username"
                    label="Username"
                    hint="Enter your username"
                    lazy-rules
                    :rules="[
                      val =>
                        (val && val.length > 0) || 'Please enter your username'
                    ]"
                  />

                  <q-input
                    filled
                    v-model="password"
                    label="Password"
                    type="password"
                    hint="Enter your password"
                    lazy-rules
                    :rules="[
                      val =>
                        (val !== null && val !== '') ||
                        'Please enter your password'
                    ]"
                  />

                  <div>
                    <q-btn
                      label="Log In"
                      type="submit"
                      style="background:#cad5db;"
                    />
                  </div>
                </q-form>
              </q-tab-panel>

              <q-tab-panel name="signup">
                <q-form @submit="onSignUp" class="q-gutter-md">
                  <q-input
                    filled
                    v-model="username"
                    label="Username"
                    hint="Enter your username"
                    lazy-rules
                    :rules="[
                      val =>
                        (val && val.length > 0) || 'Please enter your username'
                    ]"
                  />
                  <q-input
                    filled
                    v-model="email"
                    label="Email"
                    hint="Enter your email"
                    lazy-rules
                    :rules="[
                      val =>
                        (val && val.length > 0) || 'Please enter your email'
                    ]"
                  />
                  <q-input
                    filled
                    v-model="name"
                    label="Name"
                    hint="Enter your name"
                    lazy-rules
                    :rules="[
                      val => (val && val.length > 0) || 'Please enter your name'
                    ]"
                  />
                  <q-input
                    filled
                    v-model="address"
                    label="Address"
                    hint="Enter your address"
                    lazy-rules
                    :rules="[
                      val =>
                        (val && val.length > 0) || 'Please enter your address'
                    ]"
                  />
                  <q-input
                    filled
                    v-model="password"
                    label="Password"
                    type="password"
                    hint="Enter your password"
                    lazy-rules
                    :rules="[
                      val =>
                        (val !== null && val !== '') ||
                        'Please enter your password'
                    ]"
                  />

                  <q-input
                    filled
                    v-model="confirm_password"
                    label="Confirm Password"
                    type="password"
                    hint="Confirm your password"
                    lazy-rules
                    :rules="[
                      val =>
                        (val !== null && val !== '') ||
                        'Please confirm your password',
                      val => val === password || 'Passwords do not match'
                    ]"
                  />

                  <div>
                    <q-btn
                      label="Sign Up"
                      type="submit"
                      style="background:#cad5db;"
                    />
                  </div>
                </q-form>
              </q-tab-panel>
            </q-tab-panels>
          </q-card>
        </div>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: "LoginPage",
  data() {
    return {
      username: null,
      email: null,
      name: null,
      address: null,
      password: null,
      confirm_password: null,
      tab: "login"
    };
  },
  methods: {
    onLogIn() {
      let username = this.username;
      let password = this.password;
      this.$store
        .dispatch("login", { username, password })
        .then(() => {
          this.$q.notify({
            color: "green-4",
            position: "top",
            textColor: "white",
            icon: "cloud_done",
            message: "Logged in successfully"
          });
          this.$router.push({ path: "/home" });
        })
        .catch(_err => {
          this.$q.notify({
            color: "red-4",
            position: "top",
            textColor: "white",
            icon: "error",
            message: "Wrong email or password"
          });
        });
    },
    onSignUp() {
      let username = this.username;
      let email = this.email;
      let name = this.name;
      let address = this.address;
      let password = this.password;
      let confirm_password = this.confirm_password;
      this.$store
        .dispatch("register", {
          username,
          email,
          name,
          address,
          password,
          confirm_password
        })
        .then(() => {
          this.$q.notify({
            color: "green-4",
            position: "top",
            textColor: "white",
            icon: "cloud_done",
            message: "Registered successfully"
          });
          this.$router.push({ path: "/home" });
        })
        .catch(_err => {
          console.log(_err);
          this.$q.notify({
            color: "red-4",
            position: "top",
            textColor: "white",
            icon: "error",
            message: "Sign Up Error"
          });
        });
    }
  }
};
</script>

<style lang="scss" scoped>
.login-banner {
  background-color: #445c3c;
  color: white;
  font-size: 25px;
  font-weight: bold;
  letter-spacing: 0.5rem;
  padding-left: 2%;
}
</style>
