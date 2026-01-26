<script lang="ts" setup>
import FormDateField from '@/components/form/FormDateField.vue'
import FormSelectField from '@/components/form/FormSelectField.vue'
import FormTextAreaField from '@/components/form/FormTextAreaField.vue'
import FormTextField from '@/components/form/FormTextField.vue'
import Card from '@/components/ui/card/Card.vue'
import CardContent from '@/components/ui/card/CardContent.vue'

const categoryLabels = [
  {
    value: 'open',
    label: 'Open',
  },
  { value: 'open-amateur', label: 'Open Amateur' },
  { value: 'amateur', label: 'Amateur' },
  { value: 'beginner', label: 'Beginner' },
  { value: 'junior', label: 'Junior' },
  { value: 'senior', label: 'Senior (40+)' },
  { value: 'super-senior', label: 'Super Senior (55+)' },
  { value: 'womens', label: "Women's" },
  { value: 'mens', label: "Men's" },
  { value: 'mixed', label: 'Mixed Doubles' },
]
</script>

<template>
  <div class="py-8">
    <Stepper />
    <Card class="bg-card border-border">
      <CardContent>
        <FormTextField
          name="name"
          label="Tournament Name"
          placeholder="Summer Championship 2024"
          description="A unique name for your tournament"
        />
        <FormSelectField
          name="category"
          label="Category"
          :options="categoryLabels"
          placeholder="Category"
        />
        <div class="flex gap-4">
          <FormDateField name="date" label="Start date" />
          <FormDateField name="date" label="End date" />
        </div>
        <FormTextField name="location" label="Location" placeholder="City Stadium" />
        <FormTextAreaField
          name="location"
          label="Description"
          placeholder="Add any additional details about the tournament"
        />
      </CardContent>
    </Card>
  </div>
</template>
