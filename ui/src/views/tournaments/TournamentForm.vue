<script setup lang="ts">
import { useListPlayers } from '@/api/generated/players/players'
import { useCreateTournament } from '@/api/generated/tournaments/tournaments'
import { toTypedSchema } from '@vee-validate/zod'
import { useForm } from 'vee-validate'
import * as z from 'zod'

import FormTextField from '@/components/form/FormTextField.vue'
import Card from '@/components/ui/card/Card.vue'
import CardContent from '@/components/ui/card/CardContent.vue'

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
</script>

<template>
  <Card className="bg-card border-border">
    <CardContent class="pt-6">
      <form @submit="onSubmit" class="space-y-4">
        <FormTextField
          name="name"
          label="Tournament Name"
          placeholder="Summer Championship 2024"
          description="A unique name for your tournament"
        />
        <FormTextField name="location" label="Location" placeholder="City Stadium" />
        <FormTextField name="location" label="Location" placeholder="City Stadium" />
      </form>
    </CardContent>
  </Card>
</template>
