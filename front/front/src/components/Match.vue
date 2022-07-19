<template>
  <div class="match">
    <router-link
      v-if="this.status == 'مباشر'"
      :to="{ name: 'Live', params: { id: id } }"
    >
    </router-link>

    <div class="tourName">
      <p class="text-center">
        {{ tourName }}
      </p>
    </div>
    <div class="match-details">
      <div class="teamA team">
        <img :src="teamAImg" :alt="teamA" />

        <p>{{ teamA }}</p>
      </div>
      <div class="resultDiv">
        <div v-if="this.status == 'لم يبدأ'" class="notyet">
          <p class="vs en">VS</p>
        </div>

        <div v-if="this.status !== 'لم يبدأ'" class="matchResult en">
          <span class="resultA">{{ resultA }}</span>
          <span>:</span>
          <span class="resultB">{{ resultB }}</span>
        </div>
        <div class="matchStatus">
          <p class="status">{{ this.status }}</p>

          <p class="time">{{ timeStart.split("T")[1].slice(0, -9) }}</p>
        </div>
      </div>
      <div class="teamB team">
        <img :src="teamBImg" :alt="teamB" />

        <p>{{ teamB }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Match",
  props: [
    "id",
    "tourName",
    "teamA",
    "teamAImg",
    "resultA",
    "teamB",
    "teamBImg",
    "resultB",
    "timeStart",
    "timeEnd",
    "url",
    "date",
  ],

  data: function () {
    return {
      time: "",
      status: "",
    };
  },

  components: {},
  methods: {
    getTime() {
      const today = new Date();
      const hour = today.getHours();
      const minute = today.getMinutes();

      const timeStart = this.timeStart.split("T")[1].slice(0, -9);
      const dayStart = this.timeStart.split("T")[0].split("-")[2];
      const day = today.getDate();
      const timeEnd = this.timeEnd.split("T")[1].slice(0, -9);
      const time =
        String(hour).padStart(2, "0") + ":" + String(minute).padStart(2, "0");

      if (time >= timeStart && time < timeEnd && day == dayStart) {
        this.status = "مباشر";
      } else if (time > timeStart && time > timeEnd && day == dayStart) {
        this.status = "انتهت";
      } else {
        this.status = "لم يبدأ";
      }
    },
  },
  created() {
    this.getTime();
  },
  computed: {},
};
</script>



