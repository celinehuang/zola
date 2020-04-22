<template>
  <q-page>
    <div class="container">
      <div
        class="q-pa-md col-12 col-md-8 justify-center items-start q-gutter-md"
      >
        <q-card-section v-for="(message, index) in messages" :key="index">
          <span
            class="text-bold"
            style="color: #445c3c"
            v-if="username == message.user"
            >{{ message.user }}</span
          >
          <span class="text-bold" v-if="username != message.user">{{
            message.user
          }}</span>
          <div class="q-ma-sm">{{ message.content }}</div>
          <q-separator />
        </q-card-section>
      </div>
    </div>
    <q-form @submit="send" class="q-gutter-lg q-pa-xl">
      <q-input filled v-model="currmessage" />
      <div style="text-align:center;">
        <q-btn label="SEND MESSAGE" type="submit" style="background:#cad5db;" />
      </div>
    </q-form>
  </q-page>
</template>

<script>
var ws = new WebSocket("ws://localhost:8000/ws/chat");

export default {
  name: "AllMessages",
  components: {},
  data() {
    return {
      currmessage: "",
      message: "",
      messages: [],
      username: this.$store.state.currentUser.username,
      profile_pic: this.$store.state.currentUser.profile_pic
    };
  },
  created() {
    this.initWS();
  },
  methods: {
    send() {
      var today = new Date();
      var date_today =
        today.getFullYear() +
        "-" +
        (today.getMonth() + 1) +
        "-" +
        today.getDate();
      var msg = {
        user: this.username,
        content: this.currmessage,
        date: date_today,
        command: "new_message"
      };
      ws.send(JSON.stringify({ ...msg }));
    },

    initWS() {
      ws.onmessage = e => {
        const parsedData = JSON.parse(e.data);
        console.log(parsedData);
        onMessage(parsedData.messages, parsedData.command);
      };

      ws.onopen = () => {
        sendMessage({ command: "fetch_messages", username: this.username });
      };

      ws.onerror = e => {
        console.log(e.message);
      };

      const onMessage = (message, command) => {
        console.log("in onmessage");
        if (command == "get_all_messages") {
          this.messages = message.reverse();
        }

        if (command == "new_message") {
          var m = this.messages;
          this.messages = [...m, message];
        }
      };

      const sendMessage = messageObject => {
        console.log("in sendmessage", messageObject);

        try {
          ws.send(JSON.stringify({ ...messageObject }));
        } catch (err) {
          console.log(err.message);
        }
      };
    }
  }
};
</script>

<style scoped>
.remove-border {
  box-shadow: none !important;
}
</style>
