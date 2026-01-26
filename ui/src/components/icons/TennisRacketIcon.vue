<script setup lang="ts">
interface Props {
  class?: string
  size?: string | number
}

const props = withDefaults(defineProps<Props>(), {
  size: 6,
})
</script>

<template>
  <svg
    xmlns="http://www.w3.org/2000/svg"
    class="size-6"
    :class="[`size-${props.size}`, props.class]"
    fill="none"
    viewBox="0 0 24 24"
    width="24"
    height="24"
  >
    <ellipse
      cx="12"
      cy="9"
      rx="6.5"
      ry="7.5"
      fill="none"
      stroke="currentColor"
      stroke-width="1.5"
    />

    <line x1="12" y1="2" x2="12" y2="16" stroke="currentColor" stroke-width="0.5" opacity="0.5" />
    <line x1="9" y1="4" x2="9" y2="14" stroke="currentColor" stroke-width="0.5" opacity="0.5" />
    <line x1="15" y1="4" x2="15" y2="14" stroke="currentColor" stroke-width="0.5" opacity="0.5" />
    <line x1="6.5" y1="9" x2="17.5" y2="9" stroke="currentColor" stroke-width="0.5" opacity="0.5" />
    <line x1="7.5" y1="6" x2="16.5" y2="6" stroke="currentColor" stroke-width="0.5" opacity="0.5" />
    <line
      x1="7.5"
      y1="12"
      x2="16.5"
      y2="12"
      stroke="currentColor"
      stroke-width="0.5"
      opacity="0.5"
    />

    <rect x="10.5" y="16" width="3" height="7" rx="1" fill="currentColor" />
  </svg>
</template>
