<script setup lang="ts">
import Card from 'primevue/card'

import type { Player } from '@/types/api/models/Player'
import { useDateFormat } from '@vueuse/core'

defineProps<{
  player1: Player
  player2: Player
  roundNumber: number
  score: string
  scheduledTime: string
  winnerId: number
}>()

const getFullName = (player: Player) => {
  return `${player.firstName} ${player.lastName}`
}

const isWinner = (winnerId: number, playerId: number) => {
  return winnerId === playerId
}
</script>

<template>
  <Card>
    <template #content>
      <div>
        {{ getFullName(player1) }}
        {{ isWinner(winnerId, player1.id) ? score : null }}
        <div>
          {{ useDateFormat(scheduledTime, 'YYYY-MM-DD HH:mm') }}
        </div>
      </div>

      <hr />

      <div>
        {{ getFullName(player2) }}
        {{ isWinner(winnerId, player2.id) ? score : null }}
      </div>
    </template>
  </Card>
</template>
