<script setup lang="ts">
import type { PlayerResponse } from '@/api/generated/bracketAppAPI.schemas'

import { useDateFormat } from '@vueuse/core'

const props = defineProps<{
  team1Players: PlayerResponse[]
  team2Players: PlayerResponse[]
  team1Id: number
  team2Id: number
  winnerTeamId: number | null
  roundNumber: number | null
  score: string | null
  scheduledTime: string
  isTopCard: boolean
}>()

const getFullName = (player: PlayerResponse) => {
  return `${player.first_name} ${player.last_name}`
}

const getTeamName = (players: PlayerResponse[]) => {
  if (players.length === 0) return 'TBD'
  if (players.length === 1) return getFullName(players[0])
  return players.map(getFullName).join(' / ')
}

const isWinningTeam = (teamId: number) => {
  return props.winnerTeamId === teamId
}
</script>

<template>
  <template>
    <div :class="{ 'font-bold': isWinningTeam(team1Id) }">
      {{ getTeamName(team1Players) }}
      <span v-if="isWinningTeam(team1Id) && score" class="ml-2">{{ score }}</span>
      <div class="text-sm text-gray-500">
        {{ useDateFormat(scheduledTime, 'YYYY-MM-DD HH:mm') }}
      </div>
    </div>

    <hr class="my-2" />

    <div :class="{ 'font-bold': isWinningTeam(team2Id) }">
      {{ getTeamName(team2Players) }}
      <span v-if="isWinningTeam(team2Id) && score" class="ml-2">{{ score }}</span>
    </div>
  </template>
</template>
