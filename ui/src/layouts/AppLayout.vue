<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const layoutComponent = computed(() => route.meta.layoutComponent)
</script>

<template>
  <component :is="layoutComponent">
    <slot />
  </component>
</template>
