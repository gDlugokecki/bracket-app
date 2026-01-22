<script setup lang="ts">
import BracketIcon from '../icons/BracketIcon.vue'

interface Props {
  size?: string | number
}

const props = defineProps<Props>()
</script>

<template>
  <div
    :class="[
      'bg-primary/10 border-primary/20 flex items-center justify-center rounded-2xl border p-3',
      `w-${props.size} h-${props.size}`,
    ]"
  >
    <BracketIcon class="text-primary" :size="props.size" />
  </div>
</template>
