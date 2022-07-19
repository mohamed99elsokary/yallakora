<template>
  <div>
    <div class="header">
      <button
        @click="
          changeMatches(true), getTodayMatches(matches, new Date().getDate())
        "
        :class="{ active: todayMatches }"
      >
        مباريات اليوم
      </button>
      <button
        @click="
          changeMatches(false),
            getTodayMatches(matches, new Date().getDate() + 1)
        "
        :class="{ active: !todayMatches }"
      >
        مباريات الغد
      </button>
    </div>
    <div class="matches">
      <Match
        v-for="match in filterMatch"
        :key="match.id"
        :id="match.id"
        :tourName="match.tourName"
        :teamA="match.teamA"
        :teamAImg="match.teamA_image"
        :resultA="match.resultA"
        :teamB="match.teamB"
        :teamBImg="match.teamB_image"
        :resultB="match.resultB"
        :timeStart="match.start_date"
        :timeEnd="match.end_date"
        :url="match.url"
        :date="match.date"
      />
      <div class="check-api" v-if="this.filterMatch.length == 0">
        <h2>لا توجد مباريات</h2>
      </div>
    </div>
  </div>
</template>
<script>
import Match from "./Match.vue";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "Matches",
  data() {
    return {
      time: "",
      status: "",

      todayMatches: true,
      filterMatch: this.filterMatch,
    };
  },
  props: ["title"],
  components: {
    Match,
  },
  methods: {
    ...mapActions("matchesModule", ["getMatches"]),

    changeMatches(x) {
      this.todayMatches = x;
    },

    getTodayMatches(matches, day) {
      const today = new Date();
      const monthNum = [
        "01",
        "02",
        "03",
        "04",
        "05",
        "06",
        "07",
        "08",
        "09",
        "10",
        "11",
        "12",
      ];
      let month = monthNum[today.getMonth()];
      const year = today.getFullYear();

      const t_Day = ("0" + day).slice(-2);

      const fullDate = year + "-" + month + "-" + t_Day;

      //filter
      let filterMatch = matches.filter((match) => {
        let match_date = match.start_date.split("T")[0];

        if (match_date == fullDate) {
          return true;
        } else {
          return false;
        }
      });

      this.filterMatch = filterMatch;
    },
  },

  async created() {
    const matches = await this.getMatches();
    this.getTodayMatches(matches, new Date().getDate());
  },
  computed: {
    ...mapGetters("matchesModule", ["matches"]),
  },
};
</script>