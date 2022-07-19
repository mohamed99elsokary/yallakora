<template>
  <main class="news">
    <div class="container">
      <div class="news-header">
        <h1>الأخبار</h1>
      </div>
      <div class="row">
        <div class="right col-lg-9">
          <ul class="posts">
            <li class="post" v-for="post in posts" :key="post.id">
              <!-- <router-link :to="`/Post/${post.id}`" -->
              <router-link
                :to="{
                  name: 'Post',
                  params: { id: post.id },
                }"
                ><img class="w-100 lazy" :src="post.image" :alt="post.title" />
                <div class="desc">
                  <p>{{ post.title }}</p>
                </div></router-link
              >
            </li>
          </ul>
          <div class="check-api" v-if="posts == 0">
            <h2>لا توجد أخبار</h2>
          </div>
          <div class="load">
            <button
              v-if="this.loadMore"
              class="btn loadMore"
              @click="incrementCounter"
            >
              مشاهدة المذيد
            </button>
          </div>
        </div>
        <div class="left col-lg-3">
          <div class="side-adv mb-4">
            <iframe
              src="//pantomimethat.com/watchnew?key=004586c55d6d74860332e0838b91e0e5"
              width="300"
              height="250"
              frameborder="0"
              scrolling="no"
            ></iframe>
          </div>
          <div class="side-adv">
            <iframe
              src="//pantomimethat.com/watchnew?key=004586c55d6d74860332e0838b91e0e5"
              width="300"
              height="250"
              frameborder="0"
              scrolling="no"
            ></iframe>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  data() {
    return {
      loadMore: null,
      page: 1,
    };
  },
  metaInfo: {
    meta: [
      { content: "أخبار الرياضة", name: "twitter:title", property: "og:title" },
      { name: "keywords", content: "news" },
      { name: "description", content: "news" },
    ],
  },

  methods: {
    ...mapActions("postsModule", ["getPosts", "addPost"]),

    async incrementCounter() {
      this.page += 1;
      const more = await this.addPost(this.page);
      if (!more.next) {
        this.loadMore = null;
      }
    },
  },
  async created() {
    const posts = await this.getPosts();
    this.loadMore = posts.next;
  },
  destroyed() {},

  computed: {
    ...mapGetters("postsModule", ["posts"]),
  },
  mounted() {},
};
</script>