<script setup lang="ts">
import { useLogout } from '@/api/generated/auth/auth'
import { useAuth } from '@/composables/useAuth'
import { useMutationWithToast } from '@/composables/useMutationWithToast'
import { computed } from 'vue'
import { useRouter } from 'vue-router'

import AppBadge from '@/components/shared/AppBadge.vue'
import { Button } from '@/components/ui/button'

import { ROUTE_NAMES } from '../router/routes'

const router = useRouter()
const { currentUser, logout } = useAuth()
const { mutateAsync: logoutMutation } = useMutationWithToast(useLogout(), {
  successMessage: 'Logged out successfully!',
  onSuccessCallback: () => {
    logout()
    router.push(ROUTE_NAMES.LOGIN)
  },
})

const initials = computed(() => {
  if (!currentUser.value) {
    return ''
  }
  const first = currentUser.value.firstName[0]
  const last = currentUser.value.lastName[0]
  return (first + last).toUpperCase()
})

const handleLogout = async () => {
  await logoutMutation(undefined)
}
</script>

<template>
  <div class="bg-background min-h-screen">
    <header class="border-border bg-card sticky top-0 z-50 border-b">
      <div class="container mx-auto flex max-w-6xl items-center justify-between px-4 py-3">
        <router-link :to="{ name: ROUTE_NAMES.DASHBOARD }" class="text-lg font-semibold">
          <div class="flex items-center justify-center gap-4">
            <AppBadge size="2" />
            <span>Bracket App</span>
          </div>
        </router-link>

        <div v-if="currentUser" class="flex items-center gap-4">
          <div class="flex items-center gap-3">
            <div class="bg-primary/10 flex h-8 w-8 items-center justify-center rounded-full">
              <span class="text-primary text-sm font-medium">{{ initials }}</span>
            </div>
            <span class="text-foreground hidden text-sm sm:block">
              {{ currentUser.firstName }} {{ currentUser.lastName }}
            </span>
          </div>
          <Button variant="ghost" size="sm" @click="handleLogout">Sign out</Button>
        </div>
      </div>
    </header>

    <main class="container mx-auto max-w-6xl px-4">
      <slot />
    </main>
  </div>
</template>
