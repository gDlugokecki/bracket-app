<script setup lang="ts">
import { useFetch } from '@vueuse/core'

import Spinner from '@/components/Spinner.vue'
import TournamentPreviewCard from '@/components/TournamentPreviewCard.vue'

import type { TournamentResponse } from '@/types/api/responses/TournamentResponse'

const apiUrl = import.meta.env.VITE_API_URL

const {
  data: tournaments,
  error,
  isFetching,
} = useFetch(apiUrl + '/tournament')
  .get()
  .json<TournamentResponse[]>()
</script>

<template>
  <Spinner v-if="isFetching" />

  <div v-if="error">Error: {{ error }}</div>

  <h2 class="text-3xl font-bold underline text-black dark:text-white">Tournaments</h2>

  <TournamentPreviewCard
    v-for="tournament in tournaments"
    :id="tournament.id"
    :category="tournament.category"
    :endDate="tournament.endDate"
    :startDate="tournament.startDate"
    :name="tournament.name"
  />
</template>
