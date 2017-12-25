import Vue from 'vue'
import Vuex from 'vuex'
import VueSocketio from 'vue-socket.io'
import Parse from 'parse'
Vue.use(Vuex)

Parse.initialize('KERAS_SERVANT','KERAS_SERVANT')
Parse.serverURL = 'http://localhost:1337/parse'

const tasks = {
  state: {
    tasks: [],
    taskAttributes: ["Name"],

  },
  mutations: {
    add_task(state,task) {
      state.tasks.push(task)
    },
    update_task(state,task) {
      let id = task.objectId
      if (id == undefined) return
      for(var i in state.tasks) {
        let curTask = state.tasks[i]
        if(curTask.objectId == id) {
          curTask.name = task.name
        }
      }
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
