<script setup lang="ts">
import { useListPlayers } from '@/api/generated/players/players'
import { useCreateTournament } from '@/api/generated/tournaments/tournaments'
import Format from '@/views/match/Format.vue'
import Players from '@/views/match/Players.vue'
import Review from '@/views/match/Review.vue'
import { toTypedSchema } from '@vee-validate/zod'
import { useForm } from 'vee-validate'
import { ref } from 'vue'
import * as z from 'zod'

import Button from '@/components/ui/button/Button.vue'

import Stepper from './Stepper.vue'
import Details from './wizard-steps/Details.vue'

const createTournament = useCreateTournament()

const tournamentSchema = toTypedSchema(
  z.object({
    name: z.string().min(3, 'Name must be at least 3 characters'),
    location: z.string().min(1, 'Location is required'),
    startDate: z.string().min(1, 'Start date is required'),
    endDate: z.string().min(1, 'End date is required'),
    playersIds: z.coerce.number().min(2, 'At least 2+ players').max(128, 'Maximum 128 players'),
    category: z.string(),
  }),
)

const { handleSubmit } = useForm({
  validationSchema: tournamentSchema,
  initialValues: {
    name: '',
    location: '',
    startDate: '',
    endDate: '',
    playersIds: 16,
    category: '',
  },
})

const onSubmit = handleSubmit((values) => {
  createTournament.mutate(
    {
      data: values,
    },
    {
      onSuccess: () => {
        console.log('TOURNAMENT CREATED')
      },
      onError: () => {
        console.log('SOME WEIRD ERROR')
      },
    },
  )
})

const players = useListPlayers()
const currentStep = ref(1)

const nextStep = () => {
  currentStep.value = currentStep.value + 1
}
const prevStep = () => {
  currentStep.value = currentStep.value - 1
}
</script>

<template>
  <div class="py-8">
    <form @submit="onSubmit">
      <Stepper :currentStep="currentStep" />
      <Details v-if="currentStep === 1" />
      <Format v-if="currentStep === 2" />
      <Players v-if="currentStep === 3" />
      <Review v-if="currentStep === 4" />
      <div class="flex content-end gap-4">
        <Button variant="secondary" v-if="currentStep > 1" @click="prevStep">Previous</Button>
        <Button v-if="currentStep < 4" @click="nextStep">Next</Button>
        <Button v-if="currentStep === 4" @click="onSubmit">Submit</Button>
      </div>
    </form>
  </div>
</template>
