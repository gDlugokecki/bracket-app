<script setup lang="ts">
import type { MatchResponse } from '@/api/generated/bracketAppAPI.schemas'
import { useGetMatchListMatchesGet } from '@/api/generated/matches/matches'
import { useGetTournament } from '@/api/generated/tournaments/tournaments'
import MatchCard from '@/components-old/MatchCard.vue'
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const tournamentId = Number(route.params.id)

const {
  data: tournamentDetails,
  error: _tournamentDetailsError,
  isPending: isTournamentDetailsFetching,
} = useGetTournament(tournamentId)

const {
  data: matches,
  error: _error,
  isPending: isMatchesFetching,
} = useGetMatchListMatchesGet({ tournament_id: tournamentId })

const matchesPerRound = computed(() => {
  if (!matches.value || matches.value.length === 0) {
    return {}
  }

  return matches.value.reduce(
    (acc, curr) => {
      const roundNum = curr.round_number || 0
      if (!acc[roundNum]) {
        acc[roundNum] = []
      }
      acc[roundNum].push(curr)
      return acc
    },
    {} as Record<number, MatchResponse[]>,
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
            :team1-players="match.team1_players || []"
            :team2-players="match.team2_players || []"
            :team1-id="match.team1_id"
            :team2-id="match.team2_id"
            :winner-team-id="match.winner_team_id"
            :round-number="match.round_number"
            :scheduled-time="match.scheduled_time"
            :score="match.score"
            :is-top-card="index % 2 === 0"
          />
        </div>
      </div>
    </div>
  </div>
</template>
