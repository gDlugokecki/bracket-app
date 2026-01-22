<script lang="ts" setup>
import { cn } from '@/lib/utils'
import {
  CircleCheckIcon,
  InfoIcon,
  Loader2Icon,
  OctagonXIcon,
  TriangleAlertIcon,
  XIcon,
} from 'lucide-vue-next'
import type { ToasterProps } from 'vue-sonner'
import { Toaster as Sonner } from 'vue-sonner'

const props = defineProps<ToasterProps>()
</script>

<style>
/* Success toast styling */
[data-sonner-toast][data-type='success'] {
  background-color: var(--success) !important;
  border-color: var(--success) !important;
  color: var(--success-foreground) !important;
}

[data-sonner-toast][data-type='success'] [data-icon] {
  color: var(--success-foreground) !important;
}

/* Error toast styling */
[data-sonner-toast][data-type='error'] {
  background-color: var(--destructive) !important;
  border-color: var(--destructive) !important;
  color: var(--destructive-foreground) !important;
}

[data-sonner-toast][data-type='error'] [data-icon] {
  color: var(--destructive-foreground) !important;
}

/* Warning toast styling */
[data-sonner-toast][data-type='warning'] {
  background-color: var(--warning) !important;
  border-color: var(--warning) !important;
  color: var(--warning-foreground) !important;
}

[data-sonner-toast][data-type='warning'] [data-icon] {
  color: var(--warning-foreground) !important;
}

/* Info toast styling */
[data-sonner-toast][data-type='info'] {
  background-color: var(--info) !important;
  border-color: var(--info) !important;
  color: var(--info-foreground) !important;
}

[data-sonner-toast][data-type='info'] [data-icon] {
  color: var(--info-foreground) !important;
}
</style>

<template>
  <Sonner
    :class="cn('toaster group', props.class)"
    :style="{
      '--normal-bg': 'var(--popover)',
      '--normal-text': 'var(--popover-foreground)',
      '--normal-border': 'var(--border)',
      '--border-radius': 'var(--radius)',
    }"
    v-bind="props"
  >
    <template #success-icon>
      <CircleCheckIcon class="size-4" />
    </template>
    <template #info-icon>
      <InfoIcon class="size-4" />
    </template>
    <template #warning-icon>
      <TriangleAlertIcon class="size-4" />
    </template>
    <template #error-icon>
      <OctagonXIcon class="size-4" />
    </template>
    <template #loading-icon>
      <div>
        <Loader2Icon class="size-4 animate-spin" />
      </div>
    </template>
    <template #close-icon>
      <XIcon class="size-4" />
    </template>
  </Sonner>
</template>
