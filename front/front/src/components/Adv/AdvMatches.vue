<template>
  <div :id="compId"></div>
</template>

<script>
import postscribe from "postscribe";
var ready = require("document-ready");
export default {
  name: "AdvMatches",
  data() {
    let randomID = Math.random().toString(36).substring(7);
    return {
      compId: window.performance.now() + "-" + randomID,
    };
  },
  props: {
    script: {
      type: String,
      default: null,
    },
  },
  mounted() {
    var vm = this;
    ready(function () {
      let addEl = new Promise((resolve, reject) => {
        postscribe(`#${vm.compId}`, `${vm.script}`, {
          done: function (x) {
            resolve(x);
          },
        });
        resolve();
      });
      addEl.then(function (result) {
        //do nothing
      });
    });
  },
};
</script>
