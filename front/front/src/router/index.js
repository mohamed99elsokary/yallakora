import Vue from "vue";
import VueRouter from "vue-router";

import Home from "../views/Home.vue";
import News from "../views/News.vue";
import Transfers from "../views/Transfers.vue";
import Results from "../views/Results.vue";
import Expectations from "../views/Expectations.vue";
import Policy from "../views/Policy.vue";
import Advertise from "../views/Advertise.vue";
import Post from "../views/Post.vue";
import Live from "../views/Live.vue";
// import VueMeta from "@/../node_modules/vue-meta/dist/vue-meta.esm";
// import VueMeta from "vue-meta";
import VueMeta from 'vue-meta'


Vue.use(VueMeta);
Vue.use(VueRouter);

// const routes = [
//   {
//     path: "/",
//     name: "home",
//     component: () => import("../views/Home.vue"),
//     meta: {
//       title: "الرئيسية",
//     },
//   },
//   {
//     path: "/News",
//     name: "News",
//     component: () => import("../views/News.vue"),
//     meta: {
//       title: "الأخبار",
//     },
//   },
//   {
//     path: "/Transfers",
//     name: "Transfers",
//     component: () => import("../views/Transfers.vue"),
//     meta: {
//       title: "الانتقالات",
//     },
//   },
//   {
//     path: "/Results",
//     name: "Results",
//     component: () => import("../views/Results.vue"),
//     meta: {
//       title: "المباريات",
//     },
//   },
//   {
//     path: "/Expectations",
//     name: "Expectations",
//     component: () => import("../views/Expectations.vue"),
//     meta: {
//       title: "التوقعات",
//     },
//   },
//   ,
//   {
//     path: "/policy",
//     name: "policy",
//     component: () => import("../views/Policy.vue"),
//     meta: {
//       title: "سياسة الخصوصية",
//     },
//   },
//   {
//     path: "/Advertise",
//     name: "Advertise",
//     component: () => import("../views/Advertise.vue"),
//     meta: {
//       title: "للإعلان معنا",
//     },
//   },
//   {
//     path: "/Live/:id",
//     name: "Live",
//     component: () => import("../views/Live.vue"),
//     meta: {
//       title: "مباشر",
//     },
//   },
//   {
//     path: "/Post/:id",
//     name: "Post",
//     component: () => import("../views/Post.vue"),
//   },
// ];
const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
    meta: {
      title: "الرئيسية",
    },
  },
  {
    path: "/News",
    name: "News",
    component: News,
    meta: {
      title: "الأخبار",
    },
  },
  {
    path: "/Transfers",
    name: "Transfers",
    component: Transfers,
    meta: {
      title: "الانتقالات",
    },
  },
  {
    path: "/Results",
    name: "Results",
    component: Results,
    meta: {
      title: "المباريات",
    },
  },
  {
    path: "/Expectations",
    name: "Expectations",
    component: Expectations,
    meta: {
      title: "التوقعات",
    },
  },
  ,
  {
    path: "/policy",
    name: "policy",
    component: Policy,
    meta: {
      title: "سياسة الخصوصية",
    },
  },
  {
    path: "/Advertise",
    name: "Advertise",
    component: Advertise,
    meta: {
      title: "للإعلان معنا",
    },
  },
  {
    path: "/Live/:id",
    name: "Live",
    component: Live,
    meta: {
      title: "مباشر",
    },
  },
  {
    path: "/Post/:id",
    name: "Post",
    component: Post,
  },
];

const router = new VueRouter({
  // mode: "history",
  // base: process.env.BASE_URL,
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else {
      return { x: 0, y: 0 };
    }
  },
});

router.beforeEach((to, from, next) => {
  document.title = to.meta.title
    ? `${to.meta.title} | يلا شوت الكورة`
    : "يلا شوت الكورة";

  next();
});

export default router;
