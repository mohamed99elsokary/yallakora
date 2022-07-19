import instance from "../../plugin/axios.js";

export default {
  async getPosts({ commit }) {
    const res = await instance.get(`/posts/`);
    commit("SET_POSTS", res.data.results);
    return res.data;
  },

  async addPost({ commit }, page) {
    const res = await instance.get(`/posts/?page=${page}`);
    commit("LOAD_MORE", res.data.results);
    return res.data;
    // commit("ADD_POSTS", res.data.results);
  },

  async getPost({ commit }, id) {
    const res = await instance.get(`/posts/${id}/`);
    commit("GET_POST", res.data.results);
    return res.data;
    // commit("ADD_POSTS", res.data.results);
  },
};
