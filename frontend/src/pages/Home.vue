<template>
  <q-layout>
    <form @submit.prevent="onSearch" class="q-pa-md">
      <q-input
        rounded
        outlined
        v-model="text"
        label="Search"
        class="q-pa-lg q-mx-sm q-mt-sm"
      >
        <template v-slot:append>
          <q-btn name="cancel" @click="clearSearch" class="cursor-pointer" />
        </template>
        <template v-slot:append>
          <q-icon name="search" />
        </template>
      </q-input>
    </form>

    <q-select
      borderless
      clearable
      v-model="sortBy"
      :options="options"
      type="text"
      label="Sort By:"
      @input="findSort"
      style="width:15%"
      class="float-right q-mx-lg"
    >
      <template v-if="clearData" v-slot:append>
        <q-icon
          name="cancel"
          @click.stop="clearData = null"
          class="cursor-pointer"
        />
      </template>
    </q-select>

    <div class="container">
      <div class="q-pa-md row justify-center items-start q-gutter-md">
        <Item
          style="margin: 10px"
          v-for="item in items"
          v-bind:key="item.id"
          :artist="item.artist"
          :title="item.title"
          :id="item.id"
          :description="item.description"
          :price="item.price"
          :photo="item.photo"
        />
      </div>
    </div>
    <div>
      <q-btn flat color="primary" icon="add_shopping_cart" @click="test()" />
      <q-btn flat color="secondary" icon="add_shopping_cart" @click="test2()" />
    </div>
</template>

<script>
import Item from "../components/Item.vue";

var ws = new WebSocket("ws://localhost:8000/ws/chat");

export default {
  data() {
    return {
      clearData: null,
      // clearSearch: null,
      items: null,
      text: null,
      sortBy: null,
      options: [
        "Lowest Price",
        "Highest Price",
        "Latest Release Date",
        "Oldest Release Date"
      ],
      message: "",
      messages: ["wassssup"],
      username: this.$store.state.currentUser.username
    };
  },
  components: {
    Item
  },
  methods: {
    test() {
      var msg = {
        id: "69",
        user: "jacekd908",
        content: "plswork",
        date: "2020-04-19 22:23:23.549675+00:00",
        command: "new_message"
      };
      ws.send(JSON.stringify({ ...msg }));
    },
    test2() {
      console.log("messages", this.messages);
    },
    initWS() {
      var self = this;
      ws.onmessage = e => {
        const parsedData = JSON.parse(e.data);
        console.log(parsedData);
        onMessage(parsedData.messages, parsedData.command);
      };

      ws.onopen = () => {
        console.log("WEBSOCKET OPEN BOIIII");
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
          //lol
          this.messages = [...m, message];
        }
      };

      const sendMessage = messageObject => {
        console.log("in sendmessage");
        try {
          ws.send(JSON.stringify({ ...messageObject }));
        } catch (err) {
          console.log(err.message);
        }
      };

      const messageChangeHandler = event => {
        this.message = event.target.value;
      };

      const sendMessageHandler = (e, message) => {
        const messageObject = {
          command: "new_message",
          username: username,
          content: message
        };
        this.sendMessage(messageObject);
        this.message = "";
      };

      const renderMessages = () => {
        return this.messages.map(message => {
          return `<div key={message.id}>
              <h2> {message.user} </h2>
              <h2> {message.created_table} </h2>
              <p> {message.content} </p>
            </div>`;
        });
      };

      function render() {
        const messages = this.messages;
        return `<div>
            <div >
              <h1> chatting as {username}</h1>
              <h3> display only the recent 50 messages </h3>

              {messages && this.renderMessages()}
            </div>
            <div>
              <form 
                onSubmit={(e) => this.sendMessageHandler(e, this.message)}
              >
                <input 
                  type="text" onChange={this.messageChangeHandler} value={this.message} placeholder="Type sumn" required />
                  <button type="submit" value="Submit">
                    Submit
                  </button>
              </form>
            </div>
          </div>`;
      }

      sendMessage("hellllo???????");
    },
    findSort: function(event) {
      console.log(this.sortBy);
      if (this.sortBy == "Lowest Price") {
        this.onLowestPriceClick();
      } else if (this.sortBy == "Highest Price") {
        this.onHighestPriceClick();
      } else if (this.sortBy == "Latest Release Date") {
        this.onLatestClick();
      } else {
        this.onOldestClick();
      }
    },
    onLowestPriceClick() {
      this.sortBy = "Lowest Price";
      this.items.sort(function(x, y) {
        if (x.price < y.price) {
          return -1;
        }
        if (x.price > y.price) {
          return 1;
        }
        return 0;
      });
      this.items.forEach(item => {
        console.log(item.price);
      });
    },
    onHighestPriceClick() {
      this.items.sort(function(x, y) {
        if (x.price < y.price) {
          return 1;
        }
        if (x.price > y.price) {
          return -1;
        }
        return 0;
      });
      this.items.forEach(item => {
        console.log(item.price);
      });
    },
    onLatestClick() {
      this.items.sort(function(x, y) {
        if (x.release_year < y.release_year) {
          return 1;
        }
        if (x.release_year > y.release_year) {
          return -1;
        }
        return 0;
      });
      this.items.forEach(item => {
        console.log(item.release_year);
      });
    },
    onOldestClick() {
      this.items.sort(function(x, y) {
        if (x.release_year < y.release_year) {
          return -1;
        }
        if (x.release_year > y.release_year) {
          return 1;
        }
        return 0;
      });
      this.items.forEach(item => {
        console.log(item.release_year);
      });
    },
    clearSearch() {
      console.log("yes it worked");
      this.$axios
        .get("/api/itemsearch/")
        .then(resp => {
          console.log("clearsearch is called");
          this.items = resp.data;
          console.log(resp.data);
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
    },
    onSearch() {
      console.log("helllloooo");
      var searchText = this.text;
      this.$axios
        .get("/api/itemsearch/", {
          params: {
            search: searchText
          }
        })
        .then(resp => {
          console.log("search is called");
          this.items = resp.data;
          console.log(resp.data);
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
  },
  created() {
    this.$axios
      .get("api/items/")
      .then(response => {
        this.items = response.data;
      })
      .catch(() => {
        this.$q.notify({
          color: "negative",
          position: "top",
          message: "Loading failed",
          icon: "report_problem"
        });
      });

    this.initWS();
  }
};
</script>

<style scoped>
.container {
  padding: 20px;
  justify-content: center;
}
</style>
