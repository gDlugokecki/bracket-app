<script setup lang="ts">
import BracketIcon from '@/components/icons/BracketIcon.vue'
import { Button } from '@/components/ui/button'
import { Typography } from '@/components/ui/typography'

import { ROUTES } from '../router/routes'
</script>

<template>
  <div class="flex min-h-screen items-center justify-center px-4">
    <div class="flex w-full max-w-150 flex-col items-center justify-center space-y-3">
      <div
        className="flex items-center justify-center w-20 h-20 rounded-2xl bg-primary/10 border border-primary/20 p-3"
      >
        <BracketIcon class="text-primary size-20" />
      </div>
      <Typography variant="h1">Bracket app</Typography>
      <Typography variant="muted" class="mb-12 text-center"
        >Tournament management for tennis competitions</Typography
      >

      <Button class="w-full" size="xl" as-child
        ><RouterLink :to="ROUTES.SIGNUP"> Create account</RouterLink></Button
      >
      <Button variant="outline" size="xl" class="w-full" as-child
        ><RouterLink :to="ROUTES.LOGIN"> Sign In</RouterLink></Button
      >
    </div>
  </div>
</template>
