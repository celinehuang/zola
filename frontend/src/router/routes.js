const routes = [
  { path: "", redirect: "/login" },
  {
    path: "/login",
    component: () => import("pages/LoginPage.vue"),
    children: []
  },
  {
    path: "/home",
    component: () => import("layouts/MainLayout.vue"),
    meta: { requiresAuth: true },
    children: [{ path: "", component: () => import("pages/Home.vue") }]
  },
  {
    path: "/edit-profile",
    component: () => import("layouts/MainLayout.vue"),
    meta: { requiresAuth: true },
    children: [{ path: "", component: () => import("pages/EditProfile.vue") }]
  },
  {
    path: "/order-history",
    component: () => import("layouts/MainLayout.vue"),
    meta: { requiresAuth: true },
    children: [{ path: "", component: () => import("pages/OrderHistory.vue") }]
  },
  {
    path: "/my-listings",
    component: () => import("layouts/MainLayout.vue"),
    meta: { requiresAuth: true },
    children: [{ path: "", component: () => import("pages/MyListings.vue") }]
  },
  {
    path: "/messages",
    component: () => import("layouts/MainLayout.vue"),
    meta: { requiresAuth: true },
    children: [{ path: "", component: () => import("pages/Messages.vue") }]
  },
  {
    path: "/change-password",
    component: () => import("layouts/MainLayout.vue"),
    meta: { requiresAuth: true },
    children: [
      { path: "", component: () => import("pages/ChangePassword.vue") }
    ]
  }
];

// Always leave this as last one
if (process.env.MODE !== "ssr") {
  routes.push({
    path: "*",
    component: () => import("pages/Error404.vue")
  });
}

export default routes;
