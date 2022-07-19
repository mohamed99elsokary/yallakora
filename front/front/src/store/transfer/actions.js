import instance from "../../plugin/axios.js";

export default {
  async getTransfer({ commit }) {
    const res = await instance.get("/transfers/");
    commit("SET_TRANSFER", res.data);
  },
};
