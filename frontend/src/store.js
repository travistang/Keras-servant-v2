import Vue from 'vue'
import Vuex from 'vuex'
import VueSocketio from 'vue-socket.io'
import Parse from 'parse'
Vue.use(Vuex)

Parse.initialize('KERAS_SERVANT','KERAS_SERVANT')
Parse.serverURL = 'http://localhost:1337/parse'

const tasks = {
  state: {
    tasks: [{
      id: 1,
      name: "Example task 1",
      status: "Completed"
    }],
    taskAttributes: ["Name","Status"],

  },
  mutations: {
    add_task(state,task) {
      state.tasks.push(task)
    }
  },
  getters: {
    getTaskList: state => state.tasks
  },
  actions: {
  },
}
const parseStore = {
  state: {
    parseServer: Parse,
    applicationId: "KERAS_SERVANT",
    masterKey: "KERAS_SERVANT",
    serverURL: "http://localhost:1337/parse",
    serverLiveQueryURL: "ws://localhost:1337/parse"
  }
}
const store = new Vuex.Store({
  modules: {
    tasks: tasks,
    parse: parseStore,
  },
  state: {
    connected: false
  },
  mutations: {
  },
  actions: {
  }
})

export default store
