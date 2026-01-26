<script setup lang="ts">
import { useGetMe } from '@/api/generated/auth/auth'
import { ROUTES } from '@/router/routes'

import BecomePlayer from '@/components/dashboard/BecomePlayer.vue'
import FAB from '@/components/ui/fab/FAB.vue'

const { data, isLoading, error } = useGetMe()
console.log(data, 'DATA')
</script>

<template>
  <div v-if="isLoading">Loading...</div>
  <div v-else-if="error">Error: {{ error.detail }}</div>
  <template v-else-if="data">
    <BecomePlayer :user="data" />
    <div>dashboardView</div>
    <FAB :to="ROUTES.TOURNAMENT_CREATE" label="Create Tournament" />
  </template>
</template>
