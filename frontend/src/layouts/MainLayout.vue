<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar style="background-color: primary">
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>
          <q-btn flat class="home-btn" to="/home">ZOLA</q-btn>
        </q-toolbar-title>

        <div class="q-pa-md">
          <q-btn flat @click="logout" style="letter-spacing:0.15rem"
            >LOGOUT</q-btn
          >

          <ShoppingCart />
        </div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-2"
    >
      <q-scroll-area style="height: calc(100% - 150px); margin-top: 150px; ">
        <q-list padding>
          <q-separator />
          <q-item clickable v-ripple to="/edit-profile">
            <q-item-section avatar>
              <q-icon name="edit" />
            </q-item-section>
            <q-item-section>Edit Profile</q-item-section>
          </q-item>

          <q-item clickable v-ripple to="/order-history">
            <q-item-section avatar>
              <q-icon name="history" />
            </q-item-section>
            <q-item-section>Order History</q-item-section>
          </q-item>

          <q-item clickable v-ripple to="/my-listings">
            <q-item-section avatar>
              <q-icon name="list" />
            </q-item-section>
            <q-item-section>My Listings</q-item-section>
          </q-item>

          <q-item clickable v-ripple to="/messages">
            <q-item-section avatar>
              <q-icon name="chat" />
            </q-item-section>
            <q-item-section>Chat Room</q-item-section>
          </q-item>

          <q-item clickable v-ripple to="/change-password">
            <q-item-section avatar>
              <q-icon name="lock_open" />
            </q-item-section>
            <q-item-section>Change Password</q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>

      <div
        class="absolute-top"
        style="background-color:#fcf9f2; height: 158px; padding: 25px;"
      >
        <!-- Show generic profile picture if user has no profile picture -->
        <q-avatar
          v-if="profile_pic === null"
          size="70px"
          class="q-mb-sm profile-picture"
        >
          <img src="../assets/avatar-person.svg" />
        </q-avatar>
        <!-- Show user's profile picture otherwise -->
        <q-avatar v-else size="70px" class="q-mb-sm profile-picture">
          <img v-bind:src="profile_pic" />
        </q-avatar>
        <div class="text-weight-bold">{{ name }}</div>
        <div>@{{ username }}</div>
      </div>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import EssentialLink from "components/EssentialLink";
import ShoppingCart from "../components/ShoppingCart.vue";

export default {
  name: "MainLayout",
  data() {
    return {
      leftDrawerOpen: false,
      username: this.$store.state.currentUser.username,
      name: this.$store.state.currentUser.name,
      profile_pic: this.$store.state.currentUser.profile_pic
    };
  },
  components: {
    ShoppingCart
  },
  computed: {
    inCart() {
      return this.$store.getters.inCart;
    }
  },
  methods: {
    logout: function() {
      this.$store.dispatch("logout").then(this.$router.push({ path: "login" }));
    }
  }
};
</script>

<style scoped>
.q-item.q-router-link--active,
.q-item--active {
  color: #445c3c;
}
.home-btn {
  font-size: 25px;
  font-weight: bold;
  letter-spacing: 0.5rem;
}
.cart {
  display: inline-block;
}
#default-profile-picture {
  background-image: url("../assets/avatar-person.svg");
}
</style>
