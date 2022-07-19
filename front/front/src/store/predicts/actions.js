import instance from "../../plugin/axios.js";

export default {
  async getPredicts({ commit }) {
    const res = await instance.get("/predicts/");
    commit("SET_PREDICTS", res.data);
    return res.data;
  },

  async addPredicts({ commit }, data) {
    const res = await instance
      .post("/predicts/add/", (data = data))

      .catch((error) => {
        alert("Match has already started");
        return Promise.reject(error.response.data.message);
      });
    commit("ADD_PREDICTS", data);
  },
};
