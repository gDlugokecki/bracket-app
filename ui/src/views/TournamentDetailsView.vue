<script setup lang="ts">
import ProgressSpinner from 'primevue/progressspinner'
import { useRoute } from 'vue-router'

import { useFetch } from '@vueuse/core'

import MatchCard from '@/components/MatchCard.vue'

import type { MatchResponse } from '@/types/api/responses/MatchResponse'
import type { TournamentResponse } from '@/types/api/responses/TournamentResponse'
import type { Match } from '@/types/api/models/Match'
import { computed, reactive, watchEffect } from 'vue'

const apiUrl = import.meta.env.VITE_API_URL
const route = useRoute()
const tournamentId = route.params.id

const {
  data: tournamentDetails,
  error: tournamentDetailsError,
  isFetching: isTournamentDetailsFetching,
} = useFetch(apiUrl + `/tournament/${tournamentId}`)
  .get()
  .json<TournamentResponse>()

const {
  data: matches,
  error,
  isFetching: isMatchesFetching,
} = useFetch(apiUrl + `/tournament/${tournamentId}/matches`)
  .get()
  .json<MatchResponse[]>()

const matchesPerRound = computed(() => {
  if (!matches.value) {
    return {}
  }

  return matches.value.reduce(
    (acc, curr) => {
      if (!acc[curr.roundNumber]) {
        acc[curr.roundNumber] = []
      }
      acc[curr.roundNumber].push(curr)
      return acc
    },
    {} as Record<number, Match[]>,
  )
})
</script>

<template>
  <h2 class="mb-3 text-center text-3xl font-bold text-black underline dark:text-white">
    {{ tournamentDetails?.name }}
  </h2>
  <div class="grid auto-cols-[minmax(204px,1fr)] grid-flow-col gap-8">
    <div v-for="item in Object.keys(matchesPerRound)" class="grid items-center gap-y-8">
      <MatchCard
        v-for="match in matchesPerRound[Number(item)]"
        :player1="match.player1"
        :player2="match.player2"
        :round-number="match.roundNumber"
        :scheduled-time="match.scheduledTime"
        :score="match.score"
        :winnerId="match.winnerId"
      />
    </div>
  </div>
  <ProgressSpinner v-if="isMatchesFetching || isTournamentDetailsFetching" />
</template>
