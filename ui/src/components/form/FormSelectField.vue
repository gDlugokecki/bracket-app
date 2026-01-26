<script setup lang="ts">
import { useField } from 'vee-validate'

import { Field, FieldLabel, FieldError, FieldDescription } from '@/components/ui/field'
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'

type SelectOption = {
  label: string
  value: string
}

type Props = {
  name: string
  label: string
  placeholder?: string
  description?: string
  options: SelectOption[]
}

const props = defineProps<Props>()

const { value, errorMessage, handleChange } = useField<string>(() => props.name)
</script>

<template>
  <Field>
    <FieldLabel :for="name">{{ label }}</FieldLabel>
    <Select :model-value="value" @update:model-value="handleChange">
      <SelectTrigger>
        <SelectValue :placeholder="placeholder" />
      </SelectTrigger>
      <SelectContent>
        <SelectItem
          v-for="option in options"
          :key="option.value"
          :value="option.value"
        >
          {{ option.label }}
        </SelectItem>
      </SelectContent>
    </Select>
    <FieldDescription v-if="description">{{ description }}</FieldDescription>
    <FieldError v-if="errorMessage">{{ errorMessage }}</FieldError>
  </Field>
</template>
