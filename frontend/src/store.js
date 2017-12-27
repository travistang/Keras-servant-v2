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
    taskAttributes: ["Name","Created At"],

  },
  mutations: {
    add_task(state,task) {
      let name = task.get('name')
      let object_id = task.id
      let created_at = new Date(task.get('createdAt'))
      let res = {'name': name,'objectId': object_id}
      res['created at'] = created_at.toDateString()
      state.tasks.push(res)
    },
    update_task(state,task) {
      let id = task.id
      if (id == undefined) return
      for(var i in state.tasks) {
        let curTask = state.tasks[i]
        if(curTask.objectId == id) {
          curTask.name = task.get('name')
        }
      }
    },
    delete_task(state,task) {
      let id = task.id
      let res = []
      for(var i in state.task) {
        let curTask = state.tasks[i]
        if(curTask.objectId != id) {
          res.push(curTask)
        }
      }
      state.tasks = res
    },
    clear_task(state) {
      state.tasks = []
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
