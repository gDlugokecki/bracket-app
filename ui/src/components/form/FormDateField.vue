<script setup lang="ts">
import { cn } from '@/lib/utils'
import type { DateValue } from '@internationalized/date'
import { CalendarDate, DateFormatter, getLocalTimeZone } from '@internationalized/date'
import { CalendarIcon } from 'lucide-vue-next'
import { Field as VeeField } from 'vee-validate'
import { ref } from 'vue'

import { Button } from '@/components/ui/button'
import { Calendar } from '@/components/ui/calendar'
import { Field, FieldLabel, FieldError, FieldDescription } from '@/components/ui/field'
import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover'


type Props = {
  name: string
  label: string
  placeholder?: string
  description?: string
}

defineProps<Props>()

const open = ref(false)
const df = new DateFormatter('en-US', { dateStyle: 'long' })

function toCalendarDate(value: unknown): DateValue | undefined {
  if (!value) return undefined
  if (typeof value === 'string') {
    const [year, month, day] = value.split('-').map(Number)
    return new CalendarDate(year, month, day)
  }
  if (value instanceof Date) {
    return new CalendarDate(value.getFullYear(), value.getMonth() + 1, value.getDate())
  }
  return value as DateValue
}

function toStringValue(date: DateValue): string {
  return `${date.year}-${String(date.month).padStart(2, '0')}-${String(date.day).padStart(2, '0')}`
}
</script>

<template>
  <VeeField v-slot="{ value, setValue, errors }" :name="name">
    <Field>
      <FieldLabel :for="name">{{ label }}</FieldLabel>
      <Popover v-model:open="open">
        <PopoverTrigger as-child>
          <Button
            :id="name"
            variant="outline"
            :class="
              cn('w-full cursor-pointer justify-start text-left font-normal', !value && 'text-muted-foreground')
            "
            :aria-invalid="!!errors.length"
          >
            <CalendarIcon class="mr-2 size-4" />
            <span>{{
              value
                ? df.format(toCalendarDate(value)!.toDate(getLocalTimeZone()))
                : (placeholder ?? 'Pick a date')
            }}</span>
          </Button>
        </PopoverTrigger>
        <PopoverContent align="start" class="w-auto p-0">
          <Calendar
            :model-value="toCalendarDate(value)"
            initial-focus
            @update:model-value="
              (d) => {
                if (d) {
                  setValue(toStringValue(d))
                  open = false
                }
              }
            "
          />
        </PopoverContent>
      </Popover>
      <FieldDescription v-if="description">{{ description }}</FieldDescription>
      <FieldError v-if="errors.length">{{ errors[0] }}</FieldError>
    </Field>
  </VeeField>
</template>
