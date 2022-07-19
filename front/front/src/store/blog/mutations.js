export default {
  SET_POSTS(state, value) {
    state.posts = value;
  },
  ADD_POSTS(state, value) {
    state.posts = value;
  },

  LOAD_MORE(state, posts) {
    state.posts.push(...posts);
    console.log(state.posts);
  },

  GET_POST(state, value) {
    state.posts = value;
  },

  // UPDATE_POSTS(state, page) {
  //   // return state.posts.filter(post => value.id)
  //   // let p = state.posts.indexOf((element) => element.id == post.id);
  //   // console.log(state.posts[p]);
  //   // var index = state.posts.findIndex((x) => x.id === post.id);
  //   // state.posts[index] = post;
  // },
  // DELETE_POSTS(state, id) {
  //   var index = state.posts.findIndex((x) => x.id === id);
  //   // console.log(state.posts);
  //   console.log(index);
  //   state.posts.splice(index, 1);
  //   console.log(state.posts);
  // },
};
