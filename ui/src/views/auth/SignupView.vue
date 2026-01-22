<script setup lang="ts">
import { RouterLink } from 'vue-router'

import AppBadge from '@/components/shared/AppBadge.vue'
import Typography from '@/components/ui/typography/Typography.vue'

import { ROUTES } from '../../router/routes'
import SignupForm from './forms/SignupForm.vue'
</script>

<template>
  <main class="bg-background flex min-h-screen items-center justify-center">
    <div class="flex flex-col">
      <div class="mb-7 flex flex-col items-center">
        <div class="mb-7 flex items-center gap-2">
          <AppBadge size="2" />
          <Typography variant="xl">Bracket app</Typography>
        </div>
        <Typography variant="h2" class="text-center">Create your account</Typography>
        <Typography variant="muted" class="text-center"
          >Get started with tournament management</Typography
        >
      </div>
      <SignupForm />

      <p class="text-muted-foreground mt-6 text-center text-sm">
        Already have an account?
        <RouterLink :to="ROUTES.LOGIN" class="text-primary hover:underline"> Sign In</RouterLink>
      </p>
    </div>
  </main>
</template>
