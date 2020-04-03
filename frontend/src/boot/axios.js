import Vue from "vue";
import axios from "axios";

var config = require("../config");

// Axios config
const frontendUrl = config.build.host + ":" + config.build.port;
const backendUrl = config.build.backendHost + ":" + config.build.backendPort;

Vue.prototype.$axios = axios.create({
  baseURL: backendUrl,
  headers: {
    "Content-Type": "application/json"
  }
});
