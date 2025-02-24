import { type RouteLocationNormalized } from 'vue-router'

/**
 * This middleware is used to dynamically update the Layouts system.
 *
 * As soon as the route changes, it tries to pull the layout that we want to display from the laptop. Then it loads the layout component, and assigns the loaded component to the meta in the layout Component variable. And layoutComponent is used in the basic layout AppLayout.vue, there is a dynamic update of the layout component
 *
 * If the layout we want to display is not found, loads the default layout App Layout Default.vue
 * */
export async function loadLayoutMiddleware(route: RouteLocationNormalized) {
  try {
    let layout, layoutComponent
    if (route.meta?.layout) {
      layout = route.meta.layout
      layoutComponent = await import(`@/layouts/${layout}.vue`)
    } else {
      layoutComponent = await import('@/layouts/DefaultLayout.vue')
    }
    route.meta.layoutComponent = layoutComponent.default
  } catch (e) {
    let layoutComponent = await import(`@/layouts/LoadLayoutError.vue`)
    route.meta.layoutComponent = layoutComponent.default
  }
}
