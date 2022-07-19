<template>
  <main class="post">
    <div class="container">
      <div class="row">
        <div class="col-lg-9">
          <div class="right px-3 py-2 mb-4">
            <h1>
              {{ post.title }}
            </h1>
            <img class="w-100 lazy" :src="post.image" :alt="post.title" />
            <div v-html="post.content"></div>
          </div>
          

              <!-- url="https://www.npmjs.com/package/vue-social-sharing" -->
          <ShareNetwork
              network="facebook"
              :url="shareUrl"
              :title="post.title"
              :description="post.title"
              class="mx-4"
            >
            <svg version="1.1" width="50" height="50" id="Capa_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
              viewBox="0 0 112.196 112.196" style="enable-background:new 0 0 112.196 112.196;" xml:space="preserve">
                <g>
                  <circle style="fill:#3B5998;" cx="56.098" cy="56.098" r="56.098"/>
                  <path style="fill:#FFFFFF;" d="M70.201,58.294h-10.01v36.672H45.025V58.294h-7.213V45.406h7.213v-8.34
                    c0-5.964,2.833-15.303,15.301-15.303L71.56,21.81v12.51h-8.151c-1.337,0-3.217,0.668-3.217,3.513v7.585h11.334L70.201,58.294z"/>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
                <g>
                </g>
              </svg>

          </ShareNetwork>

          <ShareNetwork
              network="whatsapp"
              :url="shareUrl"
              :title="post.title"
              :description="post.title"
            >
            <svg version="1.1" width="50" height="50" id="Capa_2" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
                viewBox="0 0 58 58" style="enable-background:new 0 0 58 58;" xml:space="preserve">
              <g>
                <path style="fill:#2CB742;" d="M0,58l4.988-14.963C2.457,38.78,1,33.812,1,28.5C1,12.76,13.76,0,29.5,0S58,12.76,58,28.5
                  S45.24,57,29.5,57c-4.789,0-9.299-1.187-13.26-3.273L0,58z"/>
                <path style="fill:#FFFFFF;" d="M47.683,37.985c-1.316-2.487-6.169-5.331-6.169-5.331c-1.098-0.626-2.423-0.696-3.049,0.42
                  c0,0-1.577,1.891-1.978,2.163c-1.832,1.241-3.529,1.193-5.242-0.52l-3.981-3.981l-3.981-3.981c-1.713-1.713-1.761-3.41-0.52-5.242
                  c0.272-0.401,2.163-1.978,2.163-1.978c1.116-0.627,1.046-1.951,0.42-3.049c0,0-2.844-4.853-5.331-6.169
                  c-1.058-0.56-2.357-0.364-3.203,0.482l-1.758,1.758c-5.577,5.577-2.831,11.873,2.746,17.45l5.097,5.097l5.097,5.097
                  c5.577,5.577,11.873,8.323,17.45,2.746l1.758-1.758C48.048,40.341,48.243,39.042,47.683,37.985z"/>
              </g>
              <g>
              </g>
              <g>
              </g>
              <g>
              </g>
              <g>
              </g>
              <g>
              </g>
              <g>
              </g>
              <g>
              </g>
              <g>
              </g>
              <g>
              </g>
              <g>
              </g>
              <g>
              </g>
              <g>
              </g>
              <g>
              </g>
              <g>
              </g>
              <g>
              </g>
            </svg>

          </ShareNetwork>

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
  name: "Post",

  data() {
    return {
      id: this.$route.params.id,
      post: null,
      shareUrl: `http://yallashotalkora.com/#/Post/${this.$route.params.id}`
    };
  },
  metaInfo: {
    meta: [
      { name: "keywords", content: "Test;kldfmmmmmmmmmmmmmm " },
      { name: "description", content: "dkfdfm;dflmdf;ldfmd;lf " },
    ],
  },

  methods: {
    ...mapActions("postsModule", ["getPost"]),
  },

  computed: {
    ...mapGetters("postsModule", ["posts"]),
  },

  async created() {
    this.post = await this.getPost(this.id);

    document.title = this.post.title + " | يلا شوت الكورة";
    document.head
      .querySelector('meta[name="keywords"]')
      .setAttribute("content", this.post.title.split(" "));
    document.head
      .querySelector('meta[name="description"]')
      .setAttribute("content", this.post.title);
    document.head
      .querySelector("meta[name='og-url']")
      .setAttribute("content", `http://yallashotalkora.com${this.post.image}`);

      
  },
  mounted() {},
};
</script>