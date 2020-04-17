<template>
  <q-page>
    <q-card class="remove-border">
      <q-card-section @click="msgPage">
        <q-avatar size="50px" class="q-mx-sm">
          <img src="../assets/avatar-person.svg" />
        </q-avatar>
        <span>username</span>
        <div class="q-ma-sm">message preview</div>
        <q-separator />
      </q-card-section>
      <q-card-section>
        <q-avatar size="50px" class="q-mx-sm">
          <img src="../assets/avatar-person.svg" />
        </q-avatar>
        <span>username</span>
        <div class="q-ma-sm">message preview</div>
        <q-separator />
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script>
export default {
  name: "AllMessages",
  components: {},
  data() {
    return {};
  },
  methods: {
    msgPage() {}
  }
};
</script>

<style scoped>
.remove-border {
  box-shadow: none !important;
}
</style>
      
    
 <!-- v-for="msg in curr_users_msgs" v-bind:key="msg.id" -->
        <!-- <YourMessage
          :id="item.id"
          :description="item.description"
          :price="item.price"
          :photo="item.photo"
          :title="item.title"
          :artist="item.artist"
          :genre="item.genre"
          :mediatype="item.mediatype"
          :inventory_count="item.inventory_count"
          :release_year="item.release_year"/>-->