import type { VariantProps } from 'class-variance-authority'
import { cva } from 'class-variance-authority'

export const typographyVariants = cva('text-foreground', {
  variants: {
    variant: {
      h1: 'text-4xl font-extrabold tracking-tight lg:text-5xl',
      h2: 'text-3xl font-semibold tracking-tight',
      h3: 'text-2xl font-semibold tracking-tight',
      h4: 'text-xl font-semibold tracking-tight',

      p: 'text-base leading-7',
      xl: 'text-xl font-semibold text-foreground',

      lead: 'text-xl text-muted-foreground leading-relaxed',
      muted: 'text-muted-foreground',
      smallMuted: 'text-sm text-muted-foreground',
    },
  },
  defaultVariants: {
    variant: 'p',
  },
})

export type TypographyVariants = VariantProps<typeof typographyVariants>
