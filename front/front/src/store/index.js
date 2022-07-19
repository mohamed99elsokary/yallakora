import { createStore } from "vuex";
import matchesModule from "./matches/index";
import postsModule from "./blog/index";
import transferModule from "./transfer/index";
import predictModule from "./predicts/index";
import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const store = new Vuex.Store({
  modules: {
    matchesModule,
    postsModule,
    transferModule,
    predictModule,
  },
});

export default store;
