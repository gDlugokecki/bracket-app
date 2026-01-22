<script setup lang="ts">
import { useListTournaments } from '@/api/generated/tournaments/tournaments'
import Spinner from '@/components-old/Spinner.vue'
import TournamentPreviewCard from '@/components-old/TournamentPreviewCard.vue'

import TournamentForm from './tournaments/TournamentForm.vue'

const { data: tournaments, error, isPending: isFetching } = useListTournaments()
</script>

<template>
  <Spinner v-if="isFetching" />

  <div v-if="error">Error: {{ error }}</div>

  <h2 class="text-3xl font-bold text-black underline dark:text-white">Tournaments</h2>

  <TournamentPreviewCard
    v-for="tournament in tournaments"
    :key="tournament.id"
    :id="tournament.id"
    :category="tournament.category"
    :endDate="tournament.endDate"
    :startDate="tournament.startDate"
    :name="tournament.name"
  />
  <TournamentForm />
</template>
