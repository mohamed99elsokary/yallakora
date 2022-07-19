import actions from "./actions";
import getters from "./getters";
import mutations from "./mutations";

export const state = () => ({
  transfers: [],
});

export default { namespaced: true, state, actions, getters, mutations };
