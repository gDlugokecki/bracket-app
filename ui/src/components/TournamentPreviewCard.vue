<script lang="ts" setup>
import Card from 'primevue/card'
import { RouterLink } from 'vue-router'

defineProps<{
  id: number
  name: string
  startDate: string
  endDate: string
  category: string
}>()

const onCardClick = () => {}
</script>

<template>
  <RouterLink
    :to="{ name: 'tournamentDetails', params: { id: id } }"
    :aria-label="`View details for tournament ${name}`"
  >
    <Card class="gap-2 my-2">
      <template #title>
        {{ name }}
      </template>

      <template #content>
        <div class="flex flex-col">
          <span>{{ startDate }} to {{ endDate }}</span>
          <span>{{ category }}</span>
        </div>
      </template>
    </Card>
  </RouterLink>
</template>
