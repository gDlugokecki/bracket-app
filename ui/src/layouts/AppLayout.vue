<template>
  <div class="w-full">
    <component :is="this.$route.meta.layoutComponent">
      <slot />
    </component>
  </div>
</template>

<script>
export default {
  name: 'AppContainerLayout',
}
</script>
