<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated class="bg-cyan-8">
      <q-toolbar style="background-color: #445c3c">
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title style="font-size: 25px; font-weight: bold;">Marketplace</q-toolbar-title>

        <div>Quasar v{{ $q.version }}</div>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered content-class="bg-grey-1">
      <!-- <q-list> -->
      <q-scroll-area style="height: calc(100% - 150px); margin-top: 150px; ">
        <q-list padding>
          <q-separator />
          <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="inbox" />
            </q-item-section>

            <q-item-section>Edit Profile</q-item-section>
          </q-item>

          <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="star" />
            </q-item-section>

            <q-item-section>Order History</q-item-section>
          </q-item>
          <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="send" />
            </q-item-section>

            <q-item-section>My Listings</q-item-section>
          </q-item>

          <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="drafts" />
            </q-item-section>

            <q-item-section>Messages</q-item-section>
          </q-item>
        </q-list>
      </q-scroll-area>

      <!-- <q-img
          class="absolute-top"
          src="https://cdn.quasar.dev/img/material.png"
          style="height: 150px"
      >-->
      <div class="absolute-top" style="background-color:#fcf9f2; height: 158px; padding: 25px;">
        <q-avatar size="56px" class="q-mb-sm">
          <img src="https://cdn.quasar.dev/img/boy-avatar.png" />
        </q-avatar>
        <div class="text-weight-bold">Razvan Stoenescu</div>
        <div>@rstoenescu</div>
      </div>
      <!-- </q-img> -->
      <!-- </q-list> -->
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import EssentialLink from "components/EssentialLink";

export default {
  name: "MainLayout",

  components: {},

  data() {
    return {
      leftDrawerOpen: false
    };
  }
};
</script>
