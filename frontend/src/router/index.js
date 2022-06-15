import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginPage from '@/pages/LoginPage'
import ContactsPage from '@/pages/ContactsPage'
import ContactBooksPage from '@/pages/ContactBooksPage'
import RegisterPage from '@/pages/RegisterPage'
import { isLoggedIn } from 'axios-jwt'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Login',
      component: LoginPage,
      meta: { requiresAuth: false }

    },
    {
      path: '/register',
      name: 'Register',
      component: RegisterPage,
      meta: { requiresAuth: false }
    },
    {
      path: '/contacts',
      name: 'Contacts',
      component: ContactsPage,
      meta: { requiresAuth: true }
    },
    {
      path: '/contact_books',
      name: 'Contact Books',
      component: ContactBooksPage,
      meta: { requiresAuth: true }
    },
    { path: "*",
      redirect: { name: 'Contacts'} }

  ]
})

router.beforeEach((to, from, next) => {
  const log_status = isLoggedIn()
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // this route requires auth, check if logged in
    // if not, redirect to login page.
    if (!log_status) {
      next({
        path: '/',
        query: { redirect: to.fullPath }
      })
    } else {
      next()
    }
  } else if (to.name == 'Login' && log_status) {
      next({path: '/contacts'})
  } else {  // make sure to always call next()!
    next()
  }
})

export default router;

// const routes = [
//     {
//       path: '/',
//       name: 'Login',
//       component: LoginPage
//     },
//     {
//       path: '/contacts',
//       name: 'Contacts',
//       component: ContactsPage
//     }
//   ]
//
// const router = createRouter({
//   // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
//   history: createWebHistory(),
//   routes, // short for `routes: routes`
// })
//
// export default router
