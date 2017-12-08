import Sidebar from './SideBar.vue'

const SidebarStore = {
  showSidebar: false,
  sidebarLinks: [
    {
      name: 'Dashboard',
      icon: 'ti-panel-alt',
      path: '/admin/overview'
    },
    {
      name: 'Tasks',
      icon: 'ti-menu-alt',
      path: '/admin/tasks'
    },
    {
      name: 'Models',
      icon: 'ti-layout-column3-alt',
      path: '/admin/models'
    },
    {
      name: 'Weights',
      icon: 'ti-package',
      path: '/admin/weights'
    }
  ],
  displaySidebar (value) {
    this.showSidebar = value
  }
}

const SidebarPlugin = {

  install (Vue) {
    Vue.mixin({
      data () {
        return {
          sidebarStore: SidebarStore
        }
      }
    })

    Object.defineProperty(Vue.prototype, '$sidebar', {
      get () {
        return this.$root.sidebarStore
      }
    })
    Vue.component('side-bar', Sidebar)
  }
}

export default SidebarPlugin
