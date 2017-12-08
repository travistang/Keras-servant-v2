import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)
const tasks = {
  state: {
    tasks: [{
      name: "Example task 1",
      status: "Completed"
    }],
    taskAttributes: ["Name","Status"]
  },
  mutations: {
    add_task(state,task) {
      state.tasks.push(task)
    }
  }
}
const store = new Vuex.Store({
  modules: {
    tasks: tasks
  }
})

export default store
