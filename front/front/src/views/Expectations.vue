<template>
  <main class="expect">
    <div class="container">
      <div class="expect-header">
        <h1>مسابقة التوقعات</h1>
      </div>

      <div class="expect-list">
        <div class="row">
          <div class="right col-lg-9">
            <div class="expect-list_header">
              <p>المباريات</p>
            </div>
            <div
              class="accordion"
              :id="`accordion${predict.id}`"
              v-for="predict in predicts"
              :key="predict.id"
            >
              <div class="accordion-item">
                <h2 class="accordion-header" :id="`heading${predict.id}`">
                  <button
                    class="accordion-button collapsed"
                    type="button"
                    data-bs-toggle="collapse"
                    :data-bs-target="`#collapse${predict.id}`"
                    aria-expanded="false"
                    :aria-controls="`collapse${predict.id}`"
                  >
                    <span class="date">
                      <p>{{ predict.start_date.split("T")[0] }}</p>
                    </span>
                    <span class="expect-match">
                      <span class="teamA team">
                        <span class="teamName">
                          <p>{{ predict.teamA }}</p>
                        </span>
                        <span class="teamImg">
                          <img
                            class=""
                            :src="predict.teamA_image"
                            :alt="predict.teamA"
                          />
                        </span>
                      </span>
                      <p>-</p>
                      <span class="teamB team">
                        <span class="teamImg">
                          <img
                            class=""
                            :src="predict.teamB_image"
                            :alt="predict.teamB"
                          />
                        </span>
                        <span class="teamName">
                          <p>{{ predict.teamB }}</p>
                        </span>
                      </span>
                    </span>
                    <i class="fa fa-chevron-up"></i>
                  </button>
                </h2>
                <div
                  :id="`collapse${predict.id}`"
                  class="accordion-collapse collapse"
                  :aria-labelledby="`heading${predict.id}`"
                  :data-bs-parent="`accordion${predict.id}`"
                >
                  <form
                    class="expect-form"
                    @submit.prevent="sendData(predict.id)"
                    :id="predict.id"
                  >
                    <div class="row">
                      <div class="col-sm-6 right">
                        <div class="expect-form_header">
                          <p>توقع نتيجة المباراة؟</p>
                        </div>
                        <div class="expect-form_body">
                          <span class="teamA team">
                            <span class="teamImg">
                              <img
                                class=""
                                :src="predict.teamA_image"
                                :alt="predict.teamA"
                              />
                            </span>
                            <span class="teamName">
                              <p>{{ predict.teamA }}</p>
                            </span>
                          </span>
                          <input
                            :class="`number number2 pscore2 resultA${predict.id}`"
                            type="number"
                            id="number1"
                            required
                          />
                          <span>-</span>
                          <input
                            :class="`number number2 pscore2 resultB${predict.id}`"
                            type="number"
                            id="number2"
                            maxlength="2"
                            required
                          />
                          <span class="teamB team">
                            <span class="teamImg">
                              <img
                                class=""
                                :src="predict.teamB_image"
                                :alt="predict.teamB"
                              />
                            </span>
                            <span class="teamName">
                              <p>{{ predict.teamB }}</p>
                            </span>
                          </span>
                        </div>
                      </div>
                      <div class="col-sm-6 left">
                        <div class="expect-form_header">
                          <p>من سيبادر بالتسجيل؟</p>
                        </div>
                        <div class="expect-form_body">
                          <div class="form-check">
                            <input
                              class="form-check-input"
                              type="radio"
                              :name="`socer_first${predict.id}`"
                              :id="`exampleRadios0${predict.id}`"
                              value="TeamA"
                              required
                            />
                            <label
                              class="form-check-label"
                              :for="`exampleRadios0${predict.id}`"
                            >
                              {{ predict.teamA }}
                            </label>
                          </div>
                          <div class="form-check">
                            <input
                              class="form-check-input"
                              type="radio"
                              :name="`socer_first${predict.id}`"
                              :id="`exampleRadios1${predict.id}`"
                              value="NoTeam"
                              required
                            />
                            <label
                              class="form-check-label"
                              :for="`exampleRadios1${predict.id}`"
                            >
                              لا أحد
                            </label>
                          </div>
                          <div class="form-check">
                            <input
                              class="form-check-input"
                              type="radio"
                              :name="`socer_first${predict.id}`"
                              :id="`exampleRadios2${predict.id}`"
                              value="TeamB"
                              required
                            />
                            <label
                              class="form-check-label"
                              :for="`exampleRadios2${predict.id}`"
                            >
                              {{ predict.teamB }}
                            </label>
                          </div>
                        </div>
                      </div>
                      <div class="col-sm-6 mt-3">
                        <input
                          :class="`form-control name${predict.id}`"
                          type="text"
                          placeholder="الاسم"
                          required
                        />
                      </div>
                      <div class="col-sm-6 mt-3">
                        <input
                          :class="`form-control email${predict.id}`"
                          type="email"
                          placeholder="البريد الالكترونى"
                          required
                        />
                      </div>
                      <div class="col-sm-6 mt-3">
                        <input
                          :class="`form-control phone${predict.id}`"
                          type="number"
                          placeholder="موبيل"
                          required
                        />
                      </div>

                      <div class="col-12">
                        <input type="submit" value="إرسال" />
                      </div>
                    </div>
                  </form>
                </div>
              </div>
            </div>

            <div class="check-api" v-if="this.predicts.length == 0">
              <h2>لا توجد مسابقات</h2>
            </div>
          </div>
          <div class="left col-lg-3">
            <div class="side-adv">
              <div id="expect-adv">
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
      </div>
    </div>
  </main>
