import { type RouteLocationNormalized } from 'vue-router'

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
  } catch {
    const layoutComponent = await import(`@/layouts/LoadLayoutError.vue`)
    route.meta.layoutComponent = layoutComponent.default
  }
}
