import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import Axios from "axios";

// import example from './module-example'

Vue.use(Vuex);

var config = require("../config");

// Axios config
const frontendUrl = config.build.host + ":" + config.build.port;
console.log("frontend port: " + config.build.port);
const backendUrl = config.build.backendHost + ":" + config.build.backendPort;
console.log("backend port: " + config.build.backendPort);

var AXIOS = axios.create({
  baseURL: backendUrl,
  headers: {
    "Access-Control-Allow-Origin": frontendUrl,
    "Content-Type": "application/json"
  }
});

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation
 */

const Store = new Vuex.Store({
  state: {
    status: "",
    token: localStorage.getItem("token") || "",
    currentUser: {},
    userExists: false
  },
  getters: {
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status
  },
  mutations: {
    auth_request(state) {
      state.status = "loading";
    },
    auth_success(state, authObj) {
      state.status = "success";
      state.token = authObj.token;
      state.currentUser = authObj.user;
      state.userExists = true;
    },
    auth_error(state) {
      state.status = "error";
    },
    logout(state) {
      state.status = "";
      state.token = "";
      state.currentUser = {};
      state.userExists = false;
    },
    set_user(state, user) {
      state.currentUser = user;
      state.userExists = true;
    }
  },
  actions: {
    login({ commit }, user) {
      return new Promise((resolve, reject) => {
        commit("auth_request");
        AXIOS.post("http://127.0.0.1:8000/api/rest-auth/login/", {
          username: user.username,
          password: user.password
        })
          .then(resp => {
            const token = resp.data.token;
            const user = resp.data.user;
            localStorage.setItem("token", token);

            axios.defaults.headers.common["Authorization"] = token;
            commit("auth_success", { token, user });
            resolve(resp);
          })
          .catch(err => {
            commit("auth_error");
            localStorage.removeItem("token");
            reject(err);
          });
      });
    },
    register({ commit }, user) {
      return new Promise((resolve, reject) => {
        commit("auth_request");
        var request = {
          username: user.username,
          email: user.email,
          name: user.name,
          shipping_addr: user.address,
          password1: user.password,
          password2: user.confirm_password
        };
        console.log(request);
        Axios.post("http://127.0.0.1:8000/api/rest-auth/registration/", {
          username: user.username,
          email: user.email,
          name: user.name,
          shipping_addr: user.address,
          password1: user.password,
          password2: user.confirm_password
        })
          .then(resp => {
            const token = resp.data.token;
            const user = resp.data.user;
            localStorage.setItem("token", token);

            axios.defaults.headers.common["Authorization"] = token;
            commit("auth_success", { token, user });
            resolve(resp);
          })
          .catch(err => {
            commit("auth_error", err);
            localStorage.removeItem("token");
            reject(err);
          });
      });
    },
    logout({ commit }) {
      return new Promise((resolve, reject) => {
        commit("logout");
        localStorage.removeItem("token");
        delete axios.defaults.headers.common["Authorization"];
        resolve();
      });
    }
  },
  modules: {
    // example
  },

  // enable strict mode (adds overhead!)
  // for dev mode only
  strict: process.env.DEV
});

export default Store;
