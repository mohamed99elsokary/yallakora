<template>
  <main class="transfers">
    <section class="transfers-list">
      <div class="container">
        <div class="transfers-list_header">
          <p>آخر الانتقالات</p>
        </div>
        <div v-if="this.transfers.length !== 0" class="table-responsive">
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
              <tr v-for="transfer in transfers" :key="transfer.id">
                <th scope="row">{{ transfer.transfer_date.split("T")[0] }}</th>
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
        <div class="check-api" v-else>
          <h2>لا توجد انتقالات</h2>
        </div>
      </div>
    </section>
  </main>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  data() {
    return {};
  },
  metaInfo: {
    meta: [
      {
        content: "آخر الانتقالات",
        name: "twitter:title",
        property: "og:title",
      },
      {
        name: "keywords",
        content: "انتقالات اللاعبيين, سوق انتقالات اللاعبيين, أشاعات الميركاتو",
      },
      {
        name: "description",
        content:
          "تابع أخبار انتقالات اللاعبيين، و كل المفاوضات فى سوق انتقالات اللاعبيين، وأشاعات الميركاتو من يلا شوت الكوره.",
      },
    ],
  },
  components: {
    // Transfer,
  },
  methods: {
    ...mapActions("transferModule", ["getTransfer"]),
  },
  async created() {
    const transfers = this.getTransfer();
  },
  computed: {
    ...mapGetters("transferModule", ["transfers"]),
  },
};
</script>