<script setup lang="ts">
import ProgressSpinner from 'primevue/progressspinner'
import { computed } from 'vue'
import { useRoute } from 'vue-router'

import { useFetch } from '@vueuse/core'

import MatchCard from '@/components/MatchCard.vue'

import type { Match } from '@/types/api/models/Match'
import type { MatchResponse } from '@/types/api/responses/MatchResponse'
import type { TournamentResponse } from '@/types/api/responses/TournamentResponse'

const apiUrl = import.meta.env.VITE_API_URL
const route = useRoute()
const tournamentId = route.params.id

const {
  data: tournamentDetails,
  error: _tournamentDetailsError,
  isFetching: isTournamentDetailsFetching,
} = useFetch(apiUrl + `/tournament/${tournamentId}`)
  .get()
  .json<TournamentResponse>()

const {
  data: matches,
  error: _error,
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

const maxRoundNumber = computed(() => {
  if (!matchesPerRound.value || Object.keys(matchesPerRound.value).length === 0) {
    return 0
  }

  return Math.max(...Object.keys(matchesPerRound.value).map(Number))
})
const bracketConnectorClasses = (
  isTopCard: boolean,
  isFirstRound: boolean,
  isLastRound: boolean,
) => {
  let classNames =
    "after:content-[''] after:w-[32px] after:absolute after:h-full after:right-[-32px]"

  if (!isFirstRound) {
    classNames +=
      ' before:w-[8px] before:absolute before:top-[50%] before:left-[-8px] before:h-full before:border-t-1'
  }

  if (!isLastRound) {
    classNames += isTopCard
      ? " after:top-[50%] after:border-t-1 after:border-r-1 after:border-white before:content-[''] after:rounded-tr-lg"
      : ' after:bottom-[50%] after:border-b-1 after:border-r-1 after:border-white after:rounded-br-lg'
  }

  return classNames
}
</script>

<template>
  <h2 class="mb-3 text-center text-3xl font-bold text-black underline dark:text-white">
    {{ tournamentDetails?.name }}
  </h2>
  <div class="relative grid auto-cols-[minmax(204px,1fr)] grid-flow-col gap-8">
    <div
      v-bind:key="roundIndex"
      v-for="(item, roundIndex) in Object.keys(matchesPerRound)"
      class="ml-2 grid"
    >
      <div class="grid gap-y-8">
        <div
          v-bind:key="index"
          v-for="(match, index) in matchesPerRound[Number(item)]"
          :class="
            bracketConnectorClasses(
              index % 2 === 0,
              roundIndex === 0,
              maxRoundNumber === Number(item),
            )
          "
          class="relative grid items-center"
        >
          <MatchCard
            :player1="match.player1"
            :player2="match.player2"
            :round-number="match.roundNumber"
            :scheduled-time="match.scheduledTime"
            :score="match.score"
            :winnerId="match.winnerId"
            :is-top-card="index % 2 === 0"
          />
        </div>
      </div>
    </div>
  </div>
  <ProgressSpinner v-if="isMatchesFetching || isTournamentDetailsFetching" />
</template>
