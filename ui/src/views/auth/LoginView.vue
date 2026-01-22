<script setup lang="ts">
import { RouterLink } from 'vue-router'

import AppBadge from '@/components/shared/AppBadge.vue'
import Typography from '@/components/ui/typography/Typography.vue'

import { ROUTES } from '../../router/routes'
import LoginForm from './forms/LoginForm.vue'
</script>

<template>
  <main class="bg-background flex min-h-screen items-center justify-center">
    <div class="flex flex-col">
      <div class="mb-7 flex flex-col items-center">
        <div class="mb-7 flex items-center gap-2">
          <AppBadge size="2" />
          <Typography variant="xl">Bracket app</Typography>
        </div>
        <Typography variant="h2" class="text-center">Welcome back</Typography>
        <Typography variant="muted" class="text-center">Sign in to your account</Typography>
      </div>
      <LoginForm />

      <p class="text-muted-foreground mt-6 text-center text-sm">
        Already have an account?
        <RouterLink :to="ROUTES.SIGNUP" class="text-primary hover:underline"> Sign up</RouterLink>
      </p>
    </div>
  </main>
</template>
