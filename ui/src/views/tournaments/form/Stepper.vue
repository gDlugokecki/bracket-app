<script lang="ts" setup>
import { CheckIcon } from 'lucide-vue-next'

const steps = [
  { id: 1, name: 'Details', description: 'Basic info' },
  { id: 2, name: 'Format', description: 'Bracket type' },
  { id: 3, name: 'Players', description: 'Add participants' },
  { id: 4, name: 'Review', description: 'Confirm & create' },
]

type Props = {
  currentStep: number
}

const { currentStep } = defineProps<Props>()
</script>

<template>
  <nav class="mb-8">
    <ol class="flex items-center justify-between">
      <li
        v-for="(step, index) in steps"
        :key="step.id"
        class="flex items-center"
        :class="{ 'flex-1': index !== steps.length - 1 }"
      >
        <div class="flex flex-col items-center gap-2">
          <div
            class="flex h-10 w-10 items-center justify-center rounded-full border-2 transition-all duration-200"
            :class="
              currentStep > step.id
                ? 'bg-primary border-primary text-primary-foreground'
                : currentStep === step.id
                  ? 'border-primary text-primary bg-primary/10'
                  : 'border-border text-muted-foreground bg-secondary'
            "
          >
            <CheckIcon v-if="currentStep > step.id" class="h-5 w-5" />
            <span v-else class="text-sm font-semibold">{{ step.id }}</span>
          </div>
          <div class="text-center">
            <p
              class="text-sm font-medium"
              :class="currentStep > step.id ? 'text-foreground' : 'text-muted-foreground'"
            >
              {{ step.name }}
            </p>
            <p class="text-muted-foreground hidden text-xs sm:block">{{ step.description }}</p>
          </div>
        </div>
        <div
          v-if="index < steps.length - 1"
          class="mx-4 -mt-6 h-0.5 flex-1"
          :class="currentStep > step.id ? 'bg-primary' : 'bg-border'"
        />
      </li>
    </ol>
  </nav>
</template>
