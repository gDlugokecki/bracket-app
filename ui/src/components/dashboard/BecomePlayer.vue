<script lang="ts" setup>
import type { UserResponse } from '@/api/generated/bracketAppAPI.schemas'
import { ROUTES } from '@/router/routes'
import { RouterLink } from 'vue-router'

import TennisRacketIcon from '../icons/TennisRacketIcon.vue'
import Button from '../ui/button/Button.vue'
import Card from '../ui/card/Card.vue'
import CardContent from '../ui/card/CardContent.vue'

interface Props {
  user: UserResponse
}

const { user } = defineProps<Props>()
</script>
<template>
  <Card
    v-if="!user.isPlayer"
    class="from-primary/10 to-primary/5 border-primary/20 mb-6 bg-linear-to-r"
  >
    <CardContent class="py-5">
      <div class="flex flex-col items-start justify-between gap-4 sm:flex-row sm:items-center">
        <div class="flex items-center gap-4">
          <div class="bg-primary/20 flex h-12 w-12 items-center justify-center rounded-full">
            <TennisRacketIcon class="text-primary rotate-45" />
          </div>
          <div>
            <h3 class="text-foreground font-semibold">Become a Player</h3>
            <p class="text-muted-foreground text-sm">
              Register your tennis profile to join tournaments and track your stats
            </p>
          </div>
        </div>
        <Button>
          <RouterLink :to="ROUTES.PLAYER_CREATE"> Register as Player </RouterLink>
        </Button>
      </div>
    </CardContent>
  </Card>
</template>
