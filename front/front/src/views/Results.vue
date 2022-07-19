<template>
  <div class="result">
    <main class="mb-5">
      <div class="container">
        <Matches />
      </div>
    </main>
  </div>
</template>

<script>
import Matches from "@/components/Matches.vue";

export default {
  data() {
    return {};
  },
  metaInfo: {
    meta: [
      {
        content: "جدول مباريات",
        name: "twitter:title",
        property: "og:title",
      },
      { name: "keywords", content: "تابع جدول مواعيد مباريات الكورة اليوم" },
      { name: "description", content: "تابع جدول مواعيد مباريات الكورة اليوم" },
    ],
  },
  components: {
    Matches,
  },
  methods: {},
  created() {},
  computed: {},
};
</script>