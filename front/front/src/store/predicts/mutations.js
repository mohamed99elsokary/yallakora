export default {
  SET_PREDICTS(state, value) {
    state.predicts = value;
  },
  ADD_PREDICTS(state, value) {
    state.predicts.push(value);
  },
};
