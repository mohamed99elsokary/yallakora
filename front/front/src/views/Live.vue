<template>
  <main class="live">
    <div class="container" v-for="match in match" :key="match.id">
      <div class="live-header">
        <div class="match">
          <div class="tourName">
            <p class="text-center">{{ match.tourName }}</p>
          </div>
          <div class="match-details">
            <div class="teamA team">
              <p>{{ match.teamA }}</p>

              <img :src="match.teamA_image" :alt="match.teamA" />
            </div>
            <div class="resultDiv">
              <div class="matchResult en">
                <span class="resultA">{{ match.resultA }} </span>
                <span>:</span>
                <span class="resultB">{{ match.resultB }}</span>
              </div>
              <div class="matchStatus"></div>
            </div>
            <div class="teamB team">
              <img :src="match.teamB_image" :alt="match.teamB" />

              <p>{{ match.teamB }}</p>
            </div>

            <div class="status">
              <span></span>
              <p>مباشر</p>
            </div>
          </div>
        </div>
      </div>

      <div class="my-4" v-html="match.descreption" />

      <Video :url="match.stream_url" />
      <!-- <hr>
      <hr>
      <hr>
      <hr>
      <hr>
      <hr>
      <Video2 :url="match.stream_url" />
      <hr> -->
      <!-- <hr>
      <hr>
      <hr>
      <hr>
      <hr>
      <Video3 />
      <hr>
      <hr> -->



              

    </div>
  </main>
</template>
<script>
import instance from "../plugin/axios";
import Video from '@/components/Video.vue'
import Video2 from "@/components/Video2";
import Video3 from "@/components/Video3";
export default {
  name: "Matches",
  data() {
    return {
      id: "",
      match: [],
    };
  },
  metaInfo: {
    meta: [
      { name: "keywords", content: "" },
      { name: "description", content: "" },
    ],
  },
  components: {
    Video,
    Video2,
    Video3
  },
  methods: {
    async getMatch(id) {
      let match = this.match;
      await instance
        .get("/matches/")
        .then(function (res) {
          // handle success
          let index = res.data.findIndex((x) => x.id === id);
          match.push(res.data[index]);

          console.log('match', match[0]);

          document.title = `بث مباشر مباراة ${res.data[index].teamA} VS ${res.data[index].teamB} | يلا شوت الكورة`;

          document.head
            .querySelector("meta[name='keywords']")
            .setAttribute(
              "content",
              `بث مباشر مباراة ${res.data[index].teamA} VS ${res.data[index].teamB} | يلا شوت الكورة`
            );

          document.head
            .querySelector("meta[name='description']")
            .setAttribute(
              "content",
              `بث مباشر مباراة ${res.data[index].teamA} VS ${res.data[index].teamB} | يلا شوت الكورة`
            );        
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
  async created() {
    let arr = window.location.href.split("/");
    this.id = parseInt(arr[arr.length - 1]);
    this.getMatch(this.id);
  },
  watch: {},
  mounted() {},
  computed: {},
};
</script>