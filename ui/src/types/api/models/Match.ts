import type { Player } from '@/types/api/models/Player'

export type Match = {
  id: number
  player1: Player
  player2: Player
  status: string
  scheduledTime: string
  roundNumber: number
  score: string
  winnerId: number
}
