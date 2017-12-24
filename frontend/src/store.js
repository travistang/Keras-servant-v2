import Vue from 'vue'
import Vuex from 'vuex'
import VueSocketio from 'vue-socket.io'

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
  },
  getters: {
    getTaskList: state => state.tasks
  },
  actions: {
    socket_userMessage(context,message) {
      context.commit("add_task",{name: "message",status:"message"})
    }
  },
}
const store = new Vuex.Store({
  modules: {
    tasks: tasks
  },
  state: {
    connected: false
  },
  mutations: {
    SOCKET_CONNECT: (state,  status ) => {
      state.connected = status;
    },
    SOCKET_USERMESSAGE: (state, message) => {
      this.$socket.emit("Hello","from store")
    }
  },
  actions: {
    socket_connect(context,status) {
      context.commit("add_task",{name:"Socket",status: true})
    },
    socket_userMessage(context,message) {
      console.log("socket message:" + message)
    },
  }
})

export default store
Vue.use(VueSocketio,"http://database.kerasservant.keras",store)
