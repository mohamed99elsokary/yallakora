import instance from "../../plugin/axios.js";

export default {
  async getMatches({ commit }) {
    const res = await instance.get("/matches/");
    commit("SET_MATCHES", res.data);
    console.log('res.data matches', res.data);
    return res.data;
  },
};
