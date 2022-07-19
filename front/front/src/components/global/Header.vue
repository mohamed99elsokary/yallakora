<template>
  <header>
    <nav class="navbar navbar-expand-lg fixed-top bg-light">
      <div class="container">
        <router-link class="navbar-brand" to="/">
          <img src="../../assets/KORA1.png" alt="YALLA SHOT ALKORA" />
          <!-- <p class="logo">YALLA SHOOT AL KORA</p> -->
        </router-link>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="fas fa-bars"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link class="nav-link" exact to="/">الرئيسية</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" exact to="/News">
                الأخبار
              </router-link>
            </li>

            <li class="nav-item">
              <router-link class="nav-link" exact to="/Results"
                >المباريات</router-link
              >
            </li>
            <li class="nav-item">
              <router-link class="nav-link" exact to="/Transfers"
                >آخر الانتقالات</router-link
              >
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/Expectations">
                مسابقة التوقعات</router-link
              >
            </li>
          </ul>
        </div>
        <div class="social-media">
          <ul v-for="(url, index) in social" :key="index">
            <li class="facebook">
              <a :href="url.facebook" target="_blank">
                <i class="fa-fw fab fa-facebook-f"></i>
              </a>
            </li>
            <li class="instagram">
              <a :href="url.instagram" target="_blank">
                <i class="fa-fw fab fa-instagram"></i>
              </a>
            </li>
            <li class="youtube">
              <a :href="url.youtube" target="_blank">
                <i class="fa-fw fab fa-youtube"></i>
              </a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>


<style scoped lang="scss">
a {
  font-weight: bold;
  color: #2c3e50;

  &.router-link-exact-active {
    color: #42b983;
  }
}
</style>



<script>
import instance from "../../plugin/axios";

export default {
  name: "Header",
  data: function () {
    return {
      social: [],
    };
  },

  methods: {
    async getSocial() {
      let social = this.social;
      await instance
        .get("/social/")
        .then(function (res) {
          // handle success
          social.push(res.data);
        })
        .catch(function (error) {
          // handle error
          console.log(error);
        });
    },
  },
  async created() {
    this.getSocial();
    //
    //
    //
  },
  mounded() {},
};
</script>