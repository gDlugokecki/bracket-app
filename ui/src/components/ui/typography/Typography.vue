<script setup lang="ts">
import { cn } from '@/lib/utils'
import { Primitive } from 'reka-ui'
import type { PrimitiveProps } from 'reka-ui'
import type { HTMLAttributes } from 'vue'

import type { TypographyVariants } from './variants'
import { typographyVariants } from './variants'

interface Props extends PrimitiveProps {
  variant?: TypographyVariants['variant']
  class?: HTMLAttributes['class']
}

const props = withDefaults(defineProps<Props>(), {
  as: 'p',
})

// Auto-map variant to HTML element if 'as' is not explicitly provided
const elementMap: Record<string, string> = {
  h1: 'h1',
  h2: 'h2',
  h3: 'h3',
  h4: 'h4',
  p: 'p',
  lead: 'p',
  muted: 'p',
}

const element = props.as === 'p' && props.variant ? elementMap[props.variant] || 'p' : props.as
</script>

<template>
  <Primitive
    data-slot="typography"
    :as="element"
    :as-child="asChild"
    :class="cn(typographyVariants({ variant }), props.class)"
  >
    <slot />
  </Primitive>
</template>
