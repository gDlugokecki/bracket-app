<script setup lang="ts">
import { Field as VeeField } from 'vee-validate'

import { Field, FieldLabel, FieldError, FieldDescription } from '@/components/ui/field'
import { Input } from '@/components/ui/input'

type Props = {
  name: string
  label: string
  type?: 'text' | 'email' | 'password' | 'number' | 'date'
  placeholder?: string
  description?: string
}

const props = withDefaults(defineProps<Props>(), {
  type: 'text',
})
</script>

<template>
  <VeeField v-slot="{ field, errors }" :name="name">
    <Field>
      <FieldLabel :for="name">{{ label }}</FieldLabel>
      <Input
        :id="name"
        v-bind="field"
        :type="type"
        :placeholder="placeholder"
        :aria-invalid="!!errors.length"
      />
      <FieldDescription v-if="description">{{ description }}</FieldDescription>
      <FieldError v-if="errors.length">{{ errors[0] }}</FieldError>
    </Field>
  </VeeField>
</template>
