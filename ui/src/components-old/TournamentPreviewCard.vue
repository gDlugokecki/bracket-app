<script lang="ts" setup>
import { RouterLink } from 'vue-router'

defineProps<{
  id: number
  name: string
  startDate: string
  endDate: string
  category: string
}>()
</script>

<template>
  <RouterLink
    :to="{ name: 'tournamentDetails', params: { id: id } }"
    :aria-label="`View details for tournament ${name}`"
  >
    <template>
      {{ name }}
    </template>

    <template>
      <div class="flex flex-col">
        <span>{{ startDate }} to {{ endDate }}</span>
        <span>{{ category }}</span>
      </div>
    </template>
  </RouterLink>
</template>