</template>


<script>
import { mapActions, mapGetters } from "vuex";

export default {
  data() {
    return {
      ads: "",
      adsenseContent: "",
    };
  },
  metaInfo: {
    meta: [
      {
        content: "مسابقة التوقعات",
        name: "twitter:title",
        property: "og:title",
      },
      {
        name: "keywords",
        content:
          "العب وتوقع, توقع نتائج المباريات, اكسب جوائز قيمة من يلا شوت الكوره",
      },
      {
        name: "description",
        content:
          "العب وتوقع نتائج المباريات و اكسب جوائز قيمة من يلا شوت الكوره",
      },
    ],
  },
  components: {},
  methods: {
    ...mapActions("predictModule", ["getPredicts", "addPredicts"]),

    clearInputs(predict_id) {
      document.getElementsByClassName("name" + predict_id)[0].value = "";
      document.getElementsByClassName("email" + predict_id)[0].value = "";
      document.getElementsByClassName("phone" + predict_id)[0].value = "";
      document.getElementsByClassName("resultA" + predict_id)[0].value = "";
      document.getElementsByClassName("resultB" + predict_id)[0].value = "";
      document.querySelector(
        'input[name="socer_first' + predict_id + '"]:checked'
      ).checked = false;
    },

    sendData(predict_id) {
      let name = document.getElementsByClassName("name" + predict_id)[0].value;
      let email = document.getElementsByClassName("email" + predict_id)[0]
        .value;
      let phone = document.getElementsByClassName("phone" + predict_id)[0]
        .value;
      let resultA = document.getElementsByClassName("resultA" + predict_id)[0]
        .value;
      let resultB = document.getElementsByClassName("resultB" + predict_id)[0]
        .value;
      let who_score_first = document.querySelector(
        'input[name="socer_first' + predict_id + '"]:checked'
      ).value;

      let formData = {
        match_id: predict_id,
        name,
        email,
        phone,
        resultA,
        resultB,
        who_score_first,
      };
      console.log('formData', formData.who_score_first);
      if (formData.who_score_first == null ) {
        console.log('jkldflfjkldfdflldfk');
      }
      this.addPredicts(formData);
      this.clearInputs(predict_id);
    },
  },
  async created() {
    const predicts = await this.getPredicts();
  },
  computed: {
    ...mapGetters("predictModule", ["predicts"]),
  },
};
</script>