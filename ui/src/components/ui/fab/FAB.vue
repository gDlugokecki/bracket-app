<script lang="ts" setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'

const isExpanded = ref(false)

type Props = {
  to: string
  label: string
}

const { to, label } = defineProps<Props>()
</script>

<template>
  <div class="fixed right-6 bottom-6 z-50">
    <RouterLink
      :to="to"
      class="bg-primary hover:bg-primary/90 text-primary-foreground flex h-12 items-center justify-center overflow-hidden rounded-full shadow-lg transition-all duration-300"
      :class="isExpanded ? 'w-52 px-5' : 'w-12'"
      @mouseenter="isExpanded = true"
      @mouseleave="isExpanded = false"
    >
      <span class="text-2xl leading-none font-bold">+</span>
      <span
        class="overflow-hidden leading-none font-medium whitespace-nowrap transition-all duration-300"
        :class="isExpanded ? 'ml-3 max-w-40 opacity-100' : 'ml-0 max-w-0 opacity-0'"
        >{{ label }}</span
      >
    </RouterLink>
  </div>
</template>
