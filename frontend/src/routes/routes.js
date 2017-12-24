import DashboardLayout from '../components/Dashboard/Layout/DashboardLayout.vue'
// GeneralViews
import NotFound from '../components/GeneralViews/NotFoundPage.vue'
import TasksList from '../components/Dashboard/Views/TasksList.vue'
// Admin pages
import Overview from 'src/components/Dashboard/Views/Overview.vue'
import TaskView from 'src/components/Dashboard/Views/TaskView.vue'
const routes = [
  {
    path: '/',
    component: DashboardLayout,
    redirect: '/admin/overview'
  },
  {
    path: '/admin',
    component: DashboardLayout,
    redirect: '/admin/stats',
    children: [
      {
        path: 'overview',
        name: 'overview',
        component: Overview
      },
      {
        path: 'tasks',
        name: 'tasks',
        component: TasksList

      },
      {
      	path: 'tasks/:id',
      	name: 'task_details',
      	component: TaskView,
      },
    ],
  },

  { path: '*', component: NotFound }
]

export default routes
