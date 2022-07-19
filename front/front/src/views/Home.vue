<template>
  <main class="home">
    <Carousel />
    <section class="matches-list">
      <div class="container">
        <div class="row">
          <aside class="col-md-8">
            <Matches />
          </aside>
          <div class="left col-md-4">
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
    </section>

    <section class="news-list">
      <div class="container">
        <div class="list_header">
          <p>آخر الأخبار</p>
        </div>
        <div class="post-container" v-if="this.posts.length !== 0">
          <ul class="posts">
            <li
              :class="`post post${index + 1}`"
              v-for="(post, index) in slicePosts"
              :key="post.id"
            >
              <router-link :to="{ name: 'Post', params: { id: post.id } }">
                <img class="w-100" :src="post.image" :alt="post.title" />
                <div class="desc">
                  <p>{{ post.title }}</p>
                </div>
              </router-link>
            </li>
          </ul>
          <div class="table-foot">
            <router-link class="nav-link" to="/News">
              جميع الأخبار
              <i class="fa fa-chevron-left"></i>
            </router-link>
          </div>
        </div>
        <div class="check-api" v-else>
          <h2>لا توجد أخبار</h2>
        </div>
      </div>
    </section>

    <section class="transfers-list">
      <div class="container">
        <div class="list_header">
          <p>آخر الانتقالات</p>
        </div>
        <div class="transfer-container" v-if="this.transfers.length !== 0">
          <div class="table-responsive">
            <table class="table table-borderless">
              <thead>
                <tr>
                  <th scope="col">التاريخ</th>
                  <th scope="col">اللاعب</th>
                  <th scope="col">إنتقل من</th>
                  <th scope="col"></th>
                  <th scope="col">إنتقل الى</th>
                  <th scope="col">تفاصيل الصفقة</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="transfer in slicetransfers" :key="transfer.id">
                  <th scope="row">
                    {{ transfer.transfer_date.split("T")[0] }}
                  </th>
                  <td>
                    <img
                      :src="transfer.player_image"
                      v-if="transfer.player_image"
                      :alt="transfer.player_name"
                    />

                    <span>{{ transfer.player_name }}</span>
                  </td>
                  <td>{{ transfer.from_team }}</td>
                  <td>
                    <i class="fa fa-arrow-left"></i>
                  </td>
                  <td>{{ transfer.to_team }}</td>
                  <td>{{ transfer.info }}</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="table-foot">
            <router-link class="nav-link" to="/Transfers"
              >جميع الانتقالات
              <i class="fa fa-chevron-left"></i>
            </router-link>
          </div>
        </div>
        <div class="check-api" v-else>
          <h2>لا توجد انتقالات</h2>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import Matches from "@/components/Matches.vue";
import Carousel from "@/components/Carousel.vue";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "Home",
  metaInfo: {
    meta: [
      {
        name: "keywords",
        content:
          "اخبار الكورة ,الرياضة المصرية ,العالمية .مواعيد المباريات , يلا شوت كورة, yallashotalkora, yalla shot, yalla shot alkora",
      },
      {
        name: "description",
        content:
          "موقع يلا شوت الجديد الرسمي | Yalla Shoot New أهم مباريات اليوم جوال بث مباشر يلاشوت حصري بدون تقطيع كورة لايف يلا شووت yalla shoot ماتش موبايل لبث المباريات.",
      },
    ],
  },
  data() {
    return {};
  },
  components: {
    Matches,
    Carousel,
  },
  methods: {
    ...mapActions("postsModule", ["getPosts"]),
    ...mapActions("transferModule", ["getTransfer"]),
  },
  created() {
    this.getPosts();
    this.getTransfer();
  },
  computed: {
    ...mapGetters("postsModule", ["posts"]),
    ...mapGetters("transferModule", ["transfers"]),

    slicePosts() {
      return this.posts.slice(0, 4);
    },

    slicetransfers() {
      return this.transfers.slice(0, 4);
    },
  },
  mounted() {},
};
</script>

