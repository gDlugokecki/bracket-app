<script setup lang="ts">
import { Field as VeeField } from 'vee-validate'

import { Field, FieldLabel, FieldError, FieldDescription } from '@/components/ui/field'
import { Textarea } from '@/components/ui/textarea'

type Props = {
  name: string
  label: string
  placeholder?: string
  description?: string
}

defineProps<Props>()
</script>

<template>
  <VeeField v-slot="{ field, errors }" :name="name">
    <Field>
      <FieldLabel :for="name">{{ label }}</FieldLabel>
      <Textarea
        :id="name"
        v-bind="field"
        :placeholder="placeholder"
        :aria-invalid="!!errors.length"
      />
      <FieldDescription v-if="description">{{ description }}</FieldDescription>
      <FieldError v-if="errors.length">{{ errors[0] }}</FieldError>
    </Field>
  </VeeField>
</template>
