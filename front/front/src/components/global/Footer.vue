<template>
  <footer>
    <div class="container">
      <div class="up">
        <img style="height: 27px; width: 263px;" src="../../assets/KORA2.png" alt="YALLA SHOT ALKORA" />

        <!-- <p class="logo">YALLA SHOOT AL KORA</p> -->
      </div>
      <div class="down row">
        <div class="copyright col-sm-6 col-12">
          <p><span>©</span> 2021 جميع الحقوق محفوظة لدى</p>
          <a
            class="copyrightLogo"
            href="https://pythoners-eg.com"
            target="_blank"
            >Pythoners</a
          >
        </div>
        <div class="linksMenu col-sm-6 col-12">
          <router-link title="للإعلان معنا" to="/Advertise"
            >للإعلان معنا</router-link
          ><router-link title="سياسة الخصوصية" to="/policy"
            >سياسة الخصوصية</router-link
          >
        </div>
      </div>
    </div>
  </footer>
</template>


<script>
export default {
  name: "Footer",
};
</script>

 