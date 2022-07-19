<template>
  <section class="intro">
    <div
      id="carouselExampleCaptions"
      class="carousel slide"
      data-bs-ride="carousel"
    >
      <div class="carousel-inner">
        <div class="carousel-item " v-for="(img, index) in images" :class="index == 0 ? 'active': ''" :key="img.id">
          <img
            :src="`http://yallashotalkora.com/${img.image}`"
            class="d-block w-100 main-img"
            :id='index'
            :alt="img.id"
          />
        </div>
        <!-- <div class="carousel-item active">
          <img
            src="../../public/assets/carousel/carousel-1.jpg"
            class="d-block w-100 main-img"
            alt="stadium"
          />
          <div class="carousel-caption d-md-block">
            <h1 class="">بث مباشر</h1>
            <p class="">لجميع المباريات</p>
            <img
              class="scale-up-bottom"
              src="../../public/assets/carousel/png/mo-salah.png"
              alt="mo-salah"
            />
          </div>
        </div> -->
        <!-- <div class="carousel-item">
          <img
            src="../../public/assets/carousel/carousel-4.jpg"
            class="d-block w-100 main-img"
            alt="stadium"
          />
          <div class="carousel-caption d-md-block">
            <h1 class="">افضل جودة</h1>
            <p class="">بدون تقطيع</p>
            <img
              class="scale-up-bottom"
              src="../../public/assets/carousel/png/cr7.png"
              alt="cr7"
            />
          </div>
        </div> -->
      </div>
      <button
        class="carousel-control-prev"
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide="prev"
      >
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button
        class="carousel-control-next"
        type="button"
        data-bs-target="#carouselExampleCaptions"
        data-bs-slide="next"
      >
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
  </section>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      images: []
    };
  },
  methods: {},
  created() {},
  computed: {},
  mounted() {
    axios.get('http://yallashotalkora.com/api/home/images/').then(res => {
      this.images = res.data;
      console.log('res images', this.images[0].image);
      console.log('res images', res.data);
    }).error(err => {console.log(err);})
  }
};
</script>