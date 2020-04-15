import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

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
    userExists: false,
    inCart: []
  },
  getters: {
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status,
    inCart: state => state.inCart
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
    },
    add_to_cart(state, id) {
      state.inCart.push(id);
    }
  },
  actions: {
    login({ commit }, user) {
      return new Promise((resolve, reject) => {
        commit("auth_request");
        AXIOS.post("/api/rest-auth/login/", {
          username: user.username,
          password: user.password
        })
          .then(resp => {
            const token = resp.data.key;
            // get user from rest-auth/user by token
            AXIOS.get("/api/rest-auth/user", {
              headers: {
                Authorization: `Token ${token}`
              }
            })
              .then(resp => {
                const user = resp.data;
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
        AXIOS.post("/api/rest-auth/registration/", {
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
    },
    addToCart({ commit }, id) {
      commit("add_to_cart", id);
    }
  },

  // enable strict mode (adds overhead!)
  // for dev mode only
  strict: process.env.DEV
});

export default Store;
