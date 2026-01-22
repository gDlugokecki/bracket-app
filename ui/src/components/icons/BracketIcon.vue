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
    class="size-6"
    :class="[`size-${props.size}`, props.class]"
    viewBox="0 0 32 32"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      d="M4 5V11H8V8H12V16H8V13H4V19"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
    <path
      d="M4 27V21H8V24H12V16"
      stroke="currentColor"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
    <path d="M12 16H20" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" />
    <path
      d="M26 12L27.5 15H31L28.25 17.5L29.5 21L26 18.75L22.5 21L23.75 17.5L21 15H24.5L26 12Z"
      fill="currentColor"
    />
  </svg>
</template>
